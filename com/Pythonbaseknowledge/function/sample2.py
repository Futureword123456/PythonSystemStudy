# -*- coding: utf-8 -*-
# @Time : 2021/1/13 0013 16:50
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample2.py
# 函数的形参与实参
# 参数就是函数的输入数据，在函数运行时，根据参数的不同执行不同的代码


def print_verse(verse_name, is_show_title, is_show_dynasty):
    # 函数的定义并实现（形参）
    # 函数体
    if verse_name == "静夜思":
        if is_show_title:
            print("静夜思-李白")
        if is_show_dynasty:
            print("唐朝")
        print("床前明月光")
        print("疑是地上霜")
        print("举头望明月")
        print("低头思故乡")
    elif verse_name == "再别康桥":
        if is_show_title:
            print("再别康桥-徐志摩")
        if is_show_dynasty:
            print("唐朝")
        print("轻轻的我走了")
        print("正如我轻轻的来")
        print("挥一挥手")
        print("不带走一片云彩")


print_verse("静夜思", True, False)  # 函数的调用（实参）
print()
print_verse("再别康桥", True, True)
