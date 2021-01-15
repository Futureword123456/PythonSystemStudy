# -*- coding: utf-8 -*-
# @Time : 2020/12/30 0030 10:28
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : casher.py
print("欢迎使用收银台程序")
goods = input("请输入商品名称")
price = input("请输入商品单价")
num = input("请输入商品数量")  # input函数返回是字符串
total = float(price) * 0.9 * float(num)
alipay_total = total * 0.95
print("商品的数量是" + str(goods))
print("商品的总价是" + str(total))
print("使用支付宝支付" + str(alipay_total))
