# -*- coding: utf-8 -*-
# @Time : 2021/3/13 0013
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 68.py
"""计数排序"""


def countSort(arr):
    output = [0 for i in range(256)]

    count = [0 for i in range(256)]

    ans = ["" for _ in arr]

    for i in arr:
        count[ord(i)] += 1

    for i in range(256):
        count[i] += count[i - 1]

    for i in range(len(arr)):
        output[count[ord(arr[i])] - 1] = arr[i]
        count[ord(arr[i])] -= 1

    for i in range(len(arr)):
        ans[i] = output[i]
    return ans


if __name__ == "__main__":
    arr = "wwwrunoobcom"
    ans = countSort(arr)
    print("字符数组排序 %s" % ("".join(ans)))
