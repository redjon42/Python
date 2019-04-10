"""
Suppose you have a list like
myList = [ 1, 4, 6, 9 ]
Notice that 1 + 4 is 5,   4 + 6 is 10,  and 6 + 9 is 15.
Produce this list given myList (of any length):
[5, 10, 15]
Write your function up and call it "sumListPairs"
(Advanced: you can do it with a list comprehension)


If you test with [1,1,1,1,1,1] you get [2,2,2,2,2]
If you test with [1,2,3] you get [3,5]
if you test with [0] or ['fred']  you get an error probably. Handle that gracefully with try / except

"""


def pair_sum(num_list):
    sum_list = list()
    for i in range(len(num_list)-1):
        sum_list.append(num_list[i] + num_list[i+1])
    return sum_list


def test_list(some_list):
    if len(some_list) < 2:
        return False
    else:
        for x in some_list:
            if isinstance(x, (int, float)):
                t = True
            else:
                return False
    return t


def run_pair_sum(num_list):
    if test_list(num_list):
        out = pair_sum(num_list)
    else:
        out = "Error: non-numeric or out of range."
    return out


test = [[1, 1, 1, 1, 1, 1], [1, 2, 3], [0], ['fred']]
for x in test:
    print(run_pair_sum(x))
