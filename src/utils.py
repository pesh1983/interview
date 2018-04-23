"""Common utility functions."""
import time
from functools import wraps


def timed(title):
    """Decorate function and print its execution time to stdout.

    :param title: Title to be print before execution time output.
    :return: Decorated function.
    """
    def decorator(func):
        """Decorator.

        :param func: Function to be decorated.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Wrap decorated function.

            :param args: Positional arguments to be passed to original
            function.
            :param kwargs: Keyword arguments to be passed to original
            function.
            :return: Result execution of original function.
            """
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
