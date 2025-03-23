<h1 align="center">ỨNG DỤNG CÔNG NGHỆ TRONG HỆ THỐNG CẢNH BÁO ĐỘT NHẬP</h1>
<div align="center">


<p align="center">
  <img src="https://raw.githubusercontent.com/anhminhvdvn/CanhBaoDotNhap/main/images/logoDaiNam.png" width="150">
  <img src="https://raw.githubusercontent.com/anhminhvdvn/CanhBaoDotNhap/main/images/LogoAIoTLab.png" width="150">
</p>





<br>

[![Made by AIoTLab](https://img.shields.io/badge/Made%20by%20AIoTLab-blue?style=for-the-badge)](https://www.facebook.com/DNUAIoTLab)
[![Fit DNU](https://img.shields.io/badge/Fit%20DNU-green?style=for-the-badge)](https://fitdnu.net/)
[![DaiNam University](https://img.shields.io/badge/DaiNam%20University-red?style=for-the-badge)](https://dainam.edu.vn)

</div>


## 🌟 Giới thiệu

Hệ thống cảnh báo đột nhập sử dụng công nghệ nhận diện khuôn mặt và cơ sở dữ liệu db. Ứng dụng này cho phép người dùng dễ dàng bảo vệ an ninh của ngôi nhà, thực hiện nhận diện và báo động khi cần thiết.

---

## 🌟 Tính năng chính

- **Nhận diện tự động tự động:** Hệ thống sử dụng camera để quét khuôn mặt người và phát âm thanh khi khuôn mặt được nhận diện. Hệ thống sẽ báo âm thanh chào mừng nếu là người quen ngược lại phát báo động.
- **Thông báo trực quan:** Khi nhận dạng được người có trong dữ liệu, hệ thống sẽ hiển thị thông tin trên giao diện người dùng. Nếu có trường hợp không nhận diện được khuôn mặt sẽ = người lạ sẽ được hiển thị.
- **Quản lý dữ liệu:** Dữ liệu nhận diện và thông tin người quen được lưu trữ trong SQL Server.
- **Giao diện thân thiện:** Sử dụng Python tkinter cho giao diện người dùng với webcam để quét khuôn mặt, xử lý nhận dạng cũng như lưu dữ liệu. Giao diện người dùng được thiết kế đơn giản và dễ sử dụng.
- **Phát hiện khuôn mặt:** Sử dụng thư viện BDPH để phát hiện khuôn mặt và cv2 để xác thực các khuôn mặt so với cơ sở dữ liệu đã lưu trữ.
- **Cải thiện hình ảnh:** Hệ thống cải thiện chất lượng hình ảnh trước khi xác thực bằng các kỹ thuật như tăng độ nét và điều chỉnh độ sáng.

--- 

## 📂 Cấu trúc dự án
BTL_IOT  
├── 📂 data_face            # File lưu ảnh nhận diện  
│   ├── 🖼️ anh1.jpg        # Ảnh tạm lưu trong quá trình nhận diện  
│   ├── 🖼️ anh2.jpg        # Ảnh tạm lưu trong quá trình nhận diện  
├── 📂 intruders            # File lưu ảnh người lạ  
│   ├── 🖼️ anh1.jpg        # Ảnh tạm lưu trong quá trình nhận diện  
│   ├── 🖼️ anh2.jpg        # Ảnh tạm lưu trong quá trình nhận diện  
├── 📂 trainer              # File trainner  
│   ├── 📄 face-trainer.yaml # File trainer  
├── 📄 _alert.mp3           # File âm thanh cảnh báo  
├── 📄 _hello.mp3           # File âm thanh chào mừng  
├── 📄 FaceBase.db          # File dữ liệu database  
├── 📄 giaodien.py          # File code giao diện  
├── 📄 KhuonMat.xml         # File logic nhận diện  
├── 📄 lay_dulieu.py        # File code lấy dữ liệu  
├── 📄 nhan_dien.py         # File code nhận diện  
├── 📄 training.py          # File code training  

 ### 🛠️ CÔNG NGHỆ SỬ DỤNG
<h3 align="center">📡 Phần cứng</h1>


<div align="center"> 
<br>

[![CameraIP](https://img.shields.io/badge/Webcam-000000?style=for-the-badge)](https://www.logitech.com/en-us/products/webcams)
[![MTCNN](https://img.shields.io/badge/MTCNN-00979D?style=for-the-badge)](https://github.com/ipazc/mtcnn)
[![DeepFace](https://img.shields.io/badge/DeepFace-FF5722?style=for-the-badge)](https://github.com/serengil/deepface)

</div>

<h3 align="center">🖥️ Phần mềm</h1>


<div align="center"> 
<br>

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)]() 
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-blue?style=for-the-badge)]() 
[![React](https://img.shields.io/badge/React-17.0.
::contentReference[oaicite:0]{index=0}

</div>

## 🛠️ Yêu cầu hệ thống
### 🔌 Phần cứng
Camera IP (ví dụ: camera an ninh Wi-Fi hoặc camera USB).
Cáp mạng (nếu sử dụng camera IP qua cổng mạng).
Máy tính để chạy ứng dụng an ninh.
⚠️ Lưu ý: Đảm bảo camera IP đã được cấu hình đúng để có thể kết nối với mạng nội bộ.
### 💻 Phần mềm
🐍 Python 3+ 
⚡ Thư viện OpenCV để xử lý hình ảnh từ camera.
### 📦 Các thư viện Python cần thiết
Cài đặt các thư viện bằng lệnh:
pip install flask opencv-contrib-python numpy pillow sqlite3

## 🧮 Hướng dẫn kết nối camera IP tới máy tính
### 🔌 Kết nối phần cứng:

# ⛓️‍💥 Hướng Dẫn Kết Nối

## 1️⃣ Cài Đặt Camera IP
- Kết nối camera IP vào nguồn điện và vào mạng Wi-Fi.  
- Sử dụng ứng dụng/phần mềm đi kèm để cấu hình SSID và mật khẩu Wi-Fi.  

## 2️⃣ Lấy Địa Chỉ IP Của Camera
- Sau khi cấu hình, kiểm tra địa chỉ IP của camera (ví dụ: `http://192.168.1.100`).  
- Đảm bảo có thể truy cập camera thông qua trình duyệt.  

## 3️⃣ Kết Nối Camera Tới Máy Tính
- Mở ứng dụng Python trên máy tính.  
- Dùng địa chỉ IP lấy được để thiết lập kết nối với Flask.  

## 4️⃣ Kiểm Tra Kết Nối Bằng OpenCV
Sử dụng đoạn code sau để kiểm tra kết nối:  

```python
import cv2

camera_ip = 'http://127.0.0.1:5000/detect'  # Thay bằng địa chỉ IP của camera
cap = cv2.VideoCapture(camera_ip)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Camera Feed', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

⚠ **Lưu ý:**  
- Đảm bảo firewall không chặn kết nối đến địa chỉ IP của camera.  
- Camera và máy tính phải cùng mạng để truy cập và xử lý hình ảnh hiệu quả.  

---

# 🚀 Hướng Dẫn Cài Đặt & Chạy

## 1️⃣ Chuẩn Bị Phần Mềm
- **Cài đặt Node.js**: Tải và cài đặt từ trang chính thức.  
- **Cài đặt Python 3**: Đảm bảo thêm Python vào PATH khi cài đặt.  
- **Cài đặt SQL Server**: Dùng để lưu trữ thông tin sinh viên và điểm danh.  

## 2️⃣ Cài Đặt Thư Viện Cho React
```bash
mkdir attendance-app
cd attendance-app
npx create-react-app .
npm install axios react-webcam
```

## 3️⃣ Cài Đặt Thư Viện Cho Flask
```bash
pip install flask flask-cors deepface mtcnn pyodbc opencv-python numpy
```

## 4️⃣ Cấu Hình Cơ Sở Dữ Liệu
- Tạo cơ sở dữ liệu `DiemdanhHS` trong SQL Server.  
- Đảm bảo bảng dữ liệu phù hợp với mô hình ứng dụng.  

## 5️⃣ Chạy Ứng Dụng Flask API
```bash
cd path/to/flask-app
python app.py
```
- Flask chạy trên `http://127.0.0.1:5000`.  

## 6️⃣ Chạy Ứng Dụng React
```bash
cd attendance-app
npm start
```
- Ứng dụng React chạy trên `http://localhost:3000`.  

## 7️⃣ Sử Dụng Ứng Dụng
- Truy cập `http://localhost:3000` trên trình duyệt.
- Hệ thống sẽ tự động điểm danh bằng camera.

---

# 📖 Hướng Dẫn Sử Dụng

## 1️⃣ Điểm Danh Tự Động Qua Camera
- Sinh viên sử dụng camera để chụp hình khuôn mặt.
- Hệ thống gửi dữ liệu đến server Flask để xử lý.
- Nếu nhận diện thành công, thông tin sẽ được lưu vào cơ sở dữ liệu.

## 2️⃣ Quản Lý Sinh Viên
- **Thêm/Sửa/Xóa** thông tin sinh viên.
- **Tìm kiếm** danh sách sinh viên theo tên/lớp.
- **Xem lịch sử** điểm danh.

## 3️⃣ Xem Lịch Sử Điểm Danh
- Hiển thị danh sách điểm danh gần đây.
- Tìm kiếm lịch sử điểm danh theo ngày.

---

# ⚙️ Cấu Hình & Ghi Chú

## Cấu Hình Cơ Sở Dữ Liệu
- Cập nhật chuỗi kết nối SQL Server trong Flask (`get_db_connection()`).
- Đảm bảo bảng `Users`, `Faces`, và `Attendance` tồn tại.

## Cấu Hình Camera
- Kiểm tra kết nối và cấp quyền truy cập camera.
- Có thể sử dụng webcam trên máy tính.

## Cài Đặt Thư Viện Cần Thiết
```bash
pip install flask deepface mtcnn pyodbc opencv-python
```

## Hỗ Trợ CORS
- Flask đã được cấu hình hỗ trợ CORS để React có thể gọi API.

## Môi Trường Mạng
- Các thiết bị điểm danh và server Flask cần nằm cùng mạng nội bộ.

## Xử Lý Thông Báo & Lỗi
- Theo dõi console của server để kiểm tra thông báo lỗi.

Với hướng dẫn này, bạn có thể sử dụng và cấu hình hệ thống điểm danh tự động dựa trên nhận diện khuôn mặt một cách hiệu quả. 🚀



