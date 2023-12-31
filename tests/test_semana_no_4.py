import os
import unittest
import tempfile


from Semana_No_4.main import swap_two_string, count_occurrence, insert_into_middle


class TestSwapString(unittest.TestCase):
    def test_swap_two_string(self):
        str_0 = "abcdefg"
        str_1 = "0123456"
        n = 3
        result = "012defgabc3456"
        self.assertEqual(swap_two_string(str_0, str_1, n), result)

    def test_swap_two_string_less_to_n(self):
        str_0 = "abc"
        str_1 = "0123456"
        n = 10
        result = ""
        self.assertEqual(swap_two_string(str_0, str_1, n), result)


class TestStringOccurrences(unittest.TestCase):
    def test_count_occurrence_more_ten(self):
        string = "aeiou aeiou aeiou aeiou aeiou aeiou aeiou aeiou aeiou aeiou aeiou aeiou aeiou aeiou aeiou"
        result = "aeiou"
        self.assertEqual(count_occurrence(string), result)

    def test_count_occurrence_less_ten(self):
        string = "aeiou aeio aeiu aeou aiou eiou aeio aeio aei aeio ae ae ae aeo ae"
        result = "ae"
        self.assertEqual(count_occurrence(string), result)


class TestInsertIntoMiddle(unittest.TestCase):
    def test_insert_into_middle(self):
        test_file = tempfile.mkstemp()[1]
        lst = [("HelLoWorlD", "RoR"), ("TookThEtootH",)]
        result = "HelLoWorlD -> RoR -> HelRoRorlD\nTookThEtootH -> RoR -> TookRoRtootH\n"
        insert_into_middle(lst, test_file)
        with open(test_file, "r") as f:
            contents = f.read()
        os.remove(test_file)
        self.assertEqual(contents, result)

    def test_insert_into_middle_value_lol(self):
        test_file = tempfile.mkstemp()[1]
        lst = [("HelLoWorlD", ), ("HelLoWorlD", "RoR"), ("TookThEtootH",)]
        result = "HelLoWorlD -> LoL -> HelLoLorlD\nHelLoWorlD -> RoR -> HelRoRorlD\nTookThEtootH -> RoR -> " \
                 "TookRoRtootH\n"
        insert_into_middle(lst, test_file)
        with open(test_file, "r") as f:
            contents = f.read()
        os.remove(test_file)
        self.assertEqual(contents, result)

    def test_insert_into_middle_raise_error(self):
        test_file = tempfile.mkstemp()[1]
        lst = [(b"HelLoWorlD", b"RoR")]
        with self.assertRaises(TypeError):
            insert_into_middle(lst, test_file)
