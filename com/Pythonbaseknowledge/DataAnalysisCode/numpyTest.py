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
    np_lst = np.array(lst, dtype=np.float16)
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
    # 两行4列
    print(np.zeros([2, 4]))
    # 三行五列的列表
    print(type((np.ones([3, 5]))))
    print('Rand:')
    # 2行4列随机数
    print(np.random.rand(2, 4))
    print(np.random.rand())
    print('RandInt:')
    print(np.random.randint(2, 10, 3))
    print('Randn:')
    # 正态随机数
    print(np.random.randn(2, 4))
    print('Choice:')
    print(np.random.choice([1, 3, 5, 9]))
    print('Beta:')
    print(np.random.beta(1, 5, 50))
    print(np.arange(1, 13).reshape([3, 4]))
    lst = np.arange(1, 11).reshape([2, -1])
    print('=============================')
    print('exp')
    print(np.exp(lst))
    print('exp2')
    print(np.exp2(lst))
    print('sqrt')
    print(np.sqrt(lst))
    print('sin')
    print(np.sin(lst))
    print('log')
    print(np.log(lst))

    lst = np.array(
        [
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8]
            ],
            [
                [5, 8, 6, 4],
                [6, 9, 8, 2]
            ],
            [
                [8, 23, 12, 14],
                [9, 10, 11, 12]
            ]
        ]
    )
    print(lst.sum(axis=0))


if __name__ == "__main__":
    main()
