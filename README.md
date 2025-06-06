# 🦁 Nhận diện 20 Loài Động Vật bằng YOLOv8 🐾

Dự án này sử dụng mô hình YOLOv8 để nhận diện và phân loại 20 loài động vật khác nhau trong ảnh và video. Đây là một ứng dụng thực tế của công nghệ Thị giác máy tính (Computer Vision) và Học sâu (Deep Learning) trong lĩnh vực giám sát động vật hoang dã, nghiên cứu sinh thái hoặc các hệ thống an ninh.

## 🌟 Tính năng Chính

* **Nhận diện đa dạng loài:** Có khả năng nhận diện 20 loại động vật phổ biến.
* **Hỗ trợ ảnh và video:** Xử lý cả ảnh tĩnh và luồng video trực tiếp/đã ghi.
* **Hiển thị trực quan:** Vẽ bounding box và hiển thị tên loài, độ tin cậy trên đối tượng được nhận diện.
* **Dễ sử dụng:** Cung cấp giao diện lựa chọn file thân thiện với người dùng (qua Tkinter).
* **Tích hợp Matplotlib:** Hiển thị kết quả nhận diện của nhiều ảnh trên cùng một cửa sổ để dễ dàng so sánh và quản lý.

## 🛠️ Công nghệ Sử dụng

* **YOLOv8:** Mô hình phát hiện đối tượng hàng đầu của Ultralytics, được biết đến với tốc độ và độ chính xác cao.
* **Python 3.x:** Ngôn ngữ lập trình chính.
* **OpenCV (cv2):** Thư viện xử lý ảnh và video mạnh mẽ.
* **Matplotlib:** Để hiển thị kết quả trực quan.
* **Tkinter:** Để tạo hộp thoại chọn file trên môi trường desktop.
* **NumPy:** Thư viện hỗ trợ tính toán số học hiệu quả.

## 🚀 Cài đặt và Chạy

### Yêu cầu hệ thống

* Python 3.7+ (Khuyến nghị Python 3.9 trở lên)
* Git (Để clone repository)
* VS Code (Khuyến nghị cho môi trường phát triển)

### Các bước cài đặt

1.  **Clone Repository:**
    Mở Terminal/Command Prompt/Git Bash và chạy lệnh sau để tải dự án về máy của bạn:
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    # Thay 'your-username' bằng tên người dùng GitHub của bạn
    # Thay 'your-repo-name' bằng tên repository của bạn (ví dụ: Animal_Detection_YOLOv8)
    ```
    Sau đó, điều hướng vào thư mục dự án:
    ```bash
    cd your-repo-name
    ```

2.  **Tạo và Kích hoạt Môi trường Ảo (Khuyến nghị):**
    ```bash
    python -m venv venv
    # Kích hoạt môi trường ảo:
    # Windows (PowerShell): .\venv\Scripts\Activate.ps1
    # Windows (Command Prompt): .\venv\Scripts\activate.bat
    # macOS/Linux: source venv/bin/activate
    ```

3.  **Cài đặt các Thư viện cần thiết:**
    Đảm bảo môi trường ảo của bạn đang kích hoạt, sau đó chạy:
    ```bash
    pip install ultralytics opencv-python matplotlib Pillow
    ```
    * `ultralytics`: Cung cấp YOLOv8.
    * `opencv-python`: Để đọc và xử lý ảnh/video.
    * `matplotlib`: Để hiển thị kết quả.
    * `Pillow`: Thư viện xử lý ảnh, đôi khi cần cho Tkinter và các thao tác ảnh khác.

### Cách chạy chương trình

1.  **Mở dự án trong Visual Studio Code:**
    * Mở VS Code.
    * Chọn `File > Open Folder...` và điều hướng đến thư mục dự án của bạn.
    * Trong VS Code, mở Terminal (Ctrl+Shift+` hoặc `Terminal > New Terminal`). Đảm bảo môi trường ảo đã được kích hoạt.

2.  **Chạy script nhận diện ảnh:**
    ```bash
    python xulyanh.py
    ```
    * Một hộp thoại sẽ xuất hiện, cho phép bạn chọn một hoặc nhiều file ảnh.
    * Sau khi chọn ảnh, chương trình sẽ xử lý và hiển thị tất cả các kết quả nhận diện (ảnh với bounding box và thông tin) trong **cùng một cửa sổ Matplotlib**.
    * Thông tin chi tiết về các đối tượng được nhận diện cũng sẽ được in ra trong Terminal.
    * Để dừng chương trình, chỉ cần đóng hộp thoại chọn file.

3.  **Chạy script nhận diện video (tùy chọn):**
    Đoạn code nhận diện video được comment trong `xulyanh.py`. Để sử dụng:
    * Mở file `xulyanh.py`.
    * Bỏ comment (xóa `#`) ở đoạn code liên quan đến hàm `nhan_dien_video` và phần gọi hàm đó ở cuối file.
    * Chạy lại `python xulyanh.py`. Một hộp thoại chọn file video sẽ xuất hiện.

## 📊 💡Kết quả

![xử lý ảnh 5](https://github.com/user-attachments/assets/1ef41a6b-acf2-4611-9a7d-a24fa2eb3add)

![xử lý ảnh 8](https://github.com/user-attachments/assets/28fa8d21-a12c-4cdc-9a78-358bcfbf4000)
## 🤝 Đóng góp

Mọi đóng góp để cải thiện dự án đều được hoan nghênh! Hãy mở một `issue` để báo cáo lỗi hoặc đề xuất tính năng, hoặc tạo `pull request` với những cải tiến của bạn.

## 📄 Giấy phép

Dự án này được cấp phép theo Giấy phép MIT. Xem file [LICENSE](LICENSE) để biết thêm chi tiết.

## 📧 Liên hệ

Nếu có bất kỳ câu hỏi nào, vui lòng liên hệ:

* **Tên của bạn:** [Phạm Duy Đức]
* **Email:** [duc23062003@gmail.com]
* **GitHub:** [https://github.com/your-username](https://github.com/your-username)
