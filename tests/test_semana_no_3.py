import unittest

from Semana_No_3.main import correct_args, \
                                foo_0, \
                                foo_1, \
                                foo_2, \
                                foo_3, \
                                unpack_args, \
                                greet


class TestArgsAndKwargs(unittest.TestCase):
    def test_yes_args_not_kwargs(self):
        args = (1, 2, 3)
        kwargs = {}
        result = 'arguments: (1, 2, 3), keywords: {}'
        self.assertEqual(correct_args(*args, **kwargs), result)

    def test_yes_args_and_yes_kwargs(self):
        args = (1, 2, 3)
        kwargs = {"one": 1}
        result = "arguments: (1, 2, 3), keywords: {'one': 1}"
        self.assertEqual(correct_args(*args, **kwargs), result)

    def test_not_args_and_yes_kwargs(self):
        args = ()
        kwargs = {"one": 1, "two": 2, "three": 3}
        result = "arguments: (), keywords: {'one': 1, 'two': 2, 'three': 3}"
        self.assertEqual(correct_args(*args, **kwargs), result)

    def test_not_both(self):
        args = ()
        kwargs = {}
        result = "arguments: (), keywords: {}"
        self.assertEqual(correct_args(*args, **kwargs), result)


class TestFoo(unittest.TestCase):
    def test_foo_0(self):
        age = 0
        result = None
        self.assertEqual(foo_0(age), result)

    def test_foo_1(self):
        end = 0
        start = 1
        result = None
        self.assertEqual(foo_1(end, start), result)

    def test_foo_2(self):
        key = "0"
        result = None
        self.assertEqual(foo_2(key), result)

    def test_foo_3(self):
        index = 0
        result = None
        self.assertEqual(foo_3(index), result)


class TestUnpack(unittest.TestCase):
    def test_unpack_args(self):
        args = (1, 2, 3)
        result = 'arguments: (1, 2, 3)'
        self.assertEqual(unpack_args(*args), result)

    def test_unpack_kwargs(self):
        kwargs = {"one": 1}
        result = "keywords: {'one': 1}"
        self.assertEqual(unpack_args(**kwargs), result)


class TestGreet(unittest.TestCase):
    def test_greet_name_and_lastname(self):
        name = "Chamo"
        lastname = "Linares"
        result = "Hi, my name is Chamo Linares. I'm have 52 old and I live in Alcorcón. " \
                 "My args are () and my kwargs are {}"
        self.assertEqual(greet(name, lastname), result)

    def test_greet_age(self):
        name = "Chamo"
        lastname = "Linares"
        age = 21
        city = "Caracas"
        result = "Hi, my name is Chamo Linares. I'm have 21 old and I live in Caracas. " \
                 "My args are () and my kwargs are {}"
        self.assertEqual(greet(name, lastname, age=age, city=city), result)

    def test_greet_args(self):
        name = "Chamo"
        lastname = "Linares"
        age = 21
        city = "Caracas"
        args = (1, 2, 3, 4)
        result = "Hi, my name is Chamo Linares. I'm have 21 old and I live in Caracas. " \
                 "My args are (1, 2, 3, 4) and my kwargs are {}"
        self.assertEqual(greet(name, lastname, age, city, *args), result)

    def test_greet_kwargs(self):
        name = "Chamo"
        lastname = "Linares"
        age = 21
        city = "Caracas"
        one = 1
        two = 2
        three = 3
        result = "Hi, my name is Chamo Linares. I'm have 21 old and I live in Caracas. " \
                 "My args are () and my kwargs are {'one': 1, 'two': 2, 'three': 3}"
        self.assertEqual(greet(name, lastname, age, city, one=one, two=two, three=three), result)

    def test_greet_all(self):
        name = "Chamo"
        lastname = "Linares"
        age = 21
        city = "Caracas"
        args = (1, 2, 3, 4)
        one = 1
        two = 2
        result = "Hi, my name is Chamo Linares. I'm have 21 old and I live in Caracas. " \
                 "My args are (1, 2, 3, 4) and my kwargs are {'one': 1, 'two': 2}"
        self.assertEqual(greet(name, lastname, age, city, *args, one=one, two=two), result)
