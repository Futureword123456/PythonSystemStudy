# -*- coding: utf-8 -*-
# @Time : 2021/1/22 0022
# @Author : yang
# @Email : 2635681517@qq.com
# @File : test_range.py


def use_range():
    """"python内置的range函数"""
    for i in range(5, 10):
        print(i)


class IterRange(object):
    """使用迭代器来模拟range函数"""

    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def __next__(self):
        self.start += 1
        if self.start >= self.end:
            raise StopIteration
        return self.start

    def __iter__(self):
        return self


class GenRange(object):
    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def get_num(self):
        while True:
            if self.start >= self.end-1:
                break
            self.start += 1
            yield self.start


if __name__ == "__main__":
    # use_range()
    it = IterRange(5, 10)
    # print(it.__next__())
    # print(it.__next__())
    # print(it.__next__())
    # print(it.__next__())
    # l = list(it)
    # print(l)
    gen = GenRange(5,10).get_num()
    print(list(gen))