# -*- coding: utf-8 -*-
# @Time : 2021/1/13 0013 19:16
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample5.py
# 函数的使用技巧
# 1、序列传参


def calc(a, b, c):
    return (a + b) * c


v = []
a = {1, 2, 3}
b = {"a": 20, "b": 30, "c": 40}
for i in b:
    v = b[i]
    print(v, end=",")
k = list(a)
print(k)
l = [1, 5, 10]  # 序列传参
print(calc(l[0], l[1], l[2]))
print(calc(**b))


# 2、字典传参（常用）

def health_check(name, age, height, weight, hr, hbp, lbp, glu):
    print(name)
    print(age)
    print("您的健康状况良好")


param = {"name": "张三", "height": 178, "age": 32, "weight": 85.5, "hr": 70, "hbp": 120, "lbp": 80, "glu": 4.3}
health_check(**param)  # 字典传参用**加上字典名 即可


# 3、返回值包含多个数据
def get_detail_info():
    dict1 = {
        "employee": [
            {"name": "张三", "salary": 1800},
            {"name": "李四", "salary": 2000}
        ],

        "device": [
            {"id": "859551", "title": "XX笔记本"},
            {"id": "5656648", "title": "XX台式机"},
        ],
        "asset": [{}, {}],
        "project": [{}, {}]

    }
    return dict1


print(get_detail_info())
d1 = get_detail_info()
# 获取第一个员工的工资
sal = d1.get("employee")[0].get("salary")
print(sal)
# 获取第二个员工的信息
sal1 = d1.get("employee")[1]
print(sal1)
# 获取device的信息
de = d1.get("device")[0].get("id")
print(de)
