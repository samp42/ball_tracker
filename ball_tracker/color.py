import numpy as np


class Color:
    """A structure aggregating minimum and maximum HSL values of a color"""
    def __init__(self, hmin, smin, lmin, hmax, smax, lmax):
        self.hue_min = hmin
        self.sat_min = smin
        self.lum_min = lmin
        self.hue_max = hmax
        self.sat_max = smax
        self.lum_max = lmax

    def get_min_values(self) -> np.array:
        """Return minimum HSL values"""
        return np.array([self.hue_min, self.sat_min, self.lum_min])

    def get_max_values(self) -> np.array:
        """Return maximum HSL values"""
        return np.array([self.hue_max, self.sat_max, self.lum_max])
