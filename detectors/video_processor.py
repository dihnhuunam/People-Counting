# detectors/video_processor.py
import cv2
from .base_processor import BaseProcessor
from .analyzer import Analyzer

class VideoProcessor(BaseProcessor):
    def process_video(self, video_path):
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print(f"Error: Unable to open video file {video_path}")
            return

        _, initial_frame = cap.read()
        analyzer = Analyzer(initial_frame.shape[1], initial_frame.shape[0])

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            people = self.detect_people(frame)
            for x1, y1, x2, y2, conf, _ in people:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, f"Person: {conf:.2f}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            analyzer.display_analysis(frame, people)
            cv2.imshow('Video Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
