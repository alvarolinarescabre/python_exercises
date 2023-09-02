import unittest

from Semana_No_3.src.main import correct_args, foo_0, foo_1, foo_2, foo_3, unpack_args, greet


class TestArgsAndKwargs(unittest.TestCase):
    def test_yes_args_not_kwargs(self):
        _args = (1, 2, 3)
        _kwargs = {}
        _result = 'arguments: (1, 2, 3), keywords: {}'
        self.assertEqual(correct_args(*_args, **_kwargs), _result)

    def test_yes_args_and_yes_kwargs(self):
        _args = (1, 2, 3)
        _kwargs = {"one": 1}
        _result = "arguments: (1, 2, 3), keywords: {'one': 1}"
        self.assertEqual(correct_args(*_args, **_kwargs), _result)

    def test_not_args_and_yes_kwargs(self):
        _args = ()
        _kwargs = {"one": 1, "two": 2, "three": 3}
        _result = "arguments: (), keywords: {'one': 1, 'two': 2, 'three': 3}"
        self.assertEqual(correct_args(*_args, **_kwargs), _result)

    def test_not_both(self):
        _args = ()
        _kwargs = {}
        _result = "arguments: (), keywords: {}"
        self.assertEqual(correct_args(*_args, **_kwargs), _result)


class TestFoo(unittest.TestCase):
    def test_foo_0(self):
        _age = 0
        _result = None
        self.assertEqual(foo_0(_age), _result)

    def test_foo_1(self):
        _end = 0
        _start = 1
        _result = None
        self.assertEqual(foo_1(_end, _start), _result)

    def test_foo_2(self):
        _key = "0"
        _result = None
        self.assertEqual(foo_2(_key), _result)

    def test_foo_3(self):
        _index = 0
        _result = None
        self.assertEqual(foo_3(_index), _result)


class TestUnpack(unittest.TestCase):
    def test_unpack_args(self):
        _args = (1, 2, 3)
        _result = 'arguments: (1, 2, 3)'
        self.assertEqual(unpack_args(*_args), _result)

    def test_unpack_kwargs(self):
        _kwargs = {"one": 1}
        _result = "keywords: {'one': 1}"
        self.assertEqual(unpack_args(**_kwargs), _result)


class TestGreet(unittest.TestCase):
    def test_greet_name_and_lastname(self):
        _name = "Chamo"
        _lastname = "Linares"
        _result = "Hi, my name is Chamo Linares. I'm have 52 old and I live in Alcorcón. " \
                  "My args are () and my kwargs are {}"
        self.assertEqual(greet(_name, _lastname), _result)

    def test_greet_age(self):
        _name = "Chamo"
        _lastname = "Linares"
        _age = 21
        _city = "Caracas"
        _result = "Hi, my name is Chamo Linares. I'm have 21 old and I live in Caracas. " \
                  "My args are () and my kwargs are {}"
        self.assertEqual(greet(_name, _lastname, age=_age, city=_city), _result)

    def test_greet_args(self):
        _name = "Chamo"
        _lastname = "Linares"
        _age = 21
        _city = "Caracas"
        _args = (1, 2, 3, 4)
        _result = "Hi, my name is Chamo Linares. I'm have 21 old and I live in Caracas. " \
                  "My args are (1, 2, 3, 4) and my kwargs are {}"
        self.assertEqual(greet(_name, _lastname, _age, _city, *_args), _result)

    def test_greet_kwargs(self):
        _name = "Chamo"
        _lastname = "Linares"
        _age = 21
        _city = "Caracas"
        _one = 1
        _two = 2
        _three = 3
        _result = "Hi, my name is Chamo Linares. I'm have 21 old and I live in Caracas. " \
                  "My args are () and my kwargs are {'one': 1, 'two': 2, 'three': 3}"
        self.assertEqual(greet(_name, _lastname, _age, _city, one=_one, two=_two, three=_three), _result)

    def test_greet_all(self):
        _name = "Chamo"
        _lastname = "Linares"
        _age = 21
        _city = "Caracas"
        _args = (1, 2, 3, 4)
        _one = 1
        _two = 2
        _result = "Hi, my name is Chamo Linares. I'm have 21 old and I live in Caracas. " \
                  "My args are (1, 2, 3, 4) and my kwargs are {'one': 1, 'two': 2}"
        self.assertEqual(greet(_name, _lastname, _age, _city, *_args, one=_one, two=_two), _result)
