"""Performance tests a function that finds anagrams."""
import os

from find_anagrams import find_anagrams
from utils import timed

# read words from file
# the file contains around 479k english words
cur_path = os.path.dirname(__file__)
with open(os.path.join(cur_path, 'dictionary.txt')) as dict_file:
    dictionary = dict_file.read().split()

# a word to find anagrams for
word = 'rat'


@timed('{} len={}'.format(word, len(word)))
def find_anagrams_in_dictionary():
    """Find anagrams."""
    return find_anagrams(word, dictionary)


print(find_anagrams_in_dictionary())
