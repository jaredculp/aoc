#!/usr/bin/env bash
set -euo pipefail

for f in $(gls $(dirname "$0")/*.py -v)
do
  echo "$f"
  time python "$f"
  echo
done
