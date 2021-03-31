# -*- coding: utf-8 -*-
# @Time : 2021/3/14 0014
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 72.py
"""输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数"""
c = input("输入一段字符:")
eng = 0
space = 0
num = 0
other = 0
for i in c:
    if i.isalpha():
        eng = eng + 1
    elif i.isspace():
        space = space + 1
    elif i.isdigit():
        num = num + 1
    else:
        other = other + 1
print("英文数量{0},空格数量{1},数字有{2},其他的有{3}".format(eng,space,num,other))
if __name__ == "__main__":
    pass
