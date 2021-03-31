# -*- coding: utf-8 -*-
# @Time : 2021/1/21 0021
# @Author : yang
# @Email : 2635681517@qq.com
# @File : test_decorator.py

def hello():
    """简单功能模拟"""
    print("hello world")


def hello_wrapper():
    """新的函数，包裹原来的hello"""
    print("进入hello()函数")
    hello()
    test()
    print("结束hello函数的执行")


def test():
    print("test...")


if __name__ == "__main__":
    # hello()
    hello_wrapper()
