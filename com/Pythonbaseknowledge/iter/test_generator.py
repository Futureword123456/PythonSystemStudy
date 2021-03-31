# -*- coding: utf-8 -*-
# @Time : 2021/1/22 0022
# @Author : yang
# @Email : 2635681517@qq.com
# @File : test_generator.py


def pow():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


def pow_number():
    return (x * x for x in [1, 2, 3, 4, 5])


def pow_number2():
    for x in [1, 2, 3, 4, 5]:
        yield x * x


if __name__ == "__main__":

    # print(rest.__next__())
    # print(rest.__next__())
    # print(rest.__next__())
    # print(rest.__next__())
    # print(rest.__next__())
    # print(rest.__next__())
    # for i in rest:
    #     print(i)
    rest = pow_number()
    print(rest.__next__())
