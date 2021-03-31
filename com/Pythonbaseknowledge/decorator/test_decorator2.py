# -*- coding: utf-8 -*-
# @Time : 2021/1/21 0021
# @Author : yang
# @Email : 2635681517@qq.com
# @File : test_decorator2.py


def log(func):
    """记录函数执行的日志"""

    def wrapper():
        print("start...")
        func()
        print("end...")

    return wrapper


def log_in(func):
    """ 记录函数执行的日志 """

    def wrapper():
        print('开始进入...')
        func()
        print('结束..')

    return wrapper


@log
def hello():
    """简单功能模拟"""
    print("hello world")


@log
@log_in
def test():
    print('test ..')


if __name__ == "__main__":
    # hello()
    test()
