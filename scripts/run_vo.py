"""Entry point: run the VO pipeline on one EuRoC sequence and write a TUM trajectory.

Implemented progressively (Phase 0 -> 4). Output: results/<seq>/est.txt and gt_cam.txt.
"""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--seq", required=True, help="path to an EuRoC sequence (ASL format)")
    parser.add_argument("--out", default="results")
    args = parser.parse_args()
    raise NotImplementedError(f"Pipeline not implemented yet (args: {args})")


if __name__ == "__main__":
    main()
