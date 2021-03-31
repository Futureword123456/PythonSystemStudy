# -*- coding: utf-8 -*-
# @Time : 2021/1/21 0021
# @Author : yang
# @Email : 2635681517@qq.com
# @File : test_decorator3.py


def log(name=None):
    """记录函数执行日志"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            print("{0}.start...".format(name))
            print(args)
            print(kwargs)
            rest = func(*args, **kwargs)
            print('{0}.end..'.format(name))
            return rest

        return wrapper

    return decorator


@log()
def Hello():
    print("hello")


@log('test')
def test():
    print('test ..')


@log('from add')
def add(a, b):
    return a + b


if __name__ == "__main__":
    # Hello
    test()
    add(4, 5)
