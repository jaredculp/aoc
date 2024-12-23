import argparse
import datetime
import os
import pathlib
import subprocess
import sys
import time
from html.parser import HTMLParser

import requests
from dotenv import load_dotenv

load_dotenv()

session = os.environ.get("AOC_SESSION")
if not session:
    raise Exception("Must set AOC_SESSION")


class CodeParser(HTMLParser):
    """
    HTMLParser which grabs all <pre> tags.
    """

    def __init__(self):
        super().__init__()
        self._found = False
        self._code = []

    def handle_starttag(self, tag, attrs):
        if tag == "pre":
            self._found = True

    def handle_endtag(self, tag):
        if self._found and tag == "pre":
            self._found = False

    def handle_data(self, data):
        if self._found:
            self._code.append(data)

    @property
    def code(self):
        return self._code[0]


# Command line args
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--day", type=int, default=datetime.date.today().day)
parser.add_argument("-y", "--year", type=int, default=datetime.date.today().year)
parser.add_argument("-v", "--dev", action="store_true", default=False)
parser.add_argument("-r", "--run", action="store_true", default=False)
parser.add_argument("-a", "--all", action="store_true", default=False)
args = parser.parse_args()
code_parser = CodeParser()

src_path = pathlib.Path(f"{args.year}/src/{args.day:02}.py")

if args.dev and args.run:
    print("Cannot run in --run and --dev mode simultaneously!")
    sys.exit(1)

if args.dev:
    # Fetch input
    url = f"https://adventofcode.com/{args.year}/day/{args.day}"
    real_input = requests.get(f"{url}/input", cookies={"session": session})
    if real_input.status_code != 200:
        print(real_input.text)
        sys.exit(1)

    sample_input = requests.get(url)
    if sample_input.status_code != 200:
        print(sample_input.text)
        sys.exit(1)

    # Parse input
    code_parser.feed(sample_input.text)
    sample = code_parser.code.strip()

    # Create directories and save input
    input_path = pathlib.Path(f"{args.year}/inputs/{args.day:02}.txt")
    input_path.parent.mkdir(parents=True, exist_ok=True)
    input_path.write_text(real_input.text)

    # Create source file
    src_path.parent.mkdir(parents=True, exist_ok=True)
    if not src_path.exists():
        src_path.write_text(
            f'input = """{sample}""".splitlines()\n# input = open("{input_path}").readlines()\nprint(input)\n'
        )

    # Run a file watcher (entr) to rerun the program any time it changes
    subprocess.run(f"ls {src_path} | entr -c python {src_path}", shell=True, text=True)

if args.run:
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
