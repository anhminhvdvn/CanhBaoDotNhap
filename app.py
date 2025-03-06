from flask import Flask, render_template, Response
import cv2
import os
import time
from deepface import DeepFace
from threading import Thread, Lock
import datetime

app = Flask(__name__)

# URL của luồng video
# stream_url = 'http://172.16.66.126:8080/video'
# cap = cv2.VideoCapture(stream_url)
# cap.set(cv2.CAP_PROP_BUFFERSIZE, 2)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 2)

# Tạo thư mục lưu ảnh người lạ
INTRUDER_FOLDER = "intruders"
os.makedirs(INTRUDER_FOLDER, exist_ok=True)

video_frame = None
lock = Lock()
last_detection_time = time.time()
last_capture_time = time.time()
detection_interval = 10  # Nhận diện khuôn mặt mỗi 10 giây
capture_interval = 10  # Lưu ảnh người lạ mỗi 10 giây

# Hàm xử lý luồng video và nhận diện khuôn mặt
def camera_stream():
    global cap, video_frame, last_detection_time, last_capture_time
    while True:
        ret, frame = cap.read()
        if not ret:
            time.sleep(0.05)
            continue
        
        frame = cv2.resize(frame, (320, 240))  # Giảm kích thước để tối ưu
        
        # Nhận diện khuôn mặt mỗi 10 giây
        if time.time() - last_detection_time >= detection_interval:
            last_detection_time = time.time()
            try:
                result = DeepFace.find(img_path=frame, db_path="database", model_name="ArcFace", enforce_detection=False)
                if len(result) == 0 or len(result[0]) == 0:
                    print("⚠️ Phát hiện người lạ!")
                    if time.time() - last_capture_time >= capture_interval:
                        last_capture_time = time.time()
                        filename = f"intruder_{int(time.time())}.jpg"
                        filepath = os.path.join(INTRUDER_FOLDER, filename)
                        cv2.imwrite(filepath, frame)
                        print(f"📸 Ảnh người lạ đã lưu tại: {filepath}")
            except Exception as e:
                print("Lỗi nhận diện:", e)
        
        with lock:
            video_frame = frame.copy()

# Hàm phát video trên trình duyệt
def gen_frames():
    global video_frame
    while True:
        with lock:
            if video_frame is None:
                time.sleep(0.1)
                continue
            ret, buffer = cv2.imencode('.jpg', video_frame)
            if not ret:
                continue
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    camera_thread = Thread(target=camera_stream)
    camera_thread.start()
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
