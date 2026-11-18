import re
from .exceptions_db import EXCEPTIONS


def identify_exception(error_text):
    if not isinstance(error_text, str):
        return None

    lines = [line.strip() for line in error_text.splitlines() if line.strip()]

    if not lines:
        return None

    last_line = lines[-1]

    match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*(?::|$)", last_line)

    if not match:
        return None

    exception = match.group(1)

    if exception in EXCEPTIONS:
        return exception

    return None

def extract_error_message(error_text):
    if not isinstance(error_text, str):
        return None

    lines = [line.strip() for line in error_text.splitlines() if line.strip()]

    if not lines:
        return None

    last_line = lines[-1]

    match = re.match(r"^[A-Za-z_][A-Za-z0-9_]*\s*:\s*(.*)$", last_line)

    if match:
        return match.group(1)

    return None

def extract_traceback_details(error_text):
    details = []

    pattern = r'File "(.+?)", line (\d+), in (.+)'

    matches = re.finditer(pattern, error_text)

    for match in matches:
        details.append({
            "filename": match.group(1),
            "line_number": int(match.group(2)),
            "function": match.group(3)
        })

    return details

def analyze_traceback(error_text):
    exception = identify_exception(error_text)
    error_message = extract_error_message(error_text)
    details = extract_traceback_details(error_text)

    if exception is None:
        return {
            "exception": None,
            "error_message": error_message,
            "message": "Unknown or unsupported exception",
            "details": details
        }

    information = EXCEPTIONS[exception]

    return {
        "exception": exception,
        "error_message": error_message,
        "description": information["description"],
        "causes": information["causes"],
        "suggestions": information["suggestions"],
        "details": details
    }