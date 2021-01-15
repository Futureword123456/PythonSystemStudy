# -*- coding: utf-8 -*-
# @Time : 2021/1/3 0003 14:32
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample4.py
# 综合训练血压评估
high = input("请输入你测量的高压值:")
low = input("请输入你输入的低压值:")
high = int(high)
low = int(low)
# if (60 < low < 90) and (90 < high < 140):
#     print("你的血压正常，请继续保持健康生活")
# else:
#     print("你的血压出现异常，请尽快就医")
if not((low <= 60 or low >= 90) or (high >= 140 or high <= 90)):
    print("你的血压正常，请继续保持健康生活")
else:
    print("你的血压出现异常，请尽快就医")

