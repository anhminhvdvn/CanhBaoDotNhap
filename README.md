# ỨNG DỤNG CÔNG NGHỆ TRONG HỆ THỐNG QUẢN LÝ VÀ ĐIỂM DANH SINH VIÊN

![DaiNam University Logo](https://dainam.edu.vn/wp-content/uploads/2020/01/logo-dainam.png)
![AIoTLab Logo](https://www.aiotlab.vn/wp-content/uploads/2020/01/logo-aiotlab.png)

[![Made by AIoTLab](https://img.shields.io/badge/Made%20by%20AIoTLab-blue?style=for-the-badge)](https://www.facebook.com/DNUAIoTLab)
[![Fit DNU](https://img.shields.io/badge/Fit%20DNU-green?style=for-the-badge)](https://fitdnu.net/)
[![DaiNam University](https://img.shields.io/badge/DaiNam%20University-red?style=for-the-badge)](https://dainam.edu.vn)

## Giới thiệu

Hệ thống quản lý và điểm danh sinh viên sử dụng công nghệ nhận diện khuôn mặt và cơ sở dữ liệu SQL Server. Ứng dụng này cho phép giảng viên dễ dàng quản lý thông tin sinh viên, thực hiện điểm danh tự động và theo dõi lịch sử điểm danh qua giao diện người dùng thân thiện.

---

## Tính năng chính

- **Điểm danh tự động:** Hệ thống sử dụng camera để quét khuôn mặt sinh viên và tự động điểm danh khi khuôn mặt được nhận diện. Hệ thống cho phép điểm danh ngay khi sinh viên ngồi trong lớp học.
- **Thông báo trực quan:** Khi sinh viên được điểm danh, hệ thống sẽ hiển thị thông báo trên giao diện người dùng. Nếu có trường hợp không nhận diện được khuôn mặt, thông báo lỗi sẽ được hiển thị.
- **Quản lý dữ liệu:** Dữ liệu điểm danh và thông tin sinh viên được lưu trữ trong SQL Server. Hệ thống cho phép xem danh sách sinh viên, danh sách lớp học, và lịch sử điểm danh.
- **Giao diện thân thiện:** Sử dụng React cho giao diện người dùng với webcam để quét khuôn mặt, và Flask cho backend xử lý điểm danh cũng như lưu dữ liệu. Giao diện người dùng được thiết kế đơn giản và dễ sử dụng.
- **Phát hiện khuôn mặt:** Sử dụng thư viện MTCNN để phát hiện khuôn mặt và DeepFace để xác thực các khuôn mặt so với cơ sở dữ liệu đã lưu trữ.
- **Cải thiện hình ảnh:** Hệ thống cải thiện chất lượng hình ảnh trước khi xác thực bằng các kỹ thuật như tăng độ nét và điều chỉnh độ sáng.

---

## Hệ thống

![System Architecture](https://github.com/DuccHuyyy/Diem_Danh_Sinh_Vien_Bang_Guong_Mat_FaceNet/raw/main/system_architecture.png)

---

## Cấu trúc dự án
BTL_IOT
├── 📂 face-recognition-attendance   # Hệ thống điểm danh dựa trên nhận diện khuôn mặt
│   ├── 📂 backend                   # Backend xử lý dữ liệu và logic
│   │   ├── 📂 dataset               # Dữ liệu khuôn mặt của sinh viên
│   │   │   ├── 📂 CNTT_16-05/       # Dữ liệu sinh viên CNTT - lớp 16-05
│   │   │   ├── 📂 HAN_16-03/        # Dữ liệu sinh viên HAN - lớp 16-03
│   │   ├── 📂 sound                 # Âm thanh thông báo điểm danh
│   │   ├── 📄 app.py                # API backend chính
│   │   ├── 🖼️ temp.jpg              # Ảnh tạm lưu trong quá trình nhận diện
│   ├── 📂 frontend                  # Giao diện người dùng (React)
│   │   ├── 📂 node_modules           # Thư viện phụ thuộc cho frontend
│   │   ├── 📂 public                 # Tệp tĩnh của ứng dụng
│   │   ├── 📂 src                    # Mã nguồn frontend
│   │   │   ├── 📂 components         # Các component của React
│   │   │   │   ├── 📄 DsDiemDanh.js  # Component hiển thị danh sách điểm danh
│   │   │   │   ├── 📄 StudentList.js # Component hiển thị danh sách sinh viên
│   │   │   │   ├── 📄 CameraComponent.js # Component xử lý camera
│   │   │   │   ├── 📄 ManageStudents.js  # Component quản lý sinh viên
│   │   │   ├── 📄 App.js             # Component chính của ứng dụng
│   │   │   ├── 📄 index.js           # Điểm vào chính của ứng dụng React
│   │   │   ├── 📄 setupTests.js      # Cấu hình kiểm thử
│   ├── 📄 package.json               # Thông tin về các dependencies của frontend
│   ├── 📄 package-lock.json          # Tệp khóa phiên bản cho các dependencies
├── 📂 venv                            # Môi trường ảo Python
├── 📄 package.json                    # Thông tin về các dependencies chung


## Công nghệ sử dụng

### Phần cứng

[![CameraIP](https://img.shields.io/badge/Webcam-000000?style=for-the-badge)](https://www.logitech.com/en-us/products/webcams)
[![MTCNN](https://img.shields.io/badge/MTCNN-00979D?style=for-the-badge)](https://github.com/ipazc/mtcnn)
[![DeepFace](https://img.shields.io/badge/DeepFace-FF5722?style=for-the-badge)](https://github.com/serengil/deepface)

### Phần mềm

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)]()
[![Flask](https://img.shields.io/badge/Flask-v2.0.1-black?style=for-the-badge&logo=flask)]()
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-blue?style=for-the-badge)]()
[![pyodbc](https://img.shields.io/badge/pyodbc-4.x-green?style=for-the-badge&logo=python)]()
[![React](https://img.shields.io/badge/React-17.0.
::contentReference[oaicite:0]{index=0}
