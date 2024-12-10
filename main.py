# main.py
from detectors.image_processor import ImageProcessor
from detectors.video_processor import VideoProcessor
from detectors.realtime_processor import RealtimeProcessor

def main():
    print("Choose an option:")
    print("1. Process Image")
    print("2. Process Video")
    print("3. Realtime Detection (Webcam)")
    choice = input("Enter your choice: ")

    if choice == '1':
        image_path = input("Enter image path: ")
        processor = ImageProcessor()
        processor.process_image(image_path)
    elif choice == '2':
        video_path = input("Enter video path: ")
        processor = VideoProcessor()
        processor.process_video(video_path)
    elif choice == '3':
        processor = RealtimeProcessor()
        processor.process_webcam()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
