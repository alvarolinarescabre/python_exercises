# 1) Pass the correct arguments to function foo to print the expected outputs:
# def foo(*args, **kwargs):
# 	print(f"arguments: {args}, keywords: {kwargs}")
#
# foo(?) # arguments: (1,2,3), keywords: {}
# foo(?) # arguments: (1,2,3), keywords: {'one':1}
# foo(?) # arguments: (), keywords: {'one': 1, 'two': 2, 'three': 3}
# foo(?) # arguments: (), keywords: {}
def correct_args(*args, **kwargs):
    return f"arguments: {args}, keywords: {kwargs}"


# 2) Unpack arguments and keywords to function foo, keep in mind that manually passing positional arguments
# can be tricky, the order is something important to take into consideration, also is not a good practice
# to have a signature that long with many parameters define in a function, sometimes this is not in our control,
# for that reason we need to know how to unpack arguments and keywords when is needed for long signatures define
# in a function.
#
# def foo(id, name, last_name, age, email, username, department):
# 	pass
#
# define arguments and keywords on separate variables
# arguments: tuple = ? # variable define with the arguments to pass to the function
# keywords: dict = ? # variable define with the keywords to pass to the function
#
# unpack then while doing the call on function foo, remember one call for the args and one call for the kwargs.
# foo(?) # args call
# foo(?) # kwargs call
def unpack_args(*args, **kwargs):
    if args:
        return f"arguments: {args}"
    else:
        return f"keywords: {kwargs}"


# 3) Fix all the calls on function foo, keep in mind the order between positional arguments and
# also default argument values.
#
# fix
# def foo(id=None, name=None, age):
# 	pass
#
# fix
# def foo(elements=[], start=1, end):
# 	pass
#
# fix
# def foo(item={"one": 1}, key="1", default_value=None):
# 	pass
#
# fix
# def foo(country_initials=("AR","ES","VE","PE","BO"), index, return_complete=False):
# 	pass
def foo_0(age, id=None, name=None):
    pass


def foo_1(end, start=1, elements=None):
    pass


def foo_2(key="1", item=None, default_value=None):
    pass


def foo_3(index, return_complete=False, country_initials=("AR", "ES", "VE", "PE", "BO")):
    pass


# 4) Write a function that takes two positional arguments, two default arguments, and lastly takes args and kwargs.
# Add three examples by calling your function, you can return or print any output that you want, be creative!
def greet(name, lastname, age=52, city="Alcorcón", *args, **kwargs):
    """ Send a greetings to a person.

    :param name: Name of the person - str
    :param lastname: Lastname of the person - str
    :param age: Age of the person, it has a 52 by default - int
    :param city: City of the person, it has Alcorcón by default - str
    :param args: Positional args to send at the function - any
    :param kwargs: Key args to send at the function - any
    :return: The greeting message - str
    """
    return f"Hi, my name is {name} {lastname}. I'm have {age} old and I live in {city}. " \
           f"My args are {(tuple(v for v in args))} and my kwargs are {kwargs}"
