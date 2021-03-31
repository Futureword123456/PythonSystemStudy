# -*- coding: utf-8 -*-
# @Time : 2021/3/7 0007
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 28.pysd
"""字符串判断"""
str1 = input("输入:")
print(str1.isalnum())  # 判断所有字符是否是数字或者字母
print(str1.isalpha())  # 判断所有字符是否都是字母
print(str1.isdigit())
print(str.islower(str1))  # 判断所有字符都是小写
print(str.isupper(str1))  # 判断所有字符都是大写
print(str.istitle(str1))  # 判断所有单词都是首字母大写，像标题
print(str1.isspace())
if __name__ == "__main__":
    pass
