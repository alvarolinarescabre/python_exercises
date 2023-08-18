#############################################################
#                 Práctica Primera Semana                   #
#############################################################


# 1) Crear una función que reciba una lista de números, y que devuelva un diccionario dónde cada key sea el elemento
# de la lista en string y su value sea el mismo elemento en su tipo de dato original,
# el diccionario debe estar en ordenado de menor a mayor.
def convert_list_to_dict(received_list: list) -> dict:
    """ This Function Convert List with Integers Items to Dictionary String Keys and Integers Values.

    :param received_list: This is the List argument of the function with Integers.
    :type received_list: list, require

    :return: A Dictionary with List item as a Key like as String and the Items of the List as Dictionary Values.
    :rtype: list
    """
    return_dict = {}
    for number in sorted(received_list):
        if isinstance(number, int):
            return_dict[str(number)] = number

    return return_dict


# 2) Crear una función que reciba una lista donde se extraigan solo los diccionarios y los devuelva en otra lista,
# en caso de que la lista de entrada no tenga dict devolver una lista vacía.
def extract_dict_from_list(received_list: list) -> list:
    """ This Function Take from a List ONLY Dictionary in a New List if not Dictionary in List return Empty List.

    :param received_list: This is the List argument of the function with Items.
    :type received_list: list, require

    :return: A List with Dictionary or Empty List if not Dictionary on the Original List.
    :rtype: list
    """
    return_list = []
    for key, value in enumerate(received_list):
        if isinstance(value, dict):
            return_list.append(value)

    return return_list


# 3) Como obtengo el siguiente elemento de la lista.
# Elemento a obtener: {'13': 14, '15': 'dieciséis'}
# lst = ["1", (2), ["3", 4, {"5": 6}],["siete"], "8", {"9": 10, "11": [12, {"13": 14,"15": "dieciséis"}]}]
def extract_item_from_list(item: any, received_list: list) -> any:
    """ This Function Extract a Specific Item from a List.

    :param item: This is the Item to extract.
    :type item: any, require

    :param received_list: This is the List with Items to Extract.
    :type item: list, require

    :return: The Item to Extract of a List.
    :rtype: any
    """
    for l1 in received_list:
        if l1 == item:
            return l1
        elif isinstance(l1, dict):
            for l2 in l1.values():
                if isinstance(l2, list):
                    for k, lst in enumerate(l2):
                        if lst == item:
                            return l2[k]
        elif isinstance(l1, list):
            for l2 in l1:
                if isinstance(l2, dict):
                    for k, v in l2.items():
                        if v == item:
                            return l2.get(k)


# 4) Crear una función que reciba una lista de diccionarios
# y devuelva una nueva lista con todos los valores de cada dict.
def get_values_from_dict(received_list: list) -> list:
    """ This Function Take from a List ONLY Dictionary Values and Return a List with Dictionary Values.

    :param received_list: This is the List argument of the function with Items.
    :type received_list: list, require

    :return: A List with Values of Dictionary or Empty List if not Dictionary not has Values.
    :rtype: list
    """
    return_list = []
    for value in received_list:
        if isinstance(value, dict):
            for k, v in value.items():
                return_list.append(v)

    return return_list


# 5) Crear una función que reciba un diccionario y devuelva una lista con sus valores siempre y cuando su key sea impar,
# las keys de este diccionario tienen que ser integers, no añadir values de keys que sean string u otro tipo de dato,
# si no hay valores de keys impares devolver una lista vacía.
def get_value_from_odd_key(received_dict: dict) -> list:
    """ This Function Take from a Odd Key of Dictionary and Return the Values on List.

    :param received_dict: This is the Dictionary argument of the function with Items.
    :type received_dict: dict, require

    :return: A List with Dictionary Values of Odd Key or Empty List if not have Odd Key Dictionary.
    :rtype: list
    """
    return_list = []
    for k, v in received_dict.items():
        if isinstance(k, int):
            for _ in v:
                if k % 2 == 1:
                    return_list.append(v)

    return return_list


# 6) Crear una función que reciba una secuencia (list, string, o tuple) como primer parámetro
# y reciba "n" como segundo parámetro, debe devolver los últimos "n" elementos de la secuencia,
# la secuencia debe ser "casteada" a lista.
def return_last_items(received_seq: any, n: int) -> list:
    """ This Function Take from a Sequence (List, String or Tuple) the "n" Last Values on a List.

    :param received_seq: This is the Sequence (List, String or Tuple) argument of the function with Items.
    :type received_seq: any, require

    :param n: This is the number of Item to return.
    :type n: int, require

    :return: A List with Values of the Sequence or Empty List if not Dictionary not has Values.
    :rtype: list
    """
    if isinstance(received_seq, list) or isinstance(received_seq, str) or isinstance(received_seq, tuple):
        return list(received_seq[-n::])
    else:
        return []
