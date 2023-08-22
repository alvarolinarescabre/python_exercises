import unittest

from src.main import flatten, compact, get_earlier_date


class TestEarlierDate(unittest.TestCase):
    def test_earlier_date(self):
        _first_date = "07/09/1971"
        _second_date = "14/12/1977"
        _result = "07/09/1971"
        self.assertEqual(get_earlier_date(_first_date, _second_date), _result)


class TestFlatten(unittest.TestCase):
    def test_flatten(self):
        _lst = ["1", (2, 3), [3, 4, {"5": 6, "6":  [1, 2, ("0", 5, "7", 9), 4, "8", {"A": 10, "B": [11, {"A": 12}]}]}]]
        _result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(flatten(_lst), _result)


class TestRemoveDuplicate(unittest.TestCase):
    def test_remove_duplicate(self):
        _lst = [1, 1, 2, 2, 3, 2, 6, 6, 4, 3, 5, 2, 1, 4, 5, 6, 4, 3, 5]
        _result = [1, 2, 3, 4, 5, 6]
        self.assertEqual(compact(_lst), _result)