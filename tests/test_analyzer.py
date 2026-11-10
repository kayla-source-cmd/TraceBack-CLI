import unittest
from traceback_explainer.analyzer import identify_exception


class TestIdentifyException(unittest.TestCase):

    def test_identifies_name_error(self):
        error_text = "NameError: name 'username' is not defined"
        result = identify_exception(error_text)
        self.assertEqual(result, "NameError")

    def test_returns_none_for_unknown_exception(self):
        error_text = "CustomError: Something went wrong"
        result = identify_exception(error_text)
        self.assertIsNone(result)