# -*- coding: utf-8 -*-
# @Time : 2021/1/20 0020
# @Author : yang
# @Email : 2635681517@qq.com
# @File : test_normal.py


class BaseCat(object):
    """猫科动物的基础类"""
    tag = "猫科动物"

    def __init__(self, name):
        self.name = name  # 猫都有名称

    def eat(self):
        """ 猫吃东西 """
        print('猫都要吃东西')


class ProtectedMixin(object):
    """ 受保护的类 """

    def protected(self):
        print('我是受省份级别保护的')


class CountryProtectedMixin(object):
    def protected(self):
        print('我是受国家级别保护的')


class Tiger(BaseCat, ProtectedMixin,CountryProtectedMixin):
    """老虎"""

    def eat(self):
        """重写父类的方法"""
        super(Tiger, self).eat()
        print("我还吃肉")


class panda(BaseCat, ProtectedMixin,CountryProtectedMixin):
    """熊猫"""
    pass


class PerCat(BaseCat, ProtectedMixin,CountryProtectedMixin):
    """宠物猫"""

    def eat(self):
        super(PerCat, self).eat()
        print("我还吃猫粮")

    pass


class DuanCat(PerCat):
    """短毛猫"""

    def eat(self):
        super(DuanCat, self).eat()
        print("吃零食")


class HuaCat(PerCat):
    """华南猫"""
    print('我啥都吃5')


if __name__ == "__main__":
    # 实例化中华田园猫
    # cat = DuanCat('小黄')
    # cat.eat()

    # print("==================")
    # cat_d = HuaCat('小辉')
    # cat_d.eat()

    panda = panda('卧龙小熊猫')
    panda.eat()
    panda.protected()

    tiger = Tiger('华南虎')
    tiger.protected()

    print('------=================-------')
    # 验证子类信息
    # print(issubclass(panda, ProtectedMixin))
    # print(issubclass(panda, BaseCat))
