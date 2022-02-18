from ball_tracker.lens import Lens
from ball_tracker.pose_3d import Pose3D


class Camera:
    def __init__(self, port: int, lens: Lens, pose: Pose3D):
        """Construct camera instance with given port id, lens parameters, and 3D pose in space"""
        self.port = port
        self.lens = lens
        self.pose = pose