"""IMU fusion (Phase 4): error-state Kalman filter.

Nominal state: p, v, q, b_g, b_a (+ visual scale lambda in loosely-coupled mode).
Error state: 15-D [dp, dv, dtheta, db_g, db_a] -> no over-parameterised quaternion
in the covariance (fixes D11). Reference: J. Sola, arXiv:1711.02508, sections 5-6.
"""
