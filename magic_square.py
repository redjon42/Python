
"""
exec(open("magic_square.py").read())
"""

"""
Hi! Please enter your square.
One line of entries, separated by spaces
When you're done with entries, enter a blank line.

> 1 2 3
> 4 5 6
> 7 8 9
>  (this is the blank line the user entered)

Okay thanks!
Is it square? Check.
All integers?  Check.
Rows sum to same number?  Bzzt.
Columns sum to same number? Bzzt.
Diagonals?  Bzzt.
This is not a magic square.
"""

"""
def get_lines():
    line_list = []
    line = "1 2 3 4 5 6 7 8 9 10 11 12 13"
    while len(line) != 0:
        line = input("Type a line, blank to stop: ")
        line_list.append(line)
    return line_list
"""


def get_square():
    line_list = []
    print("Hi! Please enter your square")
    print("One line of entries, separated by spaces")
    print("When you're done with entries, enter a blank line.")
    line = "not zero"
    while len(line) != 0:
        line = input("Type a line: ")
        line_list.append(line)
    del line_list[-1]
    return line_list


def make_int(num_string_list):
    """
    :param num_string_list: a list of numeric strings
    :return: the same list as sub-lists of integers
    """
    int_list = []
    for row in num_string_list:
        char_row = row.strip().split()
        int_row = []
        for num in char_row:
            n = int(num)
            int_row.append(n)
        int_list.append(int_row)
    return int_list


def test_square(int_list):
    """
    :param int_list: a list of integers
    :return: boolean: is the array square?
    """
    n_row = len(int_list)

    m_columns = []
    for row in int_list:
        m = len(row)
        m_columns.append(m)

    square = True
    for m in m_columns:
        if m != n_row:
            square = False
    return square


def sum_rows(square_list):
    """
    :param square_list: a square array of integers
    :return: list: sums of the rows
    """
    sum_list = []
    for row in square_list:
        row_sum = sum(row)
        sum_list.append(row_sum)
    return sum_list


def sum_columns(square_list):
    """
    :param square_list: a square array of integers
    :return: list: sum of the columns
    """
    dimension = len(square_list)
    column_sum_list = []
    for i in range(dimension):
        column_sum = 0
        for row in square_list:
            column_sum += row[i]
        column_sum_list.append(column_sum)
    return column_sum_list


def sum_diagonals(square_list):
    """
    :param square_list: a square array of integers.
    :return: list: sum of the left and right diagonals.
    """
    dim = len(square_list)
    d1_sum = 0
    d2_sum = 0
    for i in range(dim):
        d1_sum += square_list[i][i]
        i2 = -1*(i+1)
        d2_sum += square_list[i][i2]
    return [d1_sum, d2_sum]


def test_same(list_of_sums):
    """
    :param list_of_sums: list: output of sum_something().
    :return: boolean: are the sums the same?
    """
    end = len(list_of_sums)
    same = True
    index = 1
    val_0 = list_of_sums[0]
    while same:
        if index < end:
            val = list_of_sums[index]
            if val == val_0:
                index += 1
            else:
                same = False
        else:
            return True
    return same


def test_consecutive(square_list):
    """
    :param square_list: a square array of integers
    :return: do they cover all consecutive numbers in expected range?
    """
    dim = len(square_list)
    count = dim**2
    all_list = list(range(1, count+1))
    test_list = []
    for row in square_list:
        for col in row:
            test_list.append(col)
    index = 0
    same = True
    while same:
        if index < count:
            val = all_list[index]
            if val in test_list:
                index += 1
            else:
                same = False
        else:
            return True
    return same


def sum_list(square_list):
    """
    :param square_list: a square array of integers
    :return: a list of the directional sums
    """
    list_of_sums = list()
    list_of_sums.append(sum_rows(square_list))
    list_of_sums.append(sum_columns(square_list))
    list_of_sums.append(sum_diagonals(square_list))
    return list_of_sums


def un_list(list_2):
    """
    :param list_2: a list with sub-lists
    :return: list: all of the elements down to the second order
    """
    all_list = []
    for row in list_2:
        for col in row:
            all_list.append(col)
    return all_list


def test_magic():
    square = make_int(get_square())
    magic_list = list()
    magic_list.append(test_square(square))
    magic_list.append(test_same(un_list(sum_list(square))))
    magic_list.append(test_consecutive(square))
    if False in magic_list:
        magic = False
    else:
        magic = True
    return magic


def magic_square():
    test = test_magic()
    if test:
        out = "That is a magic square!"
    else:
        out = "That is not a magic square."
    return out


""" TEST ROUTINES """

"""print(get_square())"""

"""print(make_int(get_square()))"""

"""test1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
print(test_square(test1))
test2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3, 4]]
print(test_square(test2))"""

"""test1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
print(test_rows(test1))
test2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3, 4]]
print(test_rows(test2))"""

"""print(sum_columns([[1, 2, 3], [1, 2, 3], [1, 2, 3]]), 'One more time!')"""

"""print(test_same([1, 1, 1]))
print(test_same([1, 1, 2]))
print(test_same([1, 2, 1]))
print(test_same([2, 1, 1]))"""

"""print(sum_rows([[1, 2, 3], [1, 2, 3], [1, 2, 3]]), "Bruce Dickinson would be proud!")
print(sum_rows([[1, 2, 3], [1, 2, 4], [1, 2, 5]]))"""

"""print(sum_diagonals([[1, 2, 3], [1, 2, 4], [1, 2, 5]]))"""

"""test1 = sum_diagonals([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
test2 = sum_diagonals([[1, 2, 3], [1, 2, 4], [1, 2, 5]])
print(test_same(test1))
print(test_same(test2))"""

"""print(test_consecutive([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
print(test_consecutive([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))"""

"""print(un_list([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))"""

print(test_magic())










