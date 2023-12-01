#!/usr/bin/env bash
set -euo pipefail

for f in $(ls $1/src/*.py)
do
  echo "$f"
  echo "--------------"
  time python "$f"
  echo
done
