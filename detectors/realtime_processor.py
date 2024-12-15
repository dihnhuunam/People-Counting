# detectors/realtime_processor.py
import cv2
from .base_processor import BaseProcessor
from .analyzer import Analyzer

class RealtimeProcessor(BaseProcessor):
    def process_webcam(self):
        """
        @brief Process real-time video stream from the default webcam
        
        Captures video from the default camera, detects people, draws bounding boxes,
        and displays real-time density analysis. Exits when 'q' is pressed.
        """
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Unable to access the webcam.")
            return

        _, initial_frame = cap.read()
        analyzer = Analyzer(initial_frame.shape[1], initial_frame.shape[0])

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            people = self.detect_people(frame)
            for x1, y1, x2, y2, conf, class_name in people:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, f"{class_name.capitalize()}: {conf:.2f}", (int(x1), int(y1) - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            analyzer.display_analysis(frame, people)
            cv2.imshow('Realtime Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()