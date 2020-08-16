# -*- coding:utf-8 -*-
import time
import functools


def timer(func):

    @functools.wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        print(f'function name:{func.__name__}')
        print(f'start time :{start}')
        result = func(*args, **kwargs)
        print(f'execute result : {result}')
        end = time.time()
        print(f'end time :{end}')
        print(f'take time：{end - start}')
        return result

    return inner


@timer
def test():
    print("execute task .....")
    time.sleep(5)
    return 'hello world'


test()