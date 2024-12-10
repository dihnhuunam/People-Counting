# People Detection and Density Analysis Application

## Overview

This application uses a YOLOv8 model to detect people in images, videos, or real-time camera feeds. It analyzes crowd density based on bounding box areas and provides visual feedback, such as the total number of people detected and density classification (Sparse, Medium, or Crowded).

## Features

1. **Modular Design**:
   - Separate classes for processing images, videos, and real-time camera feeds for better scalability.
2. **People Detection**:
   - Detect people using YOLOv8 and draw bounding boxes with confidence scores.
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

### Files Structure

The application is organized as follows:

```
├── main.py                      # Entry point of the program
├── detectors
│   ├── image_processor.py       # Class for processing images
│   ├── video_processor.py       # Class for processing videos
│   ├── realtime_processor.py    # Class for real-time webcam feed
│   ├── analyzer.py              # Class for analyzing crowd density and statistics
├── requirements.txt             # Packages 
└── README.md                    # Documentation file
```

## Usage

### Running the Application

1. Clone this repository and navigate to the project directory.
2. Run the main script:

   ```bash
   python main.py
   ```

3. Select the desired processing mode:
   - **1**: Real-time camera feed
   - **2**: Analyze a video file
   - **3**: Process an image

4. Follow the prompts to input the image or video path if applicable.

### Outputs

- Bounding boxes and confidence scores are drawn around detected people.
- Displays:
  - **Total People**: The total number of detected individuals.
  - **Density**: The percentage of frame area occupied by detected people, with a density classification:
    - **Sparse** (Green): Density ≤ 10%.
    - **Medium** (Yellow): 10% < Density ≤ 30%.
    - **Crowded** (Red): Density > 30%.

## Example Commands

- For real-time detection:

  ```bash
  python main.py
  ```

  Then select `1` for webcam processing.

- For video analysis:

  ```bash
  python main.py
  ```

  Then select `2` and provide the path to a video file.

- For image analysis:

  ```bash
  python main.py
  ```

  Then select `3` and provide the path to an image file.

## Screenshots

### Real-Time Detection

![Real-Time Detection Example](images/real_time_detection.png)

### Video Processing

![Video Processing Example](images/video_processing.png)

## Extending the Application

1. **To detect other objects**:
   - Modify the `detect_people()` method in the `Processor` classes to include other class names from YOLOv8.

2. **To add new metrics**:
   - Extend the `Analyzer` class to calculate and display additional statistics.

## Contributions

Feel free to fork and create pull requests for new features or improvements. Contributions are welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- [YOLOv8 by Ultralytics](https://github.com/ultralytics/ultralytics)
- [OpenCV Library](https://opencv.org/)

---
Enjoy detecting and analyzing with this scalable and modular application! 🎉
