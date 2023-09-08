import unittest

from Semana_No_1.main import convert_list_to_dict, \
    extract_dict_from_list, \
    extract_item_from_list, \
    get_values_from_dict, \
    get_value_from_odd_key, \
    return_last_items


class TestConvertListToDict(unittest.TestCase):
    def test_convert_unorder_list_to_dict(self):
        numbers_list = [2, 4, 1, 3, 5, 8, 7, 6]
        result = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8}
        self.assertEqual(convert_list_to_dict(numbers_list), result)

    def test_convert_unorder_string_list_to_dict(self):
        numbers_list = ["2", "4", "1", "3", "5", "8", "7", "6"]
        result = {}
        self.assertEqual(convert_list_to_dict(numbers_list), result)


class TestExtractDictFromList(unittest.TestCase):
    def test_extract_dict_from_list_ok(self):
        numbers_list = [1, 2, 3, 4, 5, 6, 7, {"a": 0}]
        result = [{'a': 0}]
        self.assertEqual(extract_dict_from_list(numbers_list), result)

    def test_extract_dict_from_list_ko(self):
        numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
        result = []
        self.assertEqual(extract_dict_from_list(numbers_list), result)


class TestExtractItemFromList(unittest.TestCase):
    def test_extract_item_from_list_dict(self):
        lst = ["1", (2,), ["3", 4, {"5": 6}], ["siete"], "8", {"9": 10, "11": [12, {"13": 14, "15": "dieciséis"}]}]
        item = {"13": 14, "15": "dieciséis"}
        result = {"13": 14, "15": "dieciséis"}
        self.assertEqual(extract_item_from_list(item, lst), result)

    def test_extract_item_from_list_dict_item(self):
        lst = ["1", (2,), ["3", 4, {"5": 6}], ["siete"], "8", {"9": 10, "11": [12, {"13": 14, "15": "dieciséis"}]}]
        item = 6
        result = 6
        self.assertEqual(extract_item_from_list(item, lst), result)

    def test_extract_item_from_list_tuple(self):
        lst = ["1", (2,), ["3", 4, {"5": 6}], ["siete"], "8", {"9": 10, "11": [12, {"13": 14, "15": "dieciséis"}]}]
        item = (2,)
        result = (2,)
        self.assertEqual(extract_item_from_list(item, lst), result)

    def test_extract_item_from_list_lst(self):
        lst = ["1", (2,), ["3", 4, {"5": 6}], ["siete"], "8", {"9": 10, "11": [12, {"13": 14, "15": "dieciséis"}]}]
        item = ["siete"]
        result = ["siete"]
        self.assertEqual(extract_item_from_list(item, lst), result)

    def test_extract_item_from_list_str(self):
        lst = ["1", (2,), ["3", 4, {"5": 6}], ["siete"], "8", {"9": 10, "11": [12, {"13": 14, "15": "dieciséis"}]}]
        item = "1"
        result = "1"
        self.assertEqual(extract_item_from_list(item, lst), result)

    def test_extract_item_from_list_int(self):
        lst = ["1", (2,), ["3", 4, {"5": 6}], ["siete"], "8", {"9": 10, "11": [12, {"13": 14, "15": "dieciséis"}]}]
        item = 12
        result = 12
        self.assertEqual(extract_item_from_list(item, lst), result)


class TestGetValuesFromDict(unittest.TestCase):
    def test_convert_list_to_dict_ok(self):
        numbers_list = [1, 2, 3, 4, 5, 6, 7, {"a": 0}]
        result = [0]
        self.assertEqual(get_values_from_dict(numbers_list), result)

    def test_convert_list_to_dict_ko(self):
        numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
        result = []
        self.assertEqual(get_values_from_dict(numbers_list), result)


class TestGetValueFromOddKey(unittest.TestCase):
    def test_get_value_from_odd_key_ok(self):
        numbers_dict = {"a": 0, 0: "a", "b": 1, 1: "b", "c": 2, 2: "c", "d": 3, 3: "d"}
        result = ['b', 'd']
        self.assertEqual(get_value_from_odd_key(numbers_dict), result)

    def test_get_value_from_odd_key_ko(self):
        numbers_dict = {"a": 0}
        result = []
        self.assertEqual(get_value_from_odd_key(numbers_dict), result)


class TestReturnLastItems(unittest.TestCase):
    def test_return_last_items_ok(self):
        seq = (1, 2, 3, 4, 5, 6, 7, 8, ["A", "B", "C"], "Python")
        result = [7, 8, ['A', 'B', 'C'], 'Python']
        self.assertEqual(return_last_items(seq, 4), result)

    def test_return_last_items_ko(self):
        seq = {"a": 0}
        result = []
        self.assertEqual(return_last_items(seq, 1), result)
