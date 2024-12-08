import cv2
import numpy as np
from ultralytics import YOLO  # Thư viện YOLOv8

# Load the YOLO model
def load_model(model_path='yolov8s.pt'):
    try:
        # Tải model YOLO
        model = YOLO(model_path)  # Đảm bảo bạn đã cài ultralytics
        print(f"Model '{model_path}' loaded successfully.")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        exit(1)

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
        return model
    except Exception as e:
        print(f"Error during training: {e}")
        exit(1)

# Process a single image
def process_image(image_path, model):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to read the image.")
        return

    # Object detection
    results = model(image)
    person_detections = [det for det in results[0].boxes.data if int(det[5]) == 0]
    people_count = len(person_detections)

    # Draw bounding boxes
    for det in person_detections:
        x1, y1, x2, y2, conf, cls = det
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

    cv2.putText(image, f"People Count: {people_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('People Counting - Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Process a video
def process_video(video_path, model):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open video source.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video stream or cannot fetch the frame.")
            break

        # Object detection
        results = model(frame)
        person_detections = [det for det in results[0].boxes.data if int(det[5]) == 0]
        people_count = len(person_detections)

        # Draw bounding boxes
        for det in person_detections:
            x1, y1, x2, y2, conf, cls = det
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

        cv2.putText(frame, f"People Count: {people_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('People Counting - Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    action = input("Enter action (train/image/video): ").strip().lower()

    if action == "train":
        print("Starting training...")
        train_model()
    elif action == "image":
        model_path = input("Enter the trained model path (default: 'yolov8s.pt'): ").strip() or 'yolov8s.pt'
        model = load_model(model_path)
        file_path = input("Enter the path to the image: ").strip()
        process_image(file_path, model)
    elif action == "video":
        model_path = input("Enter the trained model path (default: 'yolov8s.pt'): ").strip() or 'yolov8s.pt'
        model = load_model(model_path)
        file_path = input("Enter the path to the video: ").strip()
        process_video(file_path, model)
    else:
        print("Invalid action. Please enter 'train', 'image', or 'video'.")
