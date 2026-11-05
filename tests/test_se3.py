import numpy as np
from scipy.spatial.transform import Rotation

from dronevio.geometry.se3 import inv_T, is_rotation, make_T, skew, transform_points


def random_T(rng):
    return make_T(Rotation.random(random_state=rng).as_matrix(), rng.normal(size=3))


def test_inverse_is_identity():
    rng = np.random.default_rng(0)
    T = random_T(rng)
    assert np.allclose(T @ inv_T(T), np.eye(4))


def test_composition_chains_frames():
    """p_A = T_AB @ T_BC @ p_C must equal transforming step by step."""
    rng = np.random.default_rng(1)
    T_AB, T_BC = random_T(rng), random_T(rng)
    p_C = rng.normal(size=(5, 3))
    step = transform_points(T_AB, transform_points(T_BC, p_C))
    direct = transform_points(T_AB @ T_BC, p_C)
    assert np.allclose(step, direct)


def test_skew_matches_cross():
    a, b = np.array([1.0, 2.0, 3.0]), np.array([-4.0, 0.5, 2.0])
    assert np.allclose(skew(a) @ b, np.cross(a, b))


def test_is_rotation():
    assert is_rotation(Rotation.from_euler("xyz", [0.1, -0.4, 1.2]).as_matrix())
    assert not is_rotation(np.diag([1.0, 1.0, -1.0]))
