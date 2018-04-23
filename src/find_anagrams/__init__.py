"""Task3.

Implementation of a function that finds anagrams of given word in given list
of words.
"""
from array import array
from collections import defaultdict
from functools import partial


def find_anagrams(word, words):
    """Find anagrams of given word in given list of words.

    :param word: A word to which anagrams needs to be found.
    :param words: A list of words that may or may not contain anagrams for
    the given word.
    :return: A list of anagrams if any found.
    """
    # prepare storage with data related to words
    storage = prepare_storage_with_words(words)
    # get indexes of anagrams related to parameters of given word
    letters_amount = len(word)
    indexes = storage[letters_amount][''.join(sorted(word.lower()))]
    # gather words from original list and return in required format
    return [words[idx] for idx in indexes]


def prepare_storage_with_words(words):
    """Prepare a storage with given words for fast lookup of anagrams.

    It gets given list of words and generates the following structure:

    {
        <amount of letters in words>: {
            <sorted sequence of letters of words>: [
                <index of a word with these parameters in given list>,
                ...
            ]
            ...
        }
        ...
    }
    :return: The structure described above.
    """
    result = defaultdict(partial(defaultdict, lambda: array('L')))
    for idx, item in enumerate(words):
        letters_amount = len(item)
        sorted_letters = ''.join(sorted(item.lower()))
        result[letters_amount][sorted_letters].append(idx)

    return result
