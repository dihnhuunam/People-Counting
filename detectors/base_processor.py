# detectors/base_processor.py
from ultralytics import YOLO

class BaseProcessor:
    def __init__(self, model_path='yolov8x.pt'):
        """
        BaseProcessor to load YOLOv8 model and provide detection functionality.
        """
        self.model = YOLO(model_path)

    def detect_people(self, frame):
        """
        Detect people in a frame.

        Args:
            frame (numpy.ndarray): Input image/frame.

        Returns:
            list: Detected people as [(x1, y1, x2, y2, conf, class_name)].
        """
        results = self.model(frame)
        people = []
        for r in results[0].boxes.data.tolist():
            x1, y1, x2, y2, conf, cls = r
            class_name = self.model.names[int(cls)]
            if class_name == 'person':
                people.append((x1, y1, x2, y2, conf, class_name))
        return people
