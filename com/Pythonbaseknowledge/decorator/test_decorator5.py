# -*- coding: utf-8 -*-
# @Time : 2021/1/22 0022
# @Author : yang
# @Email : 2635681517@qq.com
# @File : test_decorator5.py


def f(self):
    print("{0}要吃东西".format(self.name))
    print("456")


def eat(cls):
    """吃东西的类"""
    # cls.eat = lambda self: print("{0}要吃东西".format(self.name))
    cls.eat = f
    return cls


@eat
class Cat(object):
    """猫"""

    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    cat = Cat('小黑')
    cat.eat()
