# -*- coding:utf-8 -*-

# list 容器序列  可变序列
l = [1]
l.append("2")
l.append(3.6)
l.append(False)
l.append(['apple', 'banana', 'orange'])
print(l)

# tuple 容器序列 不可变序列
t = (1,3.5,False,l,'test')
print(type(t))
print(t)
# 可变的部分是 list
l.pop(len(l)-1)
print(t)

# str 扁平序列 不可变序列
s = 'welcome to china'
print(s.upper())
print(s)
print(type(s[1:5]))

# dict 容器序列  可变序列
d = {'name':'chenh','age':25,'hobby':['coding','coding','coding']}
print(type(d))


# deque容器序列，可变序列
from collections import deque
d = deque([i for i in range(5)])
d.append(6.1)
d.append(False)
d.appendleft(l)
print(d)
