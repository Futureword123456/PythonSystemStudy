# -*- coding: utf-8 -*-
# @Time : 2021/1/13 0013 17:03
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample3.py
# 函数的返回值,参数是函数的输入数据，而返回值则是函数的输出结果
# return不是必须的，但是return语句后，函数将中断
# 1、为参数设置默认值。只需在形参后增加=具体在 即可
# 2、


def calc_exchange_rate(amt, source='CNY', target="USD"):
    if source == 'CNY' and target == "USD":
        reslut = amt / 6.7516
        # print("转换后结果是{}".format(reslut))
        return reslut
    elif source == "CNY" and target == "EUR":
        result = amt / 7.7512
        return result


r = calc_exchange_rate(100)
print(r)


# 2、以形参形式传参（关键字传参）
def health_check(name, age, height, weight, hr, lbp, glu):
    print("您的健康状况良好")


health_check(name='张三', age=32, weight=85, height=186, hr=70, lbp=120, glu=4.3)  # 传参加上参数名


# 混合形式传参
# *代表后面所有传参必须要用关键字传参
def health_check1(name, age, *, height, weight, hr, lbp, glu):
    print("您的健康状况良好")


health_check1('张三', 32, weight=85, height=186, hr=70, lbp=120, glu=4.3)
