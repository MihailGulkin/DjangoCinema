from itertools import zip_longest


def return_query(*args, number_element=5):
    result_list = []
    for ele_1, ele_2 in zip_longest(*args):
        if len(result_list) >= number_element:
            return result_list
        if ele_1:
            result_list.append(ele_1)
        if ele_2:
            result_list.append(ele_2)
    return result_list


