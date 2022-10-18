from itertools import zip_longest
from itertools import chain


def return_query(film_list, serial_list, number_element=5):
    """
    Return que list with movie/serial/etc
    Used in search
    :param film_list:
    :param serial_list:
    :param number_element:
    :return:
    """
    return list(ele for ele in chain(*zip_longest(film_list, serial_list))
                if ele is not None)[:number_element]
