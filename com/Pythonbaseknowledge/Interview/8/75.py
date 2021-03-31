# -*- coding: utf-8 -*-
# @Time : 2021/3/14 0014
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 75.py
height = 100
tn = []
lst = []
net = 0
sun = 0
mind = 0
for _ in range(1, 11):
    height = height / 2
    sun = sun + height
    tn.append(sun)

print(tn)
lst = tn[-1]
print(lst + 100)

if __name__ == "__main__":
    pass
