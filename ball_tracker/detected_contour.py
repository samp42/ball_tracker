import numpy as np

from ball_tracker.enum.colors_enum import Colors


class DetectedContour:
    """Structure to represent a contour detected in the pipeline"""
    def __init__(self, hsl, contour, x, y, radius, color: Colors):
        self.hsl = hsl
        self.contour = contour
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
