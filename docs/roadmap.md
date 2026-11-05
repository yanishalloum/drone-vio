# Roadmap

Every phase has: **what / why / how / success criterion**, and is evaluated with
`scripts/evaluate.sh` on MH_01_easy, MH_03_medium and V1_01_easy.

## 0. Conventions

- `T_AB` maps points from B to A: `p_A = T_AB · p_B`; compose `T_AC = T_AB · T_BC`.
- Frames: `W` world (mocap), `B` body (IMU), `C` cam0. EuRoC ground truth is `T_WB`;
  camera ground truth is `T_WC = T_WB · T_BC` (`T_BS` in `cam0/sensor.yaml`).
- Quaternions: Hamilton, EuRoC order `[w, x, y, z]`; scipy and TUM use `[x, y, z, w]`.

## Phase 0 — Data & evaluation
- **What**: EuRoC loader, undistortion, camera-frame ground truth, TUM export, `evo` ATE/RPE.
- **Why**: without a trustworthy metric no improvement can be demonstrated.
- **Done when**: a reference system (DPVO or ORB-SLAM3) evaluated through the same script gives a few cm ATE on MH_01.

## Phase 1 — Correct two-view geometry
- **What**: ORB + NMS + bucketing, ratio test, 5-point E in RANSAC, cheirality, correct pose composition.
- **Why**: everything downstream inherits two-view errors.
- **Done when**: >60 % RANSAC inliers on MH_01, trajectory shape correct after Sim(3) alignment.

## Phase 2 — Frame-to-map tracking
- **What**: two-keyframe initialisation, DLT triangulation, PnP RANSAC, keyframe policy.
- **Why**: a shared 3-D map gives a consistent (though arbitrary) scale.
- **Done when**: ATE at least halved vs Phase 1.

## Phase 3 — Local bundle adjustment
- **What**: sliding-window BA on SE(3) with robust kernels (scipy → GTSAM).
- **Why**: jointly refining poses and points stops error accumulation.

## Phase 4 — IMU fusion
- **4a**: loosely-coupled ESKF (15-D error state + scale), gravity, discretised noise.
- **4b**: tightly-coupled MSCKF or preintegration + factor graph; compare with OpenVINS.
- **Done when**: metric ATE (SE(3) alignment, no scale correction) around 10 cm on MH_01.

## Phase 5 — Learned components
- **5a**: ALIKED/SuperPoint + LightGlue as a drop-in front-end (same back-end → clean ablation).
- **5b**: run DPVO, DROID-SLAM, MASt3R-SLAM on the same sequences.
- **5c**: metric monocular depth to recover scale without IMU.
- Report accuracy **and** runtime / GPU memory — what matters on a drone.

## Phase 6 — Loop closure (optional)
Place recognition + pose-graph optimisation → SLAM.

## Reading list
- Scaramuzza & Fraundorfer, VO tutorial — https://rpg.ifi.uzh.ch/visual_odometry_tutorial.html
- Cyrill Stachniss lectures — https://www.youtube.com/@CyrillStachniss
- Solà, ESKF — https://arxiv.org/abs/1711.02508 · micro Lie theory — https://arxiv.org/abs/1812.01537
- Forster et al., IMU preintegration — https://arxiv.org/abs/1512.02363
- OpenVINS docs — https://docs.openvins.com
- LightGlue — https://github.com/cvg/LightGlue · DPVO — https://github.com/princeton-vl/DPVO
- MASt3R-SLAM — https://edexheim.github.io/mast3r-slam · VGGT — https://vgg-t.github.io
- evo — https://github.com/MichaelGrupp/evo
