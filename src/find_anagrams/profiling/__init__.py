"""A module for performance testing of find anagrams function."""
import os


def read_dictionary():
    """Read words from a file 'dictionary.txt' and return a list of words.

    The file contains around 479k words. It is obtained from
    https://github.com/dwyl/english-words and is used as sample data.
    :return: A list of words read from a file.
    """
    cur_path = os.path.dirname(__file__)
    with open(os.path.join(cur_path, 'dictionary.txt')) as dict_file:
        result = dict_file.read().split()
    return result
