import unittest

from Semana_No_2.main import flatten, \
                    compact, \
                    get_earlier_date


class TestEarlierDate(unittest.TestCase):
    def test_earlier_date_day_format(self):
        first_date = "05/24/1958"
        second_date = "06/45/1958"
        result = "05/24/1958"
        self.assertEqual(get_earlier_date(first_date, second_date), result)

    def test_earlier_date_month_format(self):
        first_date = "33/06/2002"
        second_date = "39/05/2002"
        result = "39/05/2002"
        self.assertEqual(get_earlier_date(first_date, second_date), result)

    def test_earlier_date_year_format(self):
        first_date = "01/27/1832"
        second_date = "01/27/1756"
        result = "01/27/1756"
        self.assertEqual(get_earlier_date(first_date, second_date), result)


class TestFlatten(unittest.TestCase):
    def test_flatten_list(self):
        seq = [1, 2, 3, (1, 2, 3), [3, 4, 6], [1, 2, 10], (0, 5, 7, 9), [4, 8], [11, 12]]
        result = [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(flatten(seq), result)

    def test_flatten_tuple(self):
        seq = (1, 2, 3, (1, 2, 3), [3, 4, 6], [1, 2, 10], (0, 5, 7, 9), [4, 8], [11, 12])
        result = [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(flatten(seq), result)

    def test_flatten_empty_list(self):
        seq = []
        result = []
        self.assertEqual(flatten(seq), result)

    def test_flatten_empty_tuple(self):
        seq = ()
        result = []
        self.assertEqual(flatten(seq), result)


class TestRemoveDuplicate(unittest.TestCase):
    def test_compact_ok(self):
        lst = [1, 1, 2, 2, 3, 2, 6, 6, 4, 3, 5, 2, 1, 4, 4, 5, 6, 4, 3, 5]
        result = [1, 2, 3, 2, 6, 4, 3, 5, 2, 1, 4, 5, 6, 4, 3, 5]
        self.assertEqual(compact(lst), result)
