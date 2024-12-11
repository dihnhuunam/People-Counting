# detectors/base_processor.py
from ultralytics import YOLO

class BaseProcessor:
    def __init__(self, model_path='yolov8n.pt'):
        """
        @brief Initialize the BaseProcessor with a YOLOv8 model
        
        @param model_path (str, optional): Path to the YOLOv8 model weights. Defaults to 'yolov8n.pt'
        """
        self.model = YOLO(model_path)

    def detect_people(self, frame):
        """
        @brief Detect people in a given frame using the YOLO model
        
        @param frame (numpy.ndarray): Input image or video frame to detect people in
        @return list: A list of detected people with their bounding box coordinates, confidence, and class name
                      Each entry is in the format: (x1, y1, x2, y2, confidence, class_name)
        """
        results = self.model(frame)
        people = []
        for r in results[0].boxes.data.tolist():
            x1, y1, x2, y2, conf, cls = r
            class_name = self.model.names[int(cls)]
            if class_name == 'person':
                people.append((x1, y1, x2, y2, conf, class_name))
        return people