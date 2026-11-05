"""Two-view relative pose (Phase 1).

TODO (Phase 1) — fixes D4, D5, D6 of docs/postmortem.md:
    1. Undistort + normalise pixels with K (or pass K to OpenCV).
    2. Estimate the essential matrix with the 5-point algorithm inside RANSAC.
    3. Decompose E into the 4 candidate (R, t) and keep the one that passes the
       cheirality test (triangulated points in front of both cameras).
    4. Return T_{C2 C1} (maps points from camera 1 to camera 2), ||t|| = 1.

Learning exercise: first call cv2.findEssentialMat / cv2.recoverPose, then
re-implement RANSAC and the cheirality test yourself and compare.
"""

from __future__ import annotations

import numpy as np


def relative_pose(pts1: np.ndarray, pts2: np.ndarray, K: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return (T_C2C1, inlier_mask). Translation is unit-norm (scale unobservable)."""
    raise NotImplementedError("Phase 1")
