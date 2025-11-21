import unittest
import sys
import os

# Add parent directory to path so we can import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import global_resource as gr

class TestGlobalResource(unittest.TestCase):

    def test_check_date_format(self):
        self.assertTrue(gr.check_date_format("12/12/2023"))
        self.assertTrue(gr.check_date_format("1/1/2023"))
        self.assertFalse(gr.check_date_format("2023/12/12"))
        self.assertFalse(gr.check_date_format("12-12-2023"))
        self.assertFalse(gr.check_date_format("invalid"))

    def test_check_time_format(self):
        self.assertTrue(gr.check_time_format("12:30:00"))
        self.assertTrue(gr.check_time_format("1:5:9"))
        self.assertFalse(gr.check_time_format("12:30"))
        self.assertFalse(gr.check_time_format("invalid"))

    def test_extract_date(self):
        self.assertEqual(gr.extract_date("12/10/2023"), (2023, 10, 12))
        self.assertEqual(gr.extract_date("1/2/2023"), (2023, 2, 1))

    def test_extract_time(self):
        self.assertEqual(gr.extract_time("12:30:45"), (12, 30, 45))
        self.assertEqual(gr.extract_time("1:2:3"), (1, 2, 3))

    def test_convert_to_seconds(self):
        self.assertEqual(gr.convert_to_seconds("10s"), 10.0)
        self.assertEqual(gr.convert_to_seconds("1m"), 60.0)
        self.assertEqual(gr.convert_to_seconds("1h"), 3600.0)
        self.assertEqual(gr.convert_to_seconds("1d"), 86400.0)
        self.assertEqual(gr.convert_to_seconds("0.5m"), 30.0)

    def test_check_date_validity(self):
        self.assertTrue(gr.check_date("28/02/2023"))
        self.assertFalse(gr.check_date("30/02/2023")) # Invalid date
        self.assertFalse(gr.check_date("12/13/2023")) # Invalid month

    def test_check_time_validity(self):
        self.assertTrue(gr.check_time("23:59:59"))
        self.assertFalse(gr.check_time("24:00:00")) # Invalid hour
        self.assertFalse(gr.check_time("12:60:00")) # Invalid minute

    def test_check_variable_syntax(self):
        self.assertTrue(gr.check_variable_syntax("var"))
        self.assertTrue(gr.check_variable_syntax("var_1"))
        self.assertTrue(gr.check_variable_syntax("_var"))
        self.assertFalse(gr.check_variable_syntax("1var"))
        self.assertFalse(gr.check_variable_syntax("var-1"))
        self.assertFalse(gr.check_variable_syntax("var space"))

    def test_check_value_syntax(self):
        self.assertTrue(gr.check_value_syntax("10s"))
        self.assertTrue(gr.check_value_syntax("1.5h"))
        self.assertTrue(gr.check_value_syntax("100d"))
        self.assertFalse(gr.check_value_syntax("10"))
        self.assertFalse(gr.check_value_syntax("10x"))
        self.assertFalse(gr.check_value_syntax("s"))

    def test_check_true_false_syntax(self):
        self.assertTrue(gr.check_true_false_syntax("true"))
        self.assertTrue(gr.check_true_false_syntax("FALSE"))
        self.assertFalse(gr.check_true_false_syntax("yes"))
        self.assertFalse(gr.check_true_false_syntax("0"))

if __name__ == '__main__':
    unittest.main()
