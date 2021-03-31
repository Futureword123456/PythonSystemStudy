# -*- coding: utf-8 -*-
# @Time : 2021/3/10 0010
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 52.py
"""Python 按键(key)或值(value)对字典进行排序"""


def dictionairy():
    # 声明字典
    key_value = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
    # 初始化
    # sorted(key_value) 返回重新排序的列表
    for i in sorted(key_value):
        print("排序后是({0},{1})".format(i, key_value[i]))

    for i in sorted(key_value.items()):
        print(i)

    # for i in sorted(key_value.values(),lambda kv:(kv[1], kv[0]):

    print("按值(value)排序:")
    print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))


if __name__ == "__main__":
    dictionairy()
