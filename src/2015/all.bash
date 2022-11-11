#!/usr/bin/env bash
set -euo pipefail

time ls $(dirname "$0")/*.py | xargs -n1 python
