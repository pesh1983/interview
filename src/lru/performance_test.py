import time
from functools import wraps

from lru import lru_cache


def timed(title):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()

            result = func(*args, **kwargs)

            print('{name} ({title}): {result_time}'.format(
                name=func.__name__,
                title=title,
                result_time=time.time() - start_time
            ))
            return result

        return wrapper

    return decorator


cache_sizes = (1000, 10000, 100000)

for size in cache_sizes:
    @lru_cache(size)
    def test_func(p1, p2):
        return p1 + p2


    @timed(size)
    def fill_cache():
        for idx in xrange(size):
            test_func(idx, idx + 1)


    fill_cache()


    @timed(size)
    def replace_cache():
        for idx in xrange(size):
            test_func(idx + 1, idx)


    replace_cache()
