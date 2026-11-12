
import argparse
import json
import sys
from pathlib import Path

from .analyzer import analyze_traceback


def main():
    parser = argparse.ArgumentParser(
        description="TraceBack - Python Error Explainer"
    )

    parser.add_argument(
        "file",
        nargs="?",
        help="Path to a file containing a Python traceback"
    )

    parser.add_argument(
        "-o", "--output",
        help="Save analysis report to a JSON file"
    )

    args = parser.parse_args()

    if args.file:
        try:
            error_text = Path(args.file).read_text(encoding="utf-8")
        except OSError as error:
            parser.error(f"Could not read file: {error}")
    else:
        if sys.stdin.isatty():
            print("Paste your traceback below. Press Ctrl+D when finished:")

        error_text = sys.stdin.read()

    if not error_text.strip():
        parser.error("No traceback text was provided.")

    result = analyze_traceback(error_text)
    report = json.dumps(result, indent=4)

    if args.output:
        try:
            Path(args.output).write_text(report, encoding="utf-8")
            print(f"Report saved to {args.output}")
        except OSError as error:
            parser.error(f"Could not save report: {error}")
    else:
        print(report)


if __name__ == "__main__":
    main()
