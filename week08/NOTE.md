学习笔记

### 作用域
- L-Local(function)；函数内的名字空间
- E-Enclosing function locals；外部嵌套函数的名字空间（例如closure）
- G-Global(module)；函数定义所在模块（文件）的名字空间
- B-Builtin(Python)；Python 内置模块的名字空间

作用范围依次递增

### 闭包：内部函数对外部函数作用域里变量的引用（非全局变量）则称内部函数为闭包
```shell script
# nonlocal访问外部函数的局部变量
# 注意start的位置，return的作用域和函数内的作用域不同
def counter2(start=0):
    def incr():
        nonlocal start
        start+=1
        return start
    return incr
c1=counter2(5)
print(c1())
print(c1())

c2=counter2(50)
print(c2())
print(c2())
```

### 装饰器

类似于Java中的AOP,是保证不修改目标方法的前提下，对目标方法的一种增强。基于闭包的原理实现，最终调用的是内部函数
