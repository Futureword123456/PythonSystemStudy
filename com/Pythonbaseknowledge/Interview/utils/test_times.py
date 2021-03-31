# -*- coding: utf-8 -*-
# @Time : 2021/3/7 0007
# @Author : yang
# @Email : 2635681517@qq.com
# @File : test.py
import time


# 定义装饰器
def time_calc(func):
    def wrapper(*args, **kargs):
        start_time = time.time()
        f = func(*args, **kargs)
        exec_time = time.time() - start_time
        print("func.name:{}\texec_time:{}".format(func.__name__, exec_time))
        return f

    return wrapper
