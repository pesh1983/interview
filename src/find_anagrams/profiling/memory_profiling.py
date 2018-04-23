"""Memory profiling."""
from memory_profiler import profile

from find_anagrams import prepare_storage_with_words
from find_anagrams.profiling import read_dictionary

dictionary = read_dictionary()


@profile
def profile_memory_of_storage():
    """Create storage."""
    prepare_storage_with_words(dictionary)


profile_memory_of_storage()
