"""Performance tests a function that finds anagrams."""
from find_anagrams import find_anagrams
from find_anagrams.profiling import read_dictionary
from utils import timed

dictionary = read_dictionary()

# a word to find anagrams for
word = 'rat'


@timed('{} len={}'.format(word, len(word)))
def find_anagrams_in_dictionary():
    """Find anagrams."""
    return find_anagrams(word, dictionary)


print(find_anagrams_in_dictionary())
