.PHONY: 2015 2022 2023

dev:
	poetry run python aoc.py

2015:
	time ./runner.bash 2015

2022:
	time ./runner.bash 2022

2023:
	time ./runner.bash 2023

