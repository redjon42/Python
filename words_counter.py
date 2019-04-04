
"""
Suppose you have a string of words.
Use the split function to make it into a list.  And then write a function called
word_counts  that takes a string and returns a dictionary of how many times each word appears in the string.
Syntax hints:   empty dictionary is { }.   add to a dictionary d with d[somekey] = somevalue.
Use d.get(somekey, defaultvalue) to get dictionary at key somekey with a default value of defaultvalue.
"""


def word_counts(word_string):
    """
    :param word_string: a raw string of words
    :return: count_dict: a dictionary of word frequencies
    """
    word_list = word_string.split()
    count_dict = {}
    for word in word_list:
        count = count_dict.get(word, 0)
        count += 1
        count_dict[word] = count
    return count_dict


def test_word_count():
    test_string_0 = "this is a string with no repetition"
    test_string_1 = test_string_0 + " this is a string with some repetition"
    print(word_counts(test_string_0))
    print(word_counts(test_string_1))


test_word_count()
