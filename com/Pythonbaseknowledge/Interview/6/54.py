# -*- coding: utf-8 -*-
# @Time : 2021/3/10 0010
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 54.py
"""删除字典"""

key_value = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
key_value.pop(2)
print(key_value)
del key_value[1]
print(key_value)
if __name__ == "__main__":
    pass