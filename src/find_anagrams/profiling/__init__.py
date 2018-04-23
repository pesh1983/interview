"""A module for performance testing of find anagrams function."""
import os


def read_dictionary():
    """Read words from a file 'dictionary.txt' and return a list of words.

    :return: A list of words read from a file.
    """
    cur_path = os.path.dirname(__file__)
    with open(os.path.join(cur_path, 'dictionary.txt')) as dict_file:
        result = dict_file.read().split()
    return result
