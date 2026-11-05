# Postmortem of v0

An honest list of what was wrong in the original course project, why it mattered,
and which phase fixes it. Being able to explain your own mistakes is worth more
than hiding them.

| # | Issue in v0 | Impact | Fix | Phase |
|---|---|---|---|---|
| D1 | FAST without non-maximum suppression (~40k corners/frame) | clustered, ambiguous features | NMS + grid bucketing, ~2k features | 1 |
| D2 | Quality judged by matches/features; ~150 matches, no ratio test | few correct correspondences | Lowe ratio test, count RANSAC inliers | 1 |
| D3 | Lens distortion ignored (EuRoC radtan) | systematic bias -> drift | `cv2.undistortPoints` | 0 |
| D4 | Unnormalised 8-point F, no RANSAC | unstable, outlier-sensitive | 5-point E + RANSAC (K known) | 1 |
| D5 | Wrote `E = (K^-1)^T F K` and `R·t = E` | wrong maths | `E = K^T F K`, `E = [t]x R` | 1 |
| D6 | One of the 4 (R, t) decompositions picked by a trace rule | wrong pose on many frames | cheirality test | 1 |
| D7 | `new_pos = R @ pos + t` | incorrect accumulation | compose 4x4 transforms (`T_WC ← T_WC · T_C1C2`) | 1 |
| D8 | Unit-norm translation every frame | scale changes every frame | frame-to-map PnP; IMU for metric scale | 2, 4 |
| D9 | Triangulation presented as producing the trajectory | conceptual confusion | landmarks feed PnP | 2 |
| D10 | RMSE without alignment / time association / cam-IMU extrinsics | metric meaningless | `evo`, Sim(3) for mono, `T_WC = T_WB T_BC` | 0 |
| D11 | Full-state EKF on a quaternion, no gravity, incomplete Jacobians, IMU treated as a measurement | rotation never corrected | ESKF (15-D error state), MSCKF later | 4 |
