# -*- coding: utf-8 -*-
# @Time : 2021/1/22 0022
# @Author : yang
# @Email : 2635681517@qq.com
# @File : test_iter.py

# l = [1, 2, 3, 4, 5]
# for i in l:
#     print(i)
#
# ll = iter(l)
# print(ll)
# print(dir(ll))
# print(ll.__next__())
# print(next(ll))


# class PowNumber(object):
#     """迭代器
#     生成1，2，3，4，5数的平方
#     """
#     value = 0
#
#     def __next__(self):
#         self.value += 1
#         if self.value > 10:
#             raise StopIteration
#         return self.value * self.value
#
#     def __iter__(self):
#         return self

def seq(value=1):

    va = value * value
    return va


if __name__ == "__main__":
    for i in range(1, 5):
        print(seq(int(i)))
    # pow = PowNumber()
    # print(pow.__next__())
    # print(pow.__next__())
    # print(pow.__next__())
    # print(pow.__next__())
    # print(pow.__next__())
    # print(pow.__next__())
    # print(next(pow))
    #     # print(next(pow))
    #     # print(next(pow))
    #     # print(next(pow))

    # for i in pow:
    #     print(i,end=",")
