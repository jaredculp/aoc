import argparse
import datetime
import os
import pathlib
import subprocess
import sys
import time

import requests
from dotenv import load_dotenv

load_dotenv()

session = os.environ.get("AOC_SESSION")
if not session:
    raise Exception("Must set AOC_SESSION")

today = datetime.date.today()

parser = argparse.ArgumentParser()
parser.add_argument("--day", default=today.day)
parser.add_argument("--year", default=today.year)
parser.add_argument("--dev", action="store_true", default=False)
parser.add_argument("--run", action="store_true", default=False)
parser.add_argument("--all", action="store_true", default=False)
args = parser.parse_args()

src_path = pathlib.Path(f"{args.year}/src/{args.day:02}.py")

if args.dev:
    # Fetch input
    url = f"https://adventofcode.com/{args.year}/day/{args.day}/input"
    r = requests.get(url, cookies={"session": session})
    if r.status_code != 200:
        print(r.text)
        sys.exit(1)

    # Create directories and save input
    input_path = pathlib.Path(f"{args.year}/inputs/{args.day:02}.txt")
    input_path.parent.mkdir(parents=True, exist_ok=True)
    input_path.write_text(r.text)

    # Create source file
    src_path.parent.mkdir(parents=True, exist_ok=True)
    if not src_path.exists():
        src_path.write_text(f'input = open("{input_path}").readlines()\nprint(input)\n')

    subprocess.run(f"ls {src_path} | entr -c python {src_path}", shell=True, text=True)
elif args.run:
    start = time.time()
    for path in sorted(list(src_path.parent.glob("*.py")) if args.all else [src_path]):
        script_start = time.time()
        # Assumes each file outputs a single line for p1 and p2
        [p1, p2] = subprocess.run(
            f"python {path}", shell=True, text=True, capture_output=True
        ).stdout.splitlines()
        print(
            f"{path}\t({time.time() - script_start:.2f}s)\nPart 1: {p1}\nPart 2: {p2}\n"
        )
    print(f"🎄 {time.time() - start:.2f}s")
