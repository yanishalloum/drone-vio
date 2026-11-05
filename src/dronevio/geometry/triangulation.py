"""Linear (DLT) triangulation via SVD (Phase 2).

TODO (Phase 2): port the SVD triangulation from the v0 report (it was correct),
then add:
    - rejection of points behind either camera,
    - rejection of points with low triangulation angle (< ~1-2 deg),
    - rejection by reprojection error.

Remember: triangulation produces *landmarks* (scene points), not the
trajectory. Landmarks are then used by PnP to localise new frames.
"""

from __future__ import annotations

import numpy as np


def triangulate_dlt(P1: np.ndarray, P2: np.ndarray, x1: np.ndarray, x2: np.ndarray) -> np.ndarray:
    """Triangulate (N, 2) pixel correspondences given 3x4 projection matrices -> (N, 3)."""
    raise NotImplementedError("Phase 2")
