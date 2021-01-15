# -*- coding: utf-8 -*-
# @Time : 2020/12/29 0029 20:24
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : elec_charge.py
print("欢迎使用电价计算器!")
elec_charge = 982
charge = (240 * 0.4883) + (400 - 240) * 0.5383 + (elec_charge - 400) * 0.7883
print("你本月的用电量为：" + str(elec_charge))  # 数字转换为字符串
print("你本月的电价是：" + str(charge))
