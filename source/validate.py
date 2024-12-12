import os
from ultralytics import YOLO

def validate_model(
    model_path='best.pt', 
    data_path='dataset/data.yaml', 
    conf=0.001,  # Low confidence threshold for comprehensive evaluation
    iou=0.45,   # IoU threshold
    project='runs/val',  # Directory to save results
    name='validation_results',  # Results folder name
    exist_ok=True  # Allow overwriting existing results
):
    """
    Validate the model on the validation dataset
    
    Args:
        model_path (str): Path to the model weights
        data_path (str): Path to the dataset configuration file
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
        
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Dataset configuration not found: {data_path}")
        
        # Load the model
        model = YOLO(model_path)
        
        # Perform validation
        results = model.val(
            data=data_path,        # Path to data.yaml
            conf=conf,             # Confidence threshold
            iou=iou,               # IoU threshold
            project=project,       # Results directory
            name=name,             # Results folder name
            exist_ok=exist_ok,     # Allow overwriting
            save_json=True,        # Save results in COCO JSON format
            plots=True             # Generate visualization plots
        )
        
        # Print detailed results
        print("\n--- Model Validation Results ---")
        print(f"Model: {model_path}")
        print(f"Dataset: {data_path}")
        
        # Print key metrics
        print("\nEvaluation Metrics:")
        metrics_dict = results.results_dict
        metrics = [
            ('Precision', 'metrics/precision'),
            ('Recall', 'metrics/recall'),
            ('mAP50', 'metrics/mAP50'),
            ('mAP50-95', 'metrics/mAP50-95')
        ]
        
        for metric_name, metric_key in metrics:
            print(f"{metric_name}: {metrics_dict.get(metric_key, 'Not available')}")
        
        return results
    
    except Exception as e:
        print(f"An error occurred during model validation: {e}")
        raise

def main():
    # Paths configuration
    MODEL_PATH = "best.pt"
    DATA_PATH = "dataset/data.yaml"
    
    # Run model validation
    validate_model(
        model_path=MODEL_PATH, 
        data_path=DATA_PATH
    )

if __name__ == "__main__":
    main()