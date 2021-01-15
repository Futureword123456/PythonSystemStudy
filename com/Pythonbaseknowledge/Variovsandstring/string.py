# -*- coding: utf-8 -*-
# @Time : 2020/12/30 0030 14:20
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : string.py
# 字符串的创建
str1 = "hello world!"
str2 = 'Nice to meet you'
str3 = 'I told my friend" she is besutiful"'
str4 = str1 + str2
print(str4)

str5 = "MF" + str(8765)
print(str5)

# 大小写转换
str7 = "baw"
print(str7.upper())  # 小写转换为大写用upper()
print("nmw".upper())

print("MSJ".lower())

print("how are you!".capitalize())  # 首字母大写
print("michale jaskson sam".title())  # 人名首字母大写
print("ansHGD".swapcase())  # 大写部分变小写，小写部分变大写

print("{} {} you".format("I", "LOVE"))

# 制表符与换行符
table = "姓名\t性别\t年龄\n赵四\t男\t\t42"
print(table)
# 删除空白
space_str = "      Hello world   "
print(space_str)

lstr = len(space_str)
print(lstr)
# 字符串除去空格
nospace_str = space_str.strip()
print(nospace_str)

print(len(nospace_str))

# 字符串的查找(从零开始的)
source = "Nice to meet you, i need your  help!!"
index = source.find("ee")
print(index)
inexist = "ee" in source
print(inexist)
# 字符串替换
str8 = "this is string example...wow!!! this is really string"
pstr8 = str8.replace("is", "was")
print(pstr8)
pstr8 = str8.replace("is", "was", 3)
print(pstr8)




