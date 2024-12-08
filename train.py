import numpy as np
from ultralytics import YOLO  # Thư viện YOLOv8

# Train the YOLO model with ShanghaiTech dataset
def train_model():
    try:
        # Đường dẫn cấu hình dataset
        dataset_config = 'shanghaitech.yaml'  # Tệp cấu hình dữ liệu YOLO
        
        # Tải model YOLO
        model = YOLO('yolov8s.pt')  # Sử dụng trọng số pre-trained

        # Huấn luyện model
        model.train(
            data=dataset_config,
            epochs=50,           # Số epoch
            batch=16,            # Kích thước batch
            imgsz=640,           # Kích thước ảnh đầu vào
            device=0,            # Sử dụng GPU (0: GPU đầu tiên)
            name='yolov8s_shanghaitech',  # Tên phiên huấn luyện
            verbose=True
        )
        print("Training completed.")
    except Exception as e:
        print(f"Error during training: {e}")
        exit(1)

if __name__ == "__main__":
    print("Starting training...")
    train_model()