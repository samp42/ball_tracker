import numpy as np


class Pose3D:
    """utility class to play with ball or camera positions in a 3D space"""

    def __init__(self, x, y, z, theta, omega, alpha):
        self.x = x
        self.y = y
        self.z = z
        self.theta = theta
        self.omega = omega
        self.alpha = alpha

    def __int__(self, blob: np.ndarray):
        """from a blob in an image, return a pose of where that ball is relative to the camera"""
        height = 240
        width = 320
        blob_center = [30, 210]
        blob_diameter = 0.2413  # m

        # find axis on which the center of the blob belongs

        # find the distance from the lens where it stands,
        # taking into account the diameter of the blob in the direction of the axis
