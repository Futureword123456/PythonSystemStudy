# -*- coding: utf-8 -*-
# @Time : 2021/1/13 0013 14:33
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample5.py
# 生成式
lst1 = []
for i in range(10, 20, 2):
    lst1.append(i * 10)
print(lst1)

lst2 = [i * 10 for i in range(10, 20, 2)]
print(lst2)
# 生成式的语法:[被追加的数据 循环语句 循环或者判断语句]|{}
lst3 = [i * 10 for i in range(10, 20) if i % 3 == 0]
print(lst3)
for i in range(10, 20):
    if i % 2 == 0:
        lst3.append(i * 10)

lst4 = [i * j for i in range(1, 5) for j in range(1, 5)]
print(lst4)

for i in range(1,5):
    for j in range(1,5):
        lst4.append(i*j)
print(lst4)


#集合生成式
lst5 = ['张三','李四','王五']
dict1 = {i+1:lst5[i] for i in range(0,len(lst5))}
print(dict1)

for i in range(0,len(lst5)):
    dict1[i+1] = lst5[i]
print(dict1)

#集合生成式
set1 = {i*j for i in range(1,4) for j in range(1,4) if i==j}
print(set1)
re = {}
for i in range(1,4):
    for j in range(1, 4):
        if i == j:
            re = i*j
            list(set1).append(re)
            set1.add(i*j)
print(set1)
