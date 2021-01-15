# -*- coding: utf-8 -*-
# @Time : 2021/1/13 0013 10:02
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample6.py
# 序列类型的互相转换
l1 = ['a', 'b', 'c']
t1 = ('d', 'e', 'f')
s1 = 'abc123'
s2 = 'abc,123'
s3 = 123456
r1 = range(1, 10)
# list()--转换为列表
l2 = list(t1)
print(l2)
print(list(s1))
print(list(str(s3)))
print(list(str(1223)))
# split()函数是切割结果为列表
print(s2.split(","))

print(list(r1))
# tuple()转换为元组
print(tuple(l1))
print(tuple(s1))
print(tuple(s2.split(",")))
print(tuple(r1))

# str()用于将单个数据转换为字符串、join()对列表进行链接
print(str(l1))
print(",".join(l1))
print("|".join(t1))  # join必须要求所有元素都是字符串
s4 = ""  # 将包含数字的序列输出
for i in r1:
    s4 += str(i)
print(s4)

