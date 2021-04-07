# -*- coding: utf-8 -*-
# @Time : 2021/2/24 0024
# @Author : yang
# @Email : 2635681517@qq.com
# @File : test.py
# list_city = ['黔西南布依族苗族自治州']
# for i in list_city:
#     print(i)

# import matplotlib.pyplot as plt
#
# plt.plot([1, 50,5,10])
# plt.ylabel('some numbers')
# plt.show()

#
# list1 = {"key1", "key2", "key3"}
# list2 = {1, 2, 3}
# for x, y in zip(list1, list2):
#     # print("{0} {1}".format(x, y))
#     print(employee)

# zi = zip(list(list1), list(list2))
# key_value = dict(zi)
# print(key_value)

# for x, y in zip(list1, list2):
#     print(dict(x,y))
#     print("{0}--{1}".format(x, y))


from functools import reduce


def count(s):
    lst = str(s).split(',')
    sun = 0
    for i in lst:
        for j in i:
            if j.isdigit():
                sun += 1
    return sun


if __name__ == '__main__':
    sm1 = reduce(lambda x, y: count(x) + count(y), ["a123", "bcd1.12", 'sfd321'])
    print(sm1)
