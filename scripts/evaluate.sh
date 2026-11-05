#!/usr/bin/env bash
# Evaluate an estimated trajectory against EuRoC ground truth with evo.
# Usage: bash scripts/evaluate.sh results/MH_01_easy [--vio]
#   default: monocular -> Sim(3) alignment (-as)
#   --vio  : metric scale observable -> SE(3) alignment only (-a)
set -euo pipefail
RES_DIR="$1"
ALIGN="-as"
[[ "${2:-}" == "--vio" ]] && ALIGN="-a"

evo_ape tum "$RES_DIR/gt_cam.txt" "$RES_DIR/est.txt" $ALIGN --plot_mode xy \
        --save_plot "$RES_DIR/ape.pdf" --save_results "$RES_DIR/ape.zip"
evo_rpe tum "$RES_DIR/gt_cam.txt" "$RES_DIR/est.txt" $ALIGN --delta 1 --delta_unit m \
        --save_results "$RES_DIR/rpe.zip"
