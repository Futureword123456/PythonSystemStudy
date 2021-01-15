# -*- coding: utf-8 -*-
# @Time : 2021/1/9 0009 10:13
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample2.py
# 列表的取值
list = ['张三', '赵六','李四', '王五', '赵六', '钱七', '孙八']
# print(list)
# zhaoliu = list[3]
# print(zhaoliu)
# 取值语法：变量=列表变量[索引值]
print(list)
print(list[3])  # 输出赵六
print(list[-3])
# 范围取值：列表变量=原列表变量[起始索引:结束索引]
# 在python列表范围取值是左闭右开
list1 = list[1:4]
print(list1)
print(list1[-1])  # 输出赵六最后一个数,用list1来进行运算
print(list1[1:3])
print(list1[0:2])
print(list1[0:1])
print(list1[1])
print(type(list1))
#列表的index函数用于获取元素的索引
zhaoliu = list.index('赵六')
print(zhaoliu) #返回第一次出的位置（正向的索引）

for i in list:
    #print("{}|".format(i), end="")

    print("|",i,end="")

