import unittest

from src.main import flatten, compact, get_earlier_date


class TestEarlierDate(unittest.TestCase):
    def test_earlier_date_day_format(self):
        _first_date = "05/24/1958"
        _second_date = "06/45/1958"
        _result = "05/24/1958"
        self.assertEqual(get_earlier_date(_first_date, _second_date), _result)

    def test_earlier_date_month_format(self):
        _first_date = "33/06/2002"
        _second_date = "39/05/2002"
        _result = "39/05/2002"
        self.assertEqual(get_earlier_date(_first_date, _second_date), _result)

    def test_earlier_date_year_format(self):
        _first_date = "01/27/1832"
        _second_date = "01/27/1756"
        _result = "01/27/1756"
        self.assertEqual(get_earlier_date(_first_date, _second_date), _result)


class TestFlatten(unittest.TestCase):
    def test_flatten_list(self):
        _seq = [1, (1, 2, 3), [3, 4, 6], [1, 2, 10], (0, 5, 7, 9), [4, 8], [11, 12]]
        _result = [0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(flatten(_seq), _result)

    def test_flatten_tuple(self):
        _seq = (1, (1, 2, 3), [3, 4, 6], [1, 2, 10], (0, 5, 7, 9), [4, 8], [11, 12])
        _result = [0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(flatten(_seq), _result)

    def test_flatten_empty_list(self):
        _seq = []
        _result = []
        self.assertEqual(flatten(_seq), _result)

    def test_flatten_empty_tuple(self):
        _seq = ()
        _result = []
        self.assertEqual(flatten(_seq), _result)


class TestRemoveDuplicate(unittest.TestCase):
    def test_compact_ok(self):
        _lst = [1, 1, 2, 2, 3, 2, 6, 6, 4, 3, 5, 2, 1, 4, 4, 5, 6, 4, 3, 5]
        _result = [1, 2, 3, 2, 6, 4, 3, 5, 2, 1, 4, 5, 6, 4, 3, 5]
        self.assertEqual(compact(_lst), _result)
