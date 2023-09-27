# 1) Write a function that takes 3 arguments, first argument is a given string, second argument another given string,
# third arguments is n. Swap the first n characters of string_1 with the first n characters of string_2 and viceversa,
# The function should return both swapped strings into a single string, if the length of the two strings is
# lesser than n return an empty string.
def swap_two_string(first: str, second: str, n: int) -> str:
    """ Swap two String of n number of characters

    :param first: First String to Swap - str
    :param second: Second String to Swap - str
    :param n: Number of Characters of Swap - int
    :return: The Swapped strings or Empty String - str
    """
    if len(first) < n or len(second) < n:
        return ""
    else:
        first, second = second[:n] + first[n:], first[:n] + second[n:]
        return first + second


# 2) Write a function that takes a string as argument, record all occurrence of every char in the given string,
# use a dictionary to store the occurrences where key is the char and the value is the frequency of that char
# on alphabet.
#
# On a new string add every char with a value >= 10, otherwise an empty string will be return.
# The string return should be in alphabet order.
def count_occurrence(received_str: str) -> str:
    """ Count Occurrence of String

    :param received_str: String to Count - str
    :return: The String with Character and Occurrence Number >= 10 - str
    """
    import string

    alphabetic_dict = dict.fromkeys(string.ascii_lowercase, 0)
    occurrences = ""

    for character in received_str:
        if character in alphabetic_dict:
            alphabetic_dict[character] += 1

    for k, v in alphabetic_dict.items():
        if v >= 10:
            occurrences += k

    return occurrences


# 3) Write a function that takes a list as an argument, the list contains something like this:
# [("HelLoWorlD", "RoR"), ("TookThEtootH",)]. While looping over the list, on every tuple take the first element as
# the original string, and the second one as a substring, insert the substring in the middle of the original string,
# validations required:
# 	a) The middle of the original string is found when a lowercase char is surrounded by two uppercase chars,
# 	such as "AhhhHoHnooH" -> "HoH" is the middle part of the string.
#
# 	b) If the length of the original string is lesser than 3, return an empty string.
#
# 	c) if the tuple does not contain a second element, use the previous substring from last tuple,
# 	if no substring is found use "LoL".
#
# 	d) Every time you insert the substring, the resulting value should be store on a StringIO object.
#
# 	e) Each line you store should have: original_string -> change_to -> new_string
#
# 	f) Use the StringIO object to create a result.txt file, if there is no data store on the
# 	StringIO object raise a custom exception.
def insert_into_middle(lst: list, filename: str = "result.txt") -> str:
    """ Insert Into Middle of String

    :param lst: List of Tuple with String - list
    :param filename: Filename Output - str
    :return: File Path - str
    """
    import re
    from io import StringIO
    from pathlib import Path

    cwd = Path.cwd()
    file_path = cwd / filename
    pattern = "[A-Z][a-z][A-Z]"
    change_to = "LoL"

    for item in lst:
        original_string = item[0]
        if len(item) == 2:
            change_to = item[1]

        try:
            new_string = re.sub(pattern, change_to, original_string, count=1)
            buffer = StringIO(f"{original_string} -> {change_to} -> {new_string}\n")
            with open(file_path, mode='a') as f:
                f.writelines(buffer.getvalue())
        except BaseException:
            raise TypeError("The are a error with the output file")

    return file_path
