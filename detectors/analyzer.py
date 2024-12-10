# detectors/analyzer.py
import cv2

class Analyzer:
    def __init__(self, frame_width, frame_height):
        """
        Analyzer to analyze density and count.

        Args:
            frame_width (int): Frame width in pixels.
            frame_height (int): Frame height in pixels.
        """
        self.frame_width = frame_width
        self.frame_height = frame_height

    def calculate_density(self, people):
        """
        Calculate density based on the total area of bounding boxes.

        Args:
            people (list): List of detected people with bounding boxes.

        Returns:
            float: Density of people as a percentage.
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
        Get the density label based on percentage.

        Args:
            density_percentage (float): Density percentage.

        Returns:
            str: Density label ('Sparse', 'Medium', 'Crowded').
            tuple: RGB color for the label.
        """
        if density_percentage > 30:
            return "Crowded", (0, 0, 255)  # Red for crowded
        elif density_percentage > 10:
            return "Medium", (0, 255, 255)  # Yellow for medium
        else:
            return "Sparse", (0, 255, 0)  # Green for sparse

    def display_analysis(self, frame, people):
        """
        Display analysis info on the frame.

        Args:
            frame (numpy.ndarray): Input frame.
            people (list): List of detected people with bounding boxes.
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
