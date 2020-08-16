# -*- coding:utf-8 -*-

def cus_map(func,arr:list) -> list:
    result = []
    for item in arr:
        r = func(item)
        result.append(r)
    return result

def test(i):
    return i**2

if __name__ == '__main__':
    result = cus_map(test,range(10))
    print(result)