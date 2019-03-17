
def make_table(in_str):
    """
    :param in_str: string
    :return: a printable table of line number, then character
    """
    out_list = []
    for i in in_str:
        index = i
        char = in_str[i]
        newline = "\n"
        out_list.append([index, char, newline])
    return out_list


# Main Routine


my_str = "Five!"
for line in make_table(my_str):
    print('{:=4}'.format(line[0]), '{:=4}'.format(line[1]), line[2])

