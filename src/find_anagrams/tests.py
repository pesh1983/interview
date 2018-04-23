"""Tests for LRU cache mechanism."""
from unittest import TestCase

from find_anagrams import find_anagrams


class TestFindAnagrams(TestCase):
    """Tests for LRU cache mechanism."""

    def test_find_anagrams_positive(self):
        """Test finding of anagrams in given words list."""
        for word, words, result in (
            ('Rat', ('TLDR', 'TAR', 'art', 'TBD'), ['TAR', 'art']),
            ('no_anagrams', ('1', 'dksdls', 'dd'), []),
        ):
            anagrams = find_anagrams(word, words)

            self.assertEqual(anagrams, result)
