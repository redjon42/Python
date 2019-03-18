
def num_double(num_str):
    """
    :param num_str: a string of numbers
    :return:
    """
    num_str_list = num_str.split()
    num_list = []
    for num in num_str_list:
        num_list.append(int(num))
    double_list = []
    for num in num_list:
        double_list.append([num, num*2])
    return double_list


def list_printer(test_list):
    """
    :param test_list: a list to be printed
    :return: printed table
    """
    for line in test_list:
        print(line[0], '{:>4}'.format(line[1]))


my_str = "1 2 3 4 5"
list_printer(num_double(my_str))
