# -*- coding: utf-8 -*-
# @Time : 2021/3/10 0010
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 53.py
"""Python 计算字典值之和"""

key_value = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
sum = 0
for i in key_value:
    """i是key"""
    v = key_value[i]
    """v是value"""
    # print(v)
    sum = sum + v
print(sum)
if __name__ == "__main__":
    pass
