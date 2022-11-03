import argparse
import os
import pathlib

import requests
from dotenv import load_dotenv

load_dotenv()

session = os.environ.get("AOC_SESSION")
if not session:
    raise Exception("Must set AOC_SESSION")

parser = argparse.ArgumentParser()
parser.add_argument("--day", required=True)
parser.add_argument("--year", required=True)
args = parser.parse_args()

url = f"https://adventofcode.com/{args.year}/day/{args.day}/input"
input_data = requests.get(url, cookies={"session": session}).text

folder = f"inputs/{args.year}"
pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
with open(f"{folder}/{args.day}.txt", "w") as f:
    f.write(input_data)
