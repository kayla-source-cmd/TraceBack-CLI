import unittest

from traceback_explainer.analyzer import (
    identify_exception,
    extract_traceback_details,
    analyze_traceback
)

class TestIdentifyException(unittest.TestCase):

    def test_identifies_name_error(self):
        error_text = "NameError: name 'username' is not defined"
        result = identify_exception(error_text)
        self.assertEqual(result, "NameError")

    def test_returns_none_for_unknown_exception(self):
        error_text = "CustomError: Something went wrong"
        result = identify_exception(error_text)
        self.assertIsNone(result)

    def test_ignores_exception_names_mentioned_earlier(self):
        error_text = (
            "NameError was mentioned earlier.\n"
            "CustomError: Something went wrong"
        )
        result = identify_exception(error_text)
        self.assertIsNone(result)

    def test_extracts_traceback_details(self):
        error_text = (
            'Traceback (most recent call last):\n'
            '  File "/home/user/app.py", line 15, in main\n'
            'ValueError: Invalid value'
        )

        result = extract_traceback_details(error_text)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["filename"], "/home/user/app.py")
        self.assertEqual(result[0]["line_number"], 15)
        self.assertEqual(result[0]["function"], "main")

    def test_analyze_traceback(self):
        error_text = "NameError: name 'username' is not defined"

        result = analyze_traceback(error_text)

        self.assertEqual(result["exception"], "NameError")
        self.assertIn("description", result)
        self.assertIn("causes", result)
        self.assertIn("suggestions", result)    