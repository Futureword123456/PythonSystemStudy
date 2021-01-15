# -*- coding: utf-8 -*-
# @Time : 2021/1/5 0005 17:19
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample4.py
# break的使用

i = 0
while i < 3:
    moblie = input("请输入你要查询的手机号：")
    i = i + 1
    if moblie == "1333333333":
        print("你的花费为158元")
        break
print("感谢你的来电")
