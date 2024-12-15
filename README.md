# People Detection and Density Analysis Application

## Overview

This application uses a YOLOv8 model to detect people in images, videos, or real-time camera feeds. It analyzes crowd density based on bounding box areas and provides visual feedback, such as the total number of people detected and density classification (Sparse, Medium, or Crowded).

## Features

1. **Modular Design**:
   - Separate classes for processing images, videos, and real-time camera feeds for better scalability.
2. **People Detection**:
   - Detect people using model YOLOv8n extra trained with **crowd counting dataset** and draw bounding boxes with confidence scores.
3. **Crowd Density Analysis**:
   - Calculate and display the density percentage.
   - Classify density as **Sparse**, **Medium**, or **Crowded** with color-coded labels.
4. **Flexible Input Options**:
   - Process images, videos, or real-time camera feeds.
5. **Extensible Architecture**:
   - Easily extend functionality to detect other objects or analyze additional metrics.

## Installation

### Prerequisites

- Python 3.8+
- Install the following dependencies:

  ```bash
  pip install -r requirements.txt
  ```

## Files Structure

The application is organized as follows:

```
├── detectors
│   ├── image_processor.py       
│   ├── video_processor.py       
│   ├── realtime_processor.py   
│   └── analyzer.py               
├── source
│   ├── validate.py              
│   ├── test.py                  
│   └── main.py                 
├── best.pt                      
├── Dockerfile    
├── README.md             
└── requirements.txt
```

## Dataset Download and Preparation

### Downloading the Dataset

1. Manual Download:

- Click on the Google Drive link: Crowd Counting Dataset
- Download the dataset zip file

2. Automated Download (Recommended):
You can use the following bash script to download the dataset:

```bash
#!/bin/bash

# Create data directory if it doesn't exist
mkdir -p data/dataset

# Download dataset using gdown (ensure gdown is installed)
pip install gdown
gdown https://drive.google.com/uc?id=1Wr2L25d6XlGvYSsRbUCttXYBZRWwkp0B -O data/dataset/crowd_counting_dataset.zip

# Unzip the dataset
unzip data/dataset/crowd_counting_dataset.zip -d data/dataset

# Optional: Remove the zip file after extraction
rm data/dataset/crowd_counting_dataset.zip
```

### Dataset Preparation

After downloading, the dataset should be structured as follows:

```
data/
└── dataset/
    ├── images/
    │   ├── train/
    │   └── val/
    └── labels/
        ├── train/
        └── val/
```

### Using the Dataset for Training

- Verify the dataset structure
- Update your training script to point to the correct dataset paths
- When training the YOLOv8 model, use the paths to the train and validation sets

## Usage

Running the Application

- Clone this repository and navigate to the project directory.
- Run the main script

```bash
python main.py
```

- Select the desired processing mode:

1. Real-time camera feed
2. Analyze a video file
3. Process an image

- Follow the prompts to input the image or video path if applicable.

### Output

- Bounding boxes and confidence scores are drawn around detected people.

- Displays:

1. Total People: The total number of detected individuals.
2. Density: The percentage of frame area occupied by detected people, with a density classification:

   - Sparse (Green): Density ≤ 10%.
   - Medium (Yellow): 10% < Density ≤ 30%.
   - Crowded (Red): Density > 30%.

## Docker Deployment

1. Build the Docker image:

```bash
docker build -t people-counting .
```

2. Run the container:

- For image processing:

```bash
docker run -it --rm \
  -v $(pwd)/data/images:/app/data/images \
  people-counting
```

- For video processing:

```bash
docker run -it --rm \
  -v $(pwd)/data/videos:/app/data/videos \
  people-counting
  ```

- For realtime camera:

  ```bash
  docker run -it --rm \
  --device=/dev/video0:/dev/video0 \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  people-counting
  ```

Note: For webcam access on Linux, you might need to run xhost +local:docker first to allow Docker container to access X server.

## Usage Instructions

- Select the desired processing mode:

1. Real-time camera feed
2. Analyze a video file
3. Process an image

- For image/video processing, place your files in the respective mounted directories:
  - Images: ./data/images/
  - Videos: ./data/videos/

- When prompted, enter the path relative to the mounted directory (e.g., "data/images/sample.jpg")

### Output

- Bounding boxes and confidence scores are drawn around detected people.
- Displays:

1. Total People: The total number of detected individuals.
2. Density: The percentage of frame area occupied by detected people, with a density classification:

- Sparse (Green): Density ≤ 10%.
- Medium (Yellow): 10% < Density ≤ 30%.
- Crowded (Red): Density > 30%.

## Acknowledgments

- YOLOv8 by Ultralytics
- OpenCV Library
