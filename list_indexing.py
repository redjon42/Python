"""
winners= ['Jane', 'Bob', 'Naru', 'Simone']
prizes = ['1st', '2nd', '3rd', '4th']
write a segment of code to ask the user for a name, and see if the name is in the list of winners.
If it is, print the position plus one

E.G.
Name:  Jane
Jane got 1st prize!
or
name:  Sam
Sam did not get a prize.

"""


def get_index(some_name, some_list):
    if some_name in some_list:
        i = some_list.index(some_name)
    else:
        i = "F"
    return i


def get_name():
    name = input("Name: ")
    return name


def index_list(index, some_list):
    value = some_list[index]
    return value


def index_in_list(key_list, val_list):
    name = get_name()
    key_id = get_index(name, key_list)
    if key_id == "F":
        print("{} did not get a prize.".format(name))
    else:
        place = index_list(key_id, val_list)
        print("{} got {} prize".format(name, place))


winners= ['Jane', 'Bob', 'Naru', 'Simone']
prizes = ['1st', '2nd', '3rd', '4th']

index_in_list(winners, prizes)
