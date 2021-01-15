# -*- coding: utf-8 -*-
# @Time : 2021/1/10 0010 14:35
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample7.py
# 嵌套列表
# [[姓名,年龄,工资],[姓名,年龄,工资],[姓名,年龄,工资],[姓名,年龄,工资],[姓名,年龄,工资]]

# 字符串:"姓名,年龄,工资" 例如："张三,30,20000"
# str1 = "张三,30,20000"
# # split用于把字符串切割为列表
# l = str1.split(",")
# print(l)
#
emp_list = []
while True:
    info = input("请输入员工信息:")
    if info == "":
        print("程序结束")
        break
    info_list = info.split(",")
    if len(info_list) != 3:
        print("输入格式不正确，请重新输入！")
        continue
    # print(info_list)
    emp_list.append(info_list)
    # print(emp_list)
    i = 0
    for emp in emp_list:
        if i == 2:
            print("\n")
        i += 1
        print("姓名:{n},年龄:{a},工资:{s}".format(n=emp[0], a=emp[1], s=emp[2]), end="")
