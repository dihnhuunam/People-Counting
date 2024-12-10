# detectors/image_processor.py
import cv2
from .base_processor import BaseProcessor
from .analyzer import Analyzer

class ImageProcessor(BaseProcessor):
    def process_image(self, image_path):
        frame = cv2.imread(image_path)
        if frame is None:
            print(f"Error: Unable to load image from {image_path}")
            return

        analyzer = Analyzer(frame.shape[1], frame.shape[0])
        people = self.detect_people(frame)

        for x1, y1, x2, y2, conf, _ in people:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, f"Person: {conf:.2f}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        analyzer.display_analysis(frame, people)
        cv2.imshow('Image Detection', frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
