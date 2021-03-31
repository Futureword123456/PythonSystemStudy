# -*- coding: utf-8 -*-
# @Time : 2021/3/8 0008
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 42.py
"""Python 复制列表"""
test_list = [1, 6, 3, 5, 3, 4]
test_list1 = list(test_list)
# print(test_list1)
test_list2 = []
for i in range(1, len(test_list) + 1):
    test_list2.append(test_list[i - 1])
# print(test_list2)

print(test_list)
if __name__ == "__main__":
    pass
