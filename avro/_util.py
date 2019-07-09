import time

from timeit import default_timer as timer

import os

LOGGING_TIME = os.environ.get('LOGGING_TIME', False) or os.environ.get('LT', False)
INDENT = ''


def time_logger(func):
    def time_and_execute(*args, **kwargs):
        start = timer()

        global INDENT

        if LOGGING_TIME:
            print(f'{INDENT}<{func.__name__}')
            INDENT += '|   '

        result = func(*args, **kwargs)

        if LOGGING_TIME:
            INDENT = INDENT[:-4]
            print(f'{INDENT}{func.__name__}>: {timer() - start:.3f} s')

        return result

    return time_and_execute


if __name__ == '__main__':
    import os


    @time_logger
    def test1():
        time.sleep(1)


    test1()


    @time_logger
    def test2(x, y):
        return x + y


    print(test2(1, 2))


    @time_logger
    def test3(x, y):
        test2(x, y)
        test1()
        test4(x, y)


    @time_logger
    def test4(x, y):
        test2(x, y)


    test3(1, 2)
