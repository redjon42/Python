
def bounded_numbers(num_list, lower, upper, lower_include=True, upper_include=False):
    """
    :param num_list: a list of integers
    :param lower: integer that represents the lower bound
    :param upper: integer that represents the upper bound
    :param lower_include boolean of inclusion of the lower bound
    :param upper_include boolean of inclusion of the upper bound
    :return:
    """
    if type(num_list[0] == int):
        if (lower_include == True) and (upper_include == True):
            out_list = []
            for val in num_list:
                if lower <= val <= upper:
                    out_list.append(val)
        elif (lower_include == True) and (upper_include == False):
            out_list = []
            for val in num_list:
                if lower <= val < upper:
                    out_list.append(val)
        elif (lower_include == False) and (upper_include == True):
            out_list = []
            for val in num_list:
                if lower < val <= upper:
                    out_list.append(val)
        elif (lower_include == False) and (upper_include == True):
            out_list = []
            for val in num_list:
                if lower < val < upper:
                    out_list.append(val)
    else:
        out_list = ["unsupported data type"]
    return out_list


def list_sum(num_list):
    """
    :param num_list: a list of integers
    :return: their sum
    """
    sum = 0
    for num in num_list:
        sum += num
    return sum


def pretty_printer(bounded_numbers_output):
    total = list_sum(bounded_numbers_output)
    print("The sum of numbers greater than or equal to 1 and less than 10 is:", total)


""" Test Routine """
test_0 = [1, 3, 10, 4, 66]
test_1 = bounded_numbers(test_0, 1, 10)
pretty_printer(test_1)

