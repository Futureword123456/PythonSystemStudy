# -*- coding: utf-8 -*-
# @Time : 2021/1/22 0022
# @Author : yang
# @Email : 2635681517@qq.com
# @File : test_except.py

def test_div(num1, num2):
    """除数为零"""
    return num1 / num2


def test_file():
    """读取文件"""
    try:
        f = open('test.txt', 'r', encoding='utf-8')
        rest = f.read()
        print(rest)
    except Exception as err:
        print("error")
        print(err)
    finally:
        f.close()


if __name__ == "__main__":
    # try:
    #     rest = test_div(5, 0)
    #     print(rest)
    # except (ZeroDivisionError, TypeError) as err:
    #     print("报错了")
    #     print(err)
    # except TypeError:
    #     print('报错了，请输入数字')
    test_file()
