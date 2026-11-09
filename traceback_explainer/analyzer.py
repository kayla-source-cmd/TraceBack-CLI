from .exceptions_db import EXCEPTIONS

def identify_exception(error_text):
        for exception in EXCEPTIONS:
            if exception in error_text:
                return exception
        return None
                