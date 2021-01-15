# -*- coding: utf-8 -*-
# @Time : 2021/1/10 0010 15:07
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample8.py
emp_list = []

while True:
    info = input("请输入员工信息:")
    if info == "":
        break
    info_list = info.split(",")
    if len(info_list) != 3:
        print("输入格式有不对，请重新输入！")
        continue
    emp_list.append(info_list)
    for i in emp_list:
        print("姓名:{n},年龄:{a},工资:{s}".format(n=i[0], a=i[1], s=i[2]))
