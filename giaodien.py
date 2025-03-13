import tkinter as tk
from tkinter import ttk
import numpy as np
import os
import pickle, sqlite3
import cv2
from PIL import Image

def nhandien():
    face_cascade = cv2.CascadeClassifier('khuonMat.xml')
    #recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    #recognizer.read("huanluyen/huanluyen.yml")
    recognizer.read("trainer/face-trainner.yml")

    def getProfile(Id):
        conn=sqlite3.connect("FaceBase.db")
        query="SELECT * FROM People WHERE ID="+str(Id)
        cursor=conn.execute(query)
        profile=None
        for row in cursor:
            profile=row
        conn.close()
        return profile

    #cap = cv2.VideoCapture("rtsp://admin:admin@172.16.1.45:554/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif")
    # Địa chỉ IP Camera

    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_COMPLEX
    while True:
        #comment the next line and make sure the image being read is names img when using imread
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            nbr_predicted, conf = recognizer.predict(gray[y:y+h, x:x+w])
            if conf < 70:   
                profile=getProfile(nbr_predicted)
                if profile != None:
                    cv2.putText(img, ""+str(profile[1]), (x+10, y), font, 1, (0,255,0), 1);
            else:
                cv2.putText(img, "Unknown", (x, y + h + 30), font, 0.4, (0, 255, 0), 1);


        cv2.imshow('img', img)
        if(cv2.waitKey(1) == ord('q')):
            break
    cap.release()
    cv2.destroyAllWindows()

def train():
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    path = 'data_face'

    def getImagesWithID(path):
        imagePaths=[os.path.join(path, f) for f in os.listdir(path)]
        faces=[]
        IDs=[]
        for imagePath in imagePaths:
            faceImg = Image.open(imagePath).convert('L')
            faceNp = np.array(faceImg, 'uint8')
            ID=int(os.path.split(imagePath)[-1].split('.')[1])
            faces.append(faceNp)
            IDs.append(ID)
            cv2.imshow('training', faceNp)
            cv2.waitKey(10)
        return np.array(IDs), faces

    Ids, faces = getImagesWithID(path)
    recognizer.train(faces, Ids)

    if not os.path.exists('trainer'):
        os.makedirs('trainer')

    recognizer.save("trainer/face-trainner.yml")
    cv2.destroyAllWindows()

def laydulieu():
    def insertOrUpdate(id, name):
    #connecting to the db
        conn =sqlite3.connect("FaceBase.db")	
        #check if id already exists
        query = "SELECT * FROM People WHERE ID="+str(id)
        #returning the data in rows
        cursor = conn.execute(query)
        isRecordExist=0
        for row in cursor:
            isRecordExist=1
        if isRecordExist==1:
            query="UPDATE People SET Name="+str(name)+" WHERE ID="+str(id)
        else:
            query="INSERT INTO People(ID, Name) VALUES("+str(id)+","+str(name)+")"
        conn.execute(query)
        conn.commit()
        conn.close()


    face_cascade = cv2.CascadeClassifier('khuonMat.xml')
    cap = cv2.VideoCapture(0)

    #id = input('Enter user id: ')
    #name = input('Enter name: ')
    id = int1.get()
    name ="'"+str1.get()+"'"
    insertOrUpdate(id, name)
    sample_number = 0
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            sample_number += 1

            if not os.path.exists('data_face'):
                os.makedirs('data_face')

            cv2.imwrite('data_face/User.'+str(id)+"."+str(sample_number)+".jpg",  img[y:y+h,x:x+w])
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

        cv2.imshow('img', img)
        cv2.waitKey(1);
        if(sample_number>100):
            cap.release()
            cv2.destroyAllWindows()
            break;
    edit_id.delete(0,"end")
    edit_name.delete(0,"end")
    

win = tk.Tk()

win.title("He thong canh bao dot nhap")
win.geometry('500x300')
win.configure(bg='#1E1E1E') 
label = ttk.Label(win, text="Hệ Thống Cảnh Báo Đột Nhập", font=("Arial", 16, "bold"), background="#1E1E1E", foreground="#FFD700")

label.grid(column =1, row =0)
label.place(x=100)


label1 = ttk.Label(  text="ID:", font=("Arial", 12), background="#1E1E1E", foreground="white")
label1.grid(column =0, row =2)
label1.place(y=80)

label2 = ttk.Label(  text="Name:", font=("Arial", 12), background="#1E1E1E", foreground="white")
label2.grid(column =0, row =3)
label2.place(y=120)

int1 =tk.IntVar()
edit_id=ttk.Entry(win,textvariable=int1, width=50)
edit_id.grid(column =1, row =2)
edit_id.focus()
edit_id.place(x=90,y=80)
str1 =tk.StringVar()
edit_name=ttk.Entry(win,textvariable=str1,width=50)
edit_name.grid(column =1, row =3)
edit_name.place(x=90,y=120)

btlaydulieu= ttk.Button(win, text ="Lấy Dữ Liệu", command=laydulieu)

btlaydulieu.grid(column =0, row =4)
#btlaydulieu.place()


bttrain= ttk.Button(win, text ="Training", command=train)
bttrain.grid(column =1, row =4)

btnhandien= ttk.Button(win, text ="Nhận Diện", command=nhandien)
btnhandien.grid(column =2, row =4)  
bttrain.place(x=200,y=200)
btnhandien.place(x=350,y=200)
btlaydulieu.place(x=50,y=200)


win.mainloop()

