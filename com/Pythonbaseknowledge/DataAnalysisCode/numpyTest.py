# -*- coding: utf-8 -*-
# @Time : 2021/3/31 0031
# @Author : yang
# @Email : 2635681517@qq.com
# @File : numpyTest.py
import numpy as np


def main():
    lst = [[1, 2, 3], [3, 4, 5]]
    print(lst)
    np_lst = np.array(lst)
    print(np_lst)
    np_lst = np.array(lst,dtype=np.float16)
    print(np_lst)
    # 指明形状(2, 3)
    print(np_lst.shape)
    # 维度
    print(np_lst.ndim)
    # 数据类型
    print(np_lst.dtype)
    # 每个元素的大小
    print(np_lst.itemsize)
    # 总数
    print(np_lst.size)


if __name__ == "__main__":
    main()
