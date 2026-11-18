# TraceBack — Python Error Explainer

TraceBack is a Python command-line tool that analyzes Python traceback messages and explains common errors in simple language.

## Features
- Identifies common Python exceptions.
- Extracts error messages.
- Extracts filenames, line numbers and function names.
- Explains possible causes of errors.
- Provides debugging suggestions.
- Reads traceback text from files or standard input.
- Exports analysis reports as JSON.

## Supported Exceptions
- NameError
- TypeError
- ValueError
- IndexError
- KeyError
- ZeroDivisionError

## Requirements
- Python 3.12 or later
- No external packages required.

## Usage

Analyze a traceback file:

```bash
python3 -m traceback_explainer.cli sample_error.txt
```

Export a JSON report:

```bash
python3 -m traceback_explainer.cli sample_error.txt -o report.json
```

Run interactively:

```bash
python3 -m traceback_explainer.cli
```

Paste your traceback and press Ctrl+D when finished.

## Run Tests

```bash
python3 -m unittest
```

## Technologies
- Python
- Regular expressions
- JSON
- Argparse
- File handling
- Unittest

## Project Purpose

This project demonstrates Python programming, debugging, error handling, command-line development, file processing and automated testing.