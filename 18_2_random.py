
import random as rm
"""
exec(open("18_2_random.py").read())
"""

"""
Use the random module.  
Write a function that counts by ones until 
a random value from 1 to 100 is greater than 90.  
Print out that count. 
"""


def get_guess(range_list):
    """
    :param range_list: a 2-element list of low and high ranges
    :return: a random number in that range
    """
    low = range_list[0]
    high = range_list[1]
    guess = rm.randrange(low, high)
    return guess


def test_get_guess():
    test_list = [1, 100]
    for n in range(1, 21):
        print(get_guess(test_list), end=', ')


def top_percentile(range_list=[1, 100], percentile=.9):
    """
    :param range_list: a 2-element list of low and high ranges
    :param percentile: a float of percentile to be tested
    :return: the number of iterations it took to get a number in the top percentile
    """
    high = range_list[1]
    top = (percentile * high)//1

    n = 0
    done = False
    while not done:
        rand_int = get_guess(range_list)
        if rand_int > top:
            n += 1
            done = True
        else:
            n += 1
    return n


def test_top_percentile():
    for n in range(1, 21):
        print(top_percentile(), end=', ')



