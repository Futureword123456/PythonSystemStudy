# -*- coding: utf-8 -*-
# @Time : 2021/1/20 0020
# @Author : yang
# @Email : 2635681517@qq.com
# @File : test_class.py


class Cat(object):
    """猫科动物"""

    # 类的属性
    # 构造函数
    def __init__(self, name):
        # 实例化后的属性
        self.name = name
        pass

    # 类的属性
    tag = 'Cat base'

    # 析构函数
    def __del__(self):
        pass

    def eat(self):
        pass


class Tiger(Cat):
    pass
