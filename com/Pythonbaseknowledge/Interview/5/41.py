# -*- coding: utf-8 -*-
# @Time : 2021/3/8 0008
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 41.py
"""Python 清空列表"""

test_list = [1, 6, 3, 5, 3, 4]
test_list.clear()
# print(test_list)
for i in range(1,len(test_list)+1):
    test_list.pop(0)
print(test_list)
if __name__ == "__main__":
    pass
