from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from math import ceil, sqrt # Để tính toán số lượng hàng/cột cho subplots

# 3. Tải mô hình YOLO đã huấn luyện (phiên bản lớn hơn để tăng độ chính xác)
model = YOLO('yolov8m.pt')  # Sử dụng yolov8m để cân bằng giữa tốc độ và độ chính xác

def nhan_dien_anh(image_path, confidence_threshold=0.6, ax=None):
    """
    Hàm nhận diện động vật trên một ảnh và vẽ kết quả lên một subplot cụ thể.
    ax: Đối tượng Axes của Matplotlib để vẽ lên (nếu None, sẽ in ra console).
    """
    try:
        # Đọc ảnh bằng OpenCV
        img = cv2.imread(image_path)
        if img is None:
            print(f"Lỗi: Không thể đọc ảnh từ đường dẫn: {image_path}")
            return None # Trả về None nếu không đọc được ảnh

        # Thực hiện nhận diện đối tượng với ngưỡng độ tin cậy
        results = model.predict(img, conf=confidence_threshold, verbose=False)

        # Lấy ảnh đã được vẽ bounding box
        annotated_img = results[0].plot(conf=True)
        annotated_img_rgb = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)

        # In thông tin chi tiết về các đối tượng được nhận diện (chỉ khi độ tin cậy vượt ngưỡng)
        print(f"\n--- Kết quả nhận diện cho ảnh: {os.path.basename(image_path)} ---")
        found_objects = False
        for result in results:
            boxes = result.boxes
            for box in boxes:
                confidence = box.conf[0].cpu().numpy()
                if confidence >= confidence_threshold:
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
                    cls = int(box.cls[0].cpu().numpy())
                    class_name = model.names[cls]
                    print(f"Đã nhận diện: {class_name} tại ({x1}, {y1}), ({x2}, {y2}) với độ tin cậy {confidence:.2f}")
                    found_objects = True
        if not found_objects:
            print("Không tìm thấy đối tượng nào vượt ngưỡng độ tin cậy.")


        # Vẽ lên subplot nếu ax được cung cấp
        if ax:
            ax.imshow(annotated_img_rgb)
            ax.set_title(f"{os.path.basename(image_path)}\n({confidence_threshold:.2f})")
            ax.axis('off')
            return True # Trả về True nếu vẽ thành công
        return None # Trả về None nếu không vẽ lên subplot

    except Exception as e:
        print(f"Lỗi khi xử lý ảnh {image_path}: {e}")
        return None

def select_and_process_images_in_one_tab():
    """Hàm cho phép người dùng chọn nhiều ảnh và hiển thị tất cả kết quả trên cùng một Matplotlib tab."""
    root = tk.Tk()
    root.withdraw() # Ẩn cửa sổ Tkinter chính

    while True:
        print("\nHãy chọn các ảnh bạn muốn nhận diện (hoặc đóng hộp thoại để dừng):")
        file_paths = filedialog.askopenfilenames(
            title="Chọn ảnh để nhận diện động vật",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
        )

        if not file_paths:
            print("Không có ảnh nào được chọn. Đã dừng quá trình xử lý.")
            break

        num_images = len(file_paths)
        if num_images == 0:
            print("Không có ảnh nào được chọn.")
            continue

        # Tính toán kích thước lưới cho subplots
        # Tìm số hàng và cột sao cho gần vuông nhất
        rows = ceil(sqrt(num_images))
        cols = ceil(num_images / rows) # Đảm bảo đủ cột cho tất cả ảnh

        plt.figure(figsize=(cols * 6, rows * 6)) # Kích thước figure lớn hơn để mỗi subplot đủ rộng
        plt.suptitle("Kết quả Nhận diện Đối tượng trên Nhiều Ảnh", fontsize=16, y=1.02) # Tiêu đề chung

        for i, image_path in enumerate(file_paths):
            print(f"Đang xử lý ảnh: {image_path}")
            ax = plt.subplot(rows, cols, i + 1) # Tạo subplot thứ i+1
            nhan_dien_anh(image_path, confidence_threshold=0.5, ax=ax) # Truyền ax vào hàm nhận diện

        plt.tight_layout(rect=[0, 0.03, 1, 0.98]) # Điều chỉnh layout để tránh chồng chéo tiêu đề
        plt.show() # Hiển thị tất cả subplots trong một cửa sổ

# --- Chạy chức năng tải lên và xử lý nhiều ảnh trên cùng một tab ---
select_and_process_images_in_one_tab()

# --- Chức năng nhận diện video (giữ nguyên để bạn tham khảo nếu cần) ---
# ... (Phần code này không thay đổi) ...
def nhan_dien_video(video_path='your_video.mp4', confidence_threshold=0.5):
    """Hàm nhận diện động vật trên một video."""
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Không thể mở video tại: {video_path}")
        return

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        results = model.predict(frame, conf=confidence_threshold, verbose=False)
        annotated_frame = results[0].plot(conf=True)
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()