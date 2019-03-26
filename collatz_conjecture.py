"""
Ask the user for an integer for number of iterations, say 5…
Find the smallest N that requires 5 or more iterations of the 3n + 1 program.
"""


def conjecture(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""
    count_list = []
    while n != 1:
        count_list.append(n)
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    return count_list


def get_num():
    x = input("Test for how many iterations? (5 or greater): ")
    x = int(x)
    return x


def smallest(num):
    n = 1
    while n < len(conjecture(num)):
        n += 1
    return n


def collatz():
    n = get_num()
    x = smallest(n)
    print("The smallest number that requires fewer than {} iterations is {}.".format(n, x))

collatz()

