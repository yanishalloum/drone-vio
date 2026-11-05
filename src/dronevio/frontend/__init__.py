"""Front-end: feature detection, description, matching and tracking.

Phase 1: ORB with non-max suppression + grid bucketing, Lowe ratio test (fixes D1, D2).
Optional: KLT optical-flow tracking. The from-scratch FAST/BRIEF of v0 lives in legacy/.
Phase 5: learned front-end (ALIKED/SuperPoint + LightGlue) in dronevio.learned.
"""
