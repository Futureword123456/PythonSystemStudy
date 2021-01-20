# -*- coding: utf-8 -*-
# @Time : 2021/1/20 0020
# @Author : yang
# @Email : 2635681517@qq.com
# @File : test_method.py


class Cat(object):
    tag = "猫科动物"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def breath():
        """呼吸"""
        print("猫都需要呼吸空气")

    @classmethod
    def show_info(cls, name):
        """显示猫的信息"""
        print("类的属性：{0},实例的属性:{1}".format(cls.tag, cls.name))
        return cls(name)
        cat = Cat(name)
        return cat


if __name__ == "__main__":
   # 通过类进行调用
    Cat.breath()
    cat = Cat('小黑')
    cat.breath()
    cat.show_info("小黄")



