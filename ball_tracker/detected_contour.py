from ball_tracker.enum.colors_enum import Colors


class DetectedContour:
    """Structure to represent a contour detected in the pipeline"""
    def __init__(self, contour, x, y, radius, color: Colors.value):
        self.contour = contour
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
