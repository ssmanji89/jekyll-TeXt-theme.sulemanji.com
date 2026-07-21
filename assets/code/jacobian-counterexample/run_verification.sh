#!/usr/bin/env bash
set -euo pipefail

python verify_exact.py
python verify_sympy.py
