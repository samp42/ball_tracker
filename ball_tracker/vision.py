import cv2 as cv
import numpy as np
from ball_tracker.enum.cameras_enum import Cameras
from ball_tracker.enum.colors_enum import Colors


def get_image_from_camera(id: Cameras.value) -> np.ndarray:
    """Return an image from camera id"""
    return cv.imread()


def filter_color(img: np.ndarray, color: Colors.value) -> np.ndarray:
    """Return mask of filtered image with given color"""
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower = [color.hue_min, color.sat_min, color.val_min]
    upper = [color.hue_max, color.sat_max, color.val_max]
    return cv.inRange(hsv, lower, upper)


def get_distance(blobs: [float]) -> [float]:
    """From an image, return distances of blobs based on size of object and measured size of blobs"""
    return [1.0]
