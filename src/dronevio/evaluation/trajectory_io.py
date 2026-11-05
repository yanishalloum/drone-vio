"""Write trajectories in TUM format so they can be evaluated with `evo`.

TUM line format:  timestamp[s] tx ty tz qx qy qz qw
(note: TUM puts qw LAST, EuRoC puts it first.)
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from scipy.spatial.transform import Rotation


def write_tum(path: str | Path, timestamps_s: np.ndarray, T_WC: np.ndarray) -> None:
    """Save N poses T_WC (N, 4, 4) with timestamps in seconds to a TUM file."""
    T_WC = np.asarray(T_WC)
    q_xyzw = Rotation.from_matrix(T_WC[:, :3, :3]).as_quat()  # scipy order: x, y, z, w
    t = T_WC[:, :3, 3]
    data = np.column_stack([timestamps_s, t, q_xyzw])
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    np.savetxt(path, data, fmt="%.9f")
