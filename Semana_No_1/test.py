import unittest

from main import convert_list_to_dict, \
    extract_dict_from_list, \
    extract_item_from_list, \
    get_values_from_dict, \
    get_value_from_odd_key, \
    return_last_items


class TestConvertListToDict(unittest.TestCase):
    def test_convert_unorder_list_to_dict(self):
        _numbers_list = [2, 4, 1, 3, 5, 8, 7, 6]
        _result = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8}
        self.assertEqual(convert_list_to_dict(_numbers_list), _result)

    def test_convert_unorder_string_list_to_dict(self):
        _numbers_list = ["2", "4", "1", "3", "5", "8", "7", "6"]
        _result = {}
        self.assertEqual(convert_list_to_dict(_numbers_list), _result)


class TestExtractDictFromList(unittest.TestCase):
    def test_extract_dict_from_list_ok(self):
        _numbers_list = [1, 2, 3, 4, 5, 6, 7, {"a": 0}]
        _result = [{'a': 0}]
        self.assertEqual(extract_dict_from_list(_numbers_list), _result)

    def test_extract_dict_from_list_ko(self):
        _numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
        _result = []
        self.assertEqual(extract_dict_from_list(_numbers_list), _result)

class TestExtractItemFromList(unittest.TestCase):
    def test_extract_item_from_list_dict(self):
        _lst = ["1", (2,), ["3", 4, {"5": 6}], ["siete"], "8", {"9": 10, "11": [12, {"13": 14, "15": "dieciséis"}]}]
        _item = {"13": 14, "15": "dieciséis"}
        _result = {"13": 14, "15": "dieciséis"}
        self.assertEqual(extract_item_from_list(_item, _lst), _result)

    def test_extract_item_from_list_dict_item(self):
        _lst = ["1", (2,), ["3", 4, {"5": 6}], ["siete"], "8", {"9": 10, "11": [12, {"13": 14, "15": "dieciséis"}]}]
        _item = 6
        _result = 6
        self.assertEqual(extract_item_from_list(_item, _lst), _result)

    def test_extract_item_from_list_tuple(self):
        _lst = ["1", (2,), ["3", 4, {"5": 6}], ["siete"], "8", {"9": 10, "11": [12, {"13": 14, "15": "dieciséis"}]}]
        _item = (2,)
        _result = (2,)
        self.assertEqual(extract_item_from_list(_item, _lst), _result)

    def test_extract_item_from_list_lst(self):
        _lst = ["1", (2,), ["3", 4, {"5": 6}], ["siete"], "8", {"9": 10, "11": [12, {"13": 14, "15": "dieciséis"}]}]
        _item = ["siete"]
        _result = ["siete"]
        self.assertEqual(extract_item_from_list(_item, _lst), _result)

    def test_extract_item_from_list_str(self):
        _lst = ["1", (2,), ["3", 4, {"5": 6}], ["siete"], "8", {"9": 10, "11": [12, {"13": 14, "15": "dieciséis"}]}]
        _item = "1"
        _result = "1"
        self.assertEqual(extract_item_from_list(_item, _lst), _result)

    def test_extract_item_from_list_int(self):
        _lst = ["1", (2,), ["3", 4, {"5": 6}], ["siete"], "8", {"9": 10, "11": [12, {"13": 14, "15": "dieciséis"}]}]
        _item = 12
        _result = 12
        self.assertEqual(extract_item_from_list(_item, _lst), _result)


class TestGetValuesFromDict(unittest.TestCase):
    def test_convert_list_to_dict_ok(self):
        _numbers_list = [1, 2, 3, 4, 5, 6, 7, {"a": 0}]
        _result = [0]
        self.assertEqual(get_values_from_dict(_numbers_list), _result)

    def test_convert_list_to_dict_ko(self):
        _numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
        _result = []
        self.assertEqual(get_values_from_dict(_numbers_list), _result)


class TestGetValueFromOddKey(unittest.TestCase):
    def test_get_value_from_odd_key_ok(self):
        _numbers_dict = {"a": 0, 0: "a", "b": 1, 1: "b", "c": 2, 2: "c", "d": 3, 3: "d"}
        _result = ['b', 'd']
        self.assertEqual(get_value_from_odd_key(_numbers_dict), _result)

    def test_get_value_from_odd_key_ko(self):
        _numbers_dict = {"a": 0}
        _result = []
        self.assertEqual(get_value_from_odd_key(_numbers_dict), _result)


class TestReturnLastItems(unittest.TestCase):
    def test_return_last_items_ok(self):
        _seq = (1, 2, 3, 4, 5, 6, 7, 8, ["A", "B", "C"], "Python")
        _result = [7, 8, ['A', 'B', 'C'], 'Python']
        self.assertEqual(return_last_items(_seq, 4), _result)

    def test_return_last_items_ko(self):
        _seq = {"a": 0}
        _result = []
        self.assertEqual(return_last_items(_seq, 1), _result)
