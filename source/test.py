import os
import random
import matplotlib.pyplot as plt
import cv2
from ultralytics import YOLO

def test_model(
    model_path='best.pt', 
    source=None,
    conf=0.25,
    iou=0.45,
    project='runs/test',
    name='test_results',
    exist_ok=True
):
    # Load the model
    model = YOLO(model_path)
    
    # Perform prediction/testing
    results = model.predict(
        source=source,
        conf=conf,
        iou=iou,
        project=project,
        name=name,
        exist_ok=exist_ok,
        save=True,
        save_txt=True,
        save_conf=True,
        save_json=True
    )
    
    return results

def count_people(result):
    """Count number of people detections in a result"""
    if result.boxes is None:
        return 0
    
    # Assuming class 0 is person
    person_masks = result.boxes.cls == 0
    return int(person_masks.sum())

def test_random_images():
    # Path to test images directory
    test_images_dir = '../test/images'
    results_file = 'test_results.txt'
    output_image_path = 'detection_results_with_count.png'
    
    try:
        # Get list of all image files
        image_files = [f for f in os.listdir(test_images_dir) 
                      if f.endswith(('.jpg', '.jpeg', '.png'))]
        
        if len(image_files) < 4:
            raise ValueError("Not enough images in the test directory")
        
        # Randomly select 4 images
        selected_images = random.sample(image_files, 4)
        
        # Create figure with 2x2 subplots
        fig, axes = plt.subplots(2, 2, figsize=(19.2, 10.8))  # Full HD display
        fig.suptitle('Random Test Images Detection Results', fontsize=20)
        
        # Open file to save results
        with open(results_file, 'w') as f:
            f.write("Image Detection Results:\n")
            f.write("-----------------------\n")
            
            # Process and display each image
            for idx, image_file in enumerate(selected_images):
                # Full path to image
                image_path = os.path.join(test_images_dir, image_file)
                print(f"\nProcessing image {idx + 1}: {image_file}")
                
                # Run model prediction
                results = test_model(source=image_path)
                
                # Get the result image (assumes first result)
                if results and len(results) > 0:
                    # Count people in the image
                    people_count = count_people(results[0])
                    
                    # Save result to file
                    f.write(f"\nImage {idx + 1}: {image_file}\n")
                    f.write(f"Number of people detected: {people_count}\n")
                    
                    # Convert result image to numpy array
                    result_image = results[0].plot()
                    result_image = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)
                    
                    # Plot in appropriate subplot
                    row = idx // 2
                    col = idx % 2
                    axes[row, col].imshow(result_image)
                    axes[row, col].set_title(f'Image {idx + 1}: {image_file}\nPeople Count: {people_count}', fontsize=12)
                    axes[row, col].axis('off')
        
        # Adjust layout and display
        plt.tight_layout()
        plt.savefig(output_image_path)  # Save the figure
        plt.show()
        
        print(f"\nResults have been saved to {results_file}")
        print(f"Detection result image saved to {output_image_path}")
        
    except FileNotFoundError as fnf_error:
        print(f"File error: {fnf_error}")
    except ValueError as val_error:
        print(f"Value error: {val_error}")
    except KeyboardInterrupt:
        print("\nOperation canceled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    test_random_images()
