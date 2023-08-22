import unittest

from src.main import flatten, compact, get_earlier_date


class TestEarlierDate(unittest.TestCase):
    def test_earlier_date_valid_format_date(self):
        _first_date = "09/07/1971"
        _second_date = "12/14/1977"
        _result = "09/07/1971"
        self.assertEqual(get_earlier_date(_first_date, _second_date), _result)

    def test_earlier_date_invalid_format_date(self):
        _first_date = "06/45/1958"
        _second_date = "12/14/1977"
        _result = "06/45/1958"
        self.assertEqual(get_earlier_date(_first_date, _second_date), _result)


class TestFlatten(unittest.TestCase):
    def test_flatten_ok(self):
        _lst = ["1", (2, 3), [3, 4, 6, [1, 2, 10,  ("0", 5, "7", 9), 4, "8", [11, 12]]]]
        _result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(flatten(_lst), _result)

    def test_flatten_ko(self):
        _lst = {"1": 2, "5": 6, "6":  2, "A": 10, "B": 11}
        _result = []
        self.assertEqual(flatten(_lst), _result)


class TestRemoveDuplicate(unittest.TestCase):
    def test_compact_ok(self):
        _lst = [1, 1, 2, 2, 3, 2, 6, 6, 4, 3, 5, 2, 1, 4, 4, 5, 6, 4, 3, 5]
        _result = [1, 2, 3, 2, 6, 4, 3, 5, 2, 1, 4, 5, 6, 4, 3, 5]
        self.assertEqual(compact(_lst), _result)
