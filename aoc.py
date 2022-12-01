import argparse
import datetime
import os
import pathlib
import sys

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
args = parser.parse_args()

url = f"https://adventofcode.com/{args.year}/day/{args.day}/input"
r = requests.get(url, cookies={"session": session})
if r.status_code != 200:
    print(r.text)
    sys.exit(1)

folder = f"{args.year}/inputs"
pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
with open(f"{folder}/{args.day:0>2}.txt", "w") as f:
    f.write(r.text)
