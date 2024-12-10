# detectors/analyzer.py
import cv2

class Analyzer:
    def __init__(self, frame_width, frame_height):
        """
        @brief Initialize the Analyzer with frame dimensions
        
        @param frame_width (int): Width of the video/image frame in pixels
        @param frame_height (int): Height of the video/image frame in pixels
        """
        self.frame_width = frame_width
        self.frame_height = frame_height

    def calculate_density(self, people):
        """
        @brief Calculate the density of people in the frame
        
        Calculates the total area occupied by people as a percentage of the frame area
        
        @param people (list): List of detected people with their bounding box coordinates
        @return float: Density percentage, representing how much of the frame is occupied by people
        """
        frame_area = self.frame_width * self.frame_height
        if frame_area == 0:
            return 0

        # Calculate total area of all bounding boxes
        total_person_area = sum(
            (x2 - x1) * (y2 - y1) for (x1, y1, x2, y2, _, _) in people
        )

        # Density as a percentage
        density_percentage = (total_person_area / frame_area) * 100
        return density_percentage

    def get_density_label(self, density_percentage):
        """
        @brief Determine the density label and corresponding color based on percentage
        
        @param density_percentage (float): Calculated density percentage
        @return tuple: A tuple containing:
            - str: Density label ('Sparse', 'Medium', 'Crowded')
            - tuple: RGB color corresponding to the density (Red for crowded, Yellow for medium, Green for sparse)
        """
        if density_percentage > 30:
            return "Crowded", (0, 0, 255)  # Red for crowded
        elif density_percentage > 10:
            return "Medium", (0, 255, 255)  # Yellow for medium
        else:
            return "Sparse", (0, 255, 0)  # Green for sparse

    def display_analysis(self, frame, people):
        """
        @brief Display density and people count analysis on the frame
        
        Annotates the input frame with total number of people and density information
        
        @param frame (numpy.ndarray): Input video/image frame to annotate
        @param people (list): List of detected people with their bounding box coordinates
        """
        total_people = len(people)
        density_percentage = self.calculate_density(people)
        density_label, label_color = self.get_density_label(density_percentage)

        # Display total people
        cv2.putText(frame, f"Total People: {total_people}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

        # Display density with label
        density_text = f"Density: {density_percentage:.2f}% ({density_label})"
        cv2.putText(frame, density_text, (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, label_color, 2, cv2.LINE_AA)