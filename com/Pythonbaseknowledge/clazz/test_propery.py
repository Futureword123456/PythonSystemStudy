# -*- coding: utf-8 -*-
# @Time : 2021/1/20 0020
# @Author : yang
# @Email : 2635681517@qq.com
# @File : test_propery.py


class PetCat(object):
    """家猫"""

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # 描述符

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            print('年龄只能是整数')
            return 0
        if value < 0 or value > 100:
            print('年龄只能介于0-100之间')
            return 0
        self.__age = value

    @property
    def show_info(self):
        """ 显示猫的信息 """
        return '我叫：{0}，今年{1}岁'.format(self.name, self.age)

    def __str__(self):
        return "我的对象是:{0}".format(self.name)


if __name__ == '__main__':
    cat_black = PetCat('小黑', 2)
    # print(cat_black)
    cat_black.age = 6
    rest = cat_black.show_info
    print(rest)
