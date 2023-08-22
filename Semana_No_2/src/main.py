# 1) Write a function that takes two strings representing dates and returns
# the string that represents the earliest point in time.
# The strings are in the US-specific MM/DD/YYYY format.
# There's a catch though. Your exercise should support invalid month and date combinations.
# for example 03/55/2021 is still earlier than 04/30/2023, this will prevent you from using datetime module.
#
# >>> foo("01/27/1832", "01/27/1756")
# '01/27/1756'
# >>> foo("02/29/1972", "12/21/1946")
# '12/21/1946'
# >>> foo("02/24/1946", "03/21/1946")
# '02/24/1946'
# >>> foo("06/21/1958", "06/24/1958")
# '06/21/1958'
# >>> foo("06/45/1958", "05/24/1958")
# '05/24/1958'
def get_earlier_date(first_date: str, second_date: str) -> str:
    """ This Function Compare Two Date and Return the Earlier.

    :param first_date: This is First Date to Comparate. - str

    :param second_date: This is Second Date to Comparate. - str

    :return: Return a Earlier Date. - str
    """
    return first_date if first_date.split("/") < second_date.split("/") else second_date


# 2) Write a function that takes any number of arguments, this function supports iterables as arguments for example:
# [[1,2], [2,3,4]] # a lists of lists
# [(1,2), (2,3)] # a lists of tuples
# The function should return a flattened version list of all the iterables that were passed.
# What I mean by this is to literally extract all the integers from the iterables and
# add them in subsequential order to the flattened list. Note that if an integer
# is pass directly as an argument we should also add it to the flattened list.
#
# For example:
# >>> foo([[1, [2, 3]], 4, 5])
# [1, 2, 3, 4, 5]
# >>> foo((1, 2), (3, 4), [5, 6], 7, 8, 9)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> foo([(1, 2), (3, 4)], [[5, 6], [7, 8]], ([10, 11, 12], [13, 14, 15]))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
def flatten(*args: any) -> list:
    """ This Function Flatten the Items of the Sequence.

    :param args: This is the Sequence of Integers to Flatten. - any

    :return: Return a List with Items Flatten. - list
    """
    lst_ = []
    for value in args:
        if not isinstance(value, dict):
            for _ in value:
                if isinstance(_, list) or isinstance(_, tuple):
                    lst_.extend(flatten(_))
                else:
                    lst_.append(_)

            return list(set(sorted(lst_)))

    return lst_


# 3)  Write a function that accepts a sequence (a list for example [1, 1, 2, 2, 3, 3, 4, 5])
# and returns a new iterable with adjacent duplicate values removed.
#
# For example:
# >>> compact([1, 1, 1])
# [1]
# >>> compact([1, 1, 2, 2, 3, 2])
# [1, 2, 3, 2]
# >>> compact([4, 5, 6, 6])
# [4, 5, 6]
# >>> compact([1, 2, 3])
# [1, 2, 3]
def compact(seq: list) -> list:
    """ This Function Remove Duplicate From Sequence.

    :param seq: This is the Sequence of Integers to Remove Duplicate. - list

    :return: Return a List with Items. - list
    """
    _lst = []
    _num_check = 0

    for _num_lst in seq:
        if _num_check != _num_lst:
            _lst.append(_num_lst)

        _num_check = _num_lst

    return _lst
