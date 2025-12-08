import argparse
import importlib
from pathlib import Path
import sys


BASE = Path(__file__).parent
INPUTS = BASE / "inputs"


def load_input(day: int, input_type: str) -> list[str]:
    folder = INPUTS / f"input_{input_type}"
    path = folder / f"day_{day:02}.txt"

    if not path.exists():
        raise FileNotFoundError(f"Missing input file: {path}")

    return [line.strip() for line in path.read_text().splitlines()]


def load_input_no_strip(day: int, input_type: str) -> list[str]:
    folder = INPUTS / f"input_{input_type}"
    path = folder / f"day_{day:02}.txt"

    if not path.exists():
        raise FileNotFoundError(f"Missing input file: {path}")

    return path.read_text().splitlines()


def load_day(day: int):
    module_name = f"aoc.solutions.day_{day:02}"
    try:
        return importlib.import_module(module_name)
    except ImportError:
        raise ImportError(f"No solution file found for day {day:02}")


def main():
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions")
    parser.add_argument("day", type=int, help="Day number (1-12)")
    parser.add_argument("part", type=int, choices=[1, 2], help="Part number")
    parser.add_argument("input", choices=["min", "full"], help="Input type")
    parser.add_argument("--no-strip", action="store_true", help="Do not strip input lines")

    args = parser.parse_args()

    lines = load_input(args.day, args.input) if not args.no_strip else load_input_no_strip(args.day, args.input)
    module = load_day(args.day)

    func = getattr(module, f"part_{args.part}", None)
    if not func:
        raise AttributeError(f"part_{args.part} not implemented for day {args.day:02}")

    result = func(lines)
    print(result)


if __name__ == "__main__":
    sys.exit(main())
