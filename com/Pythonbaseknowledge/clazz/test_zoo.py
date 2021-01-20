# -*- coding: utf-8 -*-
# @Time : 2021/1/20 0020
# @Author : yang
# @Email : 2635681517@qq.com
# @File : test_zoo.py

"""猫科动物"""


class Cat(object):
    """猫科动物"""
    tag = "我是家猫"

    def __init__(self, age, name, sex=None):
        self.name = name
        self.sex = sex
        self.__age = age  # 私有成员

    def set_age(self, age):
        """设置猫的年龄"""
        self.__age = age

    def show_info(self):
        """显示猫的信息"""
        rest = '我是{0},今年{1},我的性别是{2}'.format(self.name, self.__age, self.sex)
        print(rest)

    def eat(self):
        """猫吃的信息"""
        print("猫喜欢吃鱼")

    def __call__(self, *args, **kwargs):
        """猫会叫"""
        print("猫会叫")

    def catch(self):
        """猫会捉老鼠"""
        print("猫能抓老鼠")


class Tiger(object):
    pass


if __name__ == "__main__":
    cat_balck = Cat(age=1, sex='boy', name='hello')
    # cat_balck.show_info()
    # cat_balck.set_age(5)
    # cat_balck.show_info()
    # cat_balck.catch()
    # cat_balck.eat()
    print(cat_balck.name)
    cat_balck.name = "123"
    cat_balck.sex = "9"
    # cat_black.__age = 6  # 无法操作私有变量
    cat_balck.show_info()

    print("========================")
    ti = Tiger()

    # 类的实例化判断
    print(isinstance(cat_balck, Cat))
    print(isinstance(ti, Tiger))
