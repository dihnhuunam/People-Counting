import os
from ultralytics import YOLO

def test_model(
    model_path='best.pt', 
    source=None,  # Path to test images/video
    conf=0.25,   # Confidence threshold
    iou=0.45,    # IoU threshold
    project='runs/test',  # Directory to save results
    name='test_results',  # Results folder name
    exist_ok=True  # Allow overwriting existing results
):
    """
    Test the model on a specific dataset or source
    
    Args:
        model_path (str): Path to the model weights
        source (str, optional): Path to test images/video. 
                                If None, will use default source from model
        conf (float): Confidence threshold
        iou (float): IoU threshold
        project (str): Directory to save results
        name (str): Results folder name
        exist_ok (bool): Allow overwriting existing results
    """
    try:
        # Validate input paths
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model weights not found: {model_path}")
        
        # Check source path if provided
        if source and not os.path.exists(source):
            raise FileNotFoundError(f"Test source not found: {source}")
        
        # Load the model
        model = YOLO(model_path)
        
        # Perform prediction/testing
        results = model.predict(
            source=source,          # Test source (can be None)
            conf=conf,              # Confidence threshold
            iou=iou,                # IoU threshold
            project=project,        # Results directory
            name=name,              # Results folder name
            exist_ok=exist_ok,      # Allow overwriting
            save=True,              # Save prediction results
            save_txt=True,          # Save results as txt files
            save_conf=True,         # Save confidence scores
            save_json=True          # Save results in COCO JSON format
        )
        
        # Print testing summary
        print("\n--- Model Testing Results ---")
        print(f"Model: {model_path}")
        print(f"Test Source: {source or 'Default'}")
        
        # Print summary of predictions
        print("\nTesting Summary:")
        print(f"Total predictions: {len(results)}")
        
        # Analyze predictions if results exist
        if results:
            # Count detections by class
            class_counts = {}
            for result in results:
                if result.boxes is not None:
                    for box in result.boxes:
                        cls = int(box.cls[0])
                        class_counts[cls] = class_counts.get(cls, 0) + 1
            
            print("\nDetection Counts by Class:")
            for cls, count in class_counts.items():
                print(f"Class {cls}: {count} detections")
        
        return results
    
    except Exception as e:
        print(f"An error occurred during model testing: {e}")
        raise

def main():
    # Paths configuration
    MODEL_PATH = "best.pt"
    TEST_SOURCE = None  # Specify path to test images/video, or None for default
    
    # Run model testing
    test_model(
        model_path=MODEL_PATH, 
        source=TEST_SOURCE
    )

if __name__ == "__main__":
    main()