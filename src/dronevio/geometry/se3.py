"""Rigid-body transforms in SE(3).

Convention (used everywhere in this repo):
    T_AB is a 4x4 matrix mapping points expressed in frame B to frame A:
        p_A = T_AB @ p_B          (homogeneous coordinates)
    Composition chains indices:  T_AC = T_AB @ T_BC
    T_WC is therefore the pose of the camera C in the world W, and its
    translation column is the camera centre expressed in W.

Why it matters: the v0 report updated the position with
`new_pos = R @ pos + t`, which mixes a *relative* rotation with a *global*
position. Composing full 4x4 transforms with explicit frame indices makes
that class of bug impossible.
"""

from __future__ import annotations

import numpy as np


def make_T(R: np.ndarray, t: np.ndarray) -> np.ndarray:
    """Build a 4x4 homogeneous transform from a 3x3 rotation and a 3-vector."""
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = np.asarray(t, dtype=float).reshape(3)
    return T


def inv_T(T: np.ndarray) -> np.ndarray:
    """Closed-form inverse: T_BA = inv(T_AB) = [R^T, -R^T t]."""
    R, t = T[:3, :3], T[:3, 3]
    return make_T(R.T, -R.T @ t)


def transform_points(T_AB: np.ndarray, p_B: np.ndarray) -> np.ndarray:
    """Apply T_AB to an (N, 3) array of points expressed in B -> points in A."""
    p_B = np.atleast_2d(p_B)
    return p_B @ T_AB[:3, :3].T + T_AB[:3, 3]


def skew(v: np.ndarray) -> np.ndarray:
    """[v]x such that skew(a) @ b == np.cross(a, b)."""
    x, y, z = np.asarray(v, dtype=float).reshape(3)
    return np.array([[0.0, -z, y], [z, 0.0, -x], [-y, x, 0.0]])


def is_rotation(R: np.ndarray, atol: float = 1e-6) -> bool:
    """True if R is orthonormal with det(R) = +1."""
    return np.allclose(R.T @ R, np.eye(3), atol=atol) and np.isclose(np.linalg.det(R), 1.0, atol=atol)
