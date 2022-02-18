import numpy as np


class Color:
    def __init__(self, hmin, smin, vmin, hmax, smax, vmax):
        self.hue_min = hmin
        self.sat_min = smin
        self.val_min = vmin
        self.hue_max = hmax
        self.sat_max = smax
        self.val_max = vmax

    def get_min_values(self) -> np.array:
        """Return minimum hue, sat, val"""
        return np.array([self.hue_min, self.sat_min, self.val_min])

    def get_max_values(self) -> np.array:
        """Return maximum hue, sat, val"""
        return np.array([self.hue_max, self.sat_max, self.val_max])
