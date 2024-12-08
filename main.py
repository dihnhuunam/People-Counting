import cv2
import numpy as np
from ultralytics import YOLO

class PeopleDetector:
    def __init__(self, model_path='yolov8x.pt'):
        """
        Initialize the people detector with a YOLO model.

        Args:
            model_path (str, optional): Path to the YOLO model weights. Defaults to 'yolov8x.pt'.

        Raises:
            Exception: If there's an error loading the model.
        """
        try:
            self.model = YOLO(model_path)
            print(f"Model '{model_path}' loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")
            raise

    def analyze_crowd_density(self, people_detections, frame_shape):
        """
        Analyze crowd density based on the number and area of detected people.

        Args:
            people_detections (list): List of detected person bounding boxes.
            frame_shape (tuple): Dimensions of the input frame.

        Returns:
            tuple: A tuple containing density description and crowd ratio.
                   - First element: Density description (sparse, medium, crowded)
                   - Second element: Ratio of person area to total frame area
        """
        total_area = frame_shape[0] * frame_shape[1]
        person_area = sum((x2-x1) * (y2-y1) for x1,y1,x2,y2,_,_ in people_detections)
        crowd_ratio = person_area / total_area
        
        if crowd_ratio < 0.1:
            return "Sparse", crowd_ratio
        elif crowd_ratio < 0.3:
            return "Medium", crowd_ratio
        else:
            return "Crowded", crowd_ratio

    def detect_people(self, frame):
        """
        Detect people in a frame.

        Args:
            frame (numpy.ndarray): Input image frame.

        Returns:
            list: List of detected people with their bounding box coordinates and confidence
        """
        # Detect people specifically
        results = self.model(frame)
        
        people = []
        for det in results[0].boxes.data:
            x1, y1, x2, y2, conf, cls = det
            class_name = self.model.names[int(cls)]
            
            if class_name == 'person':
                people.append((x1, y1, x2, y2, conf, class_name))
        
        return people

    def process_webcam(self):
        """
        Process real-time people detection from webcam.

        Displays a window with people detection and crowd density analysis.
        Press 'q' to exit.
        """
        cap = cv2.VideoCapture(0)
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Detect people
            people = self.detect_people(frame)
            
            # Draw bounding boxes and statistics
            for x1, y1, x2, y2, conf, class_name in people:
                cv2.rectangle(
                    frame, 
                    (int(x1), int(y1)), 
                    (int(x2), int(y2)), 
                    (0, 255, 0), 
                    2
                )
                cv2.putText(
                    frame, 
                    f"Person: {conf:.2f}", 
                    (int(x1), int(y1)-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    0.5, 
                    (0, 255, 0), 
                    2
                )
            
            # Analyze crowd density
            if people:
                density, ratio = self.analyze_crowd_density(people, frame.shape)
                cv2.putText(
                    frame, 
                    f"Density: {density} ({ratio:.2%})", 
                    (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    1, 
                    (0, 0, 255), 
                    2
                )
            
            # Display people count
            cv2.putText(
                frame, 
                f"People Count: {len(people)}", 
                (10, frame.shape[0] - 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.7, 
                (255, 255, 255), 
                2
            )
            
            cv2.imshow('People Detection', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()

    def process_video(self, video_path):
        """
        Process people detection from a video file.

        Args:
            video_path (str): Path to the input video file.

        Displays a window with people detection and crowd density analysis.
        Press 'q' to exit.
        """
        cap = cv2.VideoCapture(video_path)
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Detect people
            people = self.detect_people(frame)
            
            # Draw bounding boxes and statistics
            for x1, y1, x2, y2, conf, class_name in people:
                cv2.rectangle(
                    frame, 
                    (int(x1), int(y1)), 
                    (int(x2), int(y2)), 
                    (0, 255, 0), 
                    2
                )
                cv2.putText(
                    frame, 
                    f"Person: {conf:.2f}", 
                    (int(x1), int(y1)-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    0.5, 
                    (0, 255, 0), 
                    2
                )
            
            # Analyze crowd density
            if people:
                density, ratio = self.analyze_crowd_density(people, frame.shape)
                cv2.putText(
                    frame, 
                    f"Density: {density} ({ratio:.2%})", 
                    (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    1, 
                    (0, 0, 255), 
                    2
                )
            
            # Display people count
            cv2.putText(
                frame, 
                f"People Count: {len(people)}", 
                (10, frame.shape[0] - 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.7, 
                (255, 255, 255), 
                2
            )
            
            cv2.imshow('People Detection', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()

def main():
    """
    Main function to run the people detection application.

    Provides a menu to choose between webcam and video file processing.
    """
    print("Select Mode:")
    print("1. Webcam Realtime")
    print("2. Video Analysis")
    
    choice = input("Enter choice (1/2): ").strip()
    
    detector = PeopleDetector()
    
    if choice == '1':
        detector.process_webcam()
    elif choice == '2':
        video_path = input("Enter video path: ").strip()
        detector.process_video(video_path)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()