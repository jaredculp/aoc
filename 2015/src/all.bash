#!/usr/bin/env bash
set -euo pipefail

for f in $(ls $(dirname "$0")/*.py)
do
  echo "$f"
  time python "$f"
  echo
done
