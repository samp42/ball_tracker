import cv2 as cv
import numpy as np
from ball_tracker.enum.cameras_enum import Cameras
from ball_tracker.enum.colors_enum import Colors


# def get_image_from_camera(port: Cameras.value) -> np.ndarray:
#     """Return an image from camera id"""
    # return cv.imread()


def filter_color(img: np.ndarray, color) -> np.ndarray:
    """Return mask of filtered image with given color"""
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower = color.get_min_values()
    upper = color.get_max_values()
    return cv.inRange(hsv, lower, upper)


def find_contours(img: np.ndarray) -> np.ndarray:
    """Return image with contours highlighted"""
    pass


def get_distance(blobs: [float]) -> [float]:
    """From an image, return distances of blobs based on size of object and measured size of blobs"""
    return [1.0]
