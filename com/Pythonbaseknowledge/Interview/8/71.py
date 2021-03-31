# -*- coding: utf-8 -*-
# @Time : 2021/3/14 0014
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 71.py
"""利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。"""
score = int(input("请输入一个分数:"))
if score>=90:
    grade = 'A'
elif 60 <= score < 89:
    grade ='B'
else:
    grade = 'C'
print("分数{0}，等级{1}".format(score,grade))
if __name__ == "__main__":
    pass