# -*- coding: utf-8 -*-
# @Time : 2021/1/1 0001 20:21
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : string_format.py

name = "长江大学"
age = 23
height = 163.6
str1 = "我是" + name + ",今年" + str(age) + "岁，身高" + str(height)
print(str1)
str2 = "我叫{0},我在{1},身高{3},今年{2}".format(name, "3-2", age, height)
print(str2)
str3 = "我叫{p1},我在{p2},身高{p4},今年{p3}".format(p1=name, p2="6-9", p3=age, p4=height)
print(str3)

# 数字的格式化输出
num = 12354.7998655
str4 = format(num, '0.4f')
print(type(str4))
print(str4)
account = "6584526786"
amt = 12345678
str5 = format(amt, "0,.2f")
str6 = "请你向" + account + "账户转账￥" + str5 + "元"
print(str6)
# 在字符串格式化输出时，如果要格式化输出的数字，则需要在{}内增加:前缀,之后数字格式语句
str7 = "请你向{}账户转账￥{:0,.3f}元".format(account, amt)
print(str7)
# 早期的字符串格式化
# 我叫张三，今年30岁，体重87.5
name = "张三"
age = 30
weight = 87.5
str8 = "我叫%s,今年%d岁，体重%.2f公斤" % (name, age, weight)
print(str8)
