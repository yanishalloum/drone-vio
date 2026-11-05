"""EuRoC MAV dataset loader (Phase 0).

ASL folder layout:
    <seq>/mav0/cam0/data/*.png            images, 20 Hz, 752x480, timestamps in ns
    <seq>/mav0/cam0/sensor.yaml           intrinsics, radtan distortion, T_BS (cam -> body)
    <seq>/mav0/imu0/data.csv              gyro + accel, 200 Hz
    <seq>/mav0/state_groundtruth_estimate0/data.csv   p_WB, q_WB [w,x,y,z], v, biases

TODO (Phase 0):
    - parse sensor.yaml -> K (3x3), dist (4,), T_BC (4x4)
    - iterate (timestamp, grayscale image)
    - load ground truth and convert body poses to camera poses: T_WC = T_WB @ T_BC
    - undistort points with cv2.undistortPoints (fixes D3)
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np


@dataclass
class CameraCalib:
    K: np.ndarray        # 3x3 intrinsics
    dist: np.ndarray     # radial-tangential [k1, k2, p1, p2]
    T_BC: np.ndarray     # 4x4, maps camera-frame points to body (IMU) frame
    resolution: tuple[int, int]


def load_camera_calib(seq_dir: str | Path, cam: str = "cam0") -> CameraCalib:
    raise NotImplementedError("Phase 0")
