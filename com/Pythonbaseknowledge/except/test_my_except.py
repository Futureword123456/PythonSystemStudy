# -*- coding: utf-8 -*-
# @Time : 2021/1/22 0022
# @Author : yang
# @Email : 2635681517@qq.com
# @File : test_my_except.py

# 自定义异常微信异常接口实践


class ApiException(Exception):
    """自定义异常"""
    err_code = ''
    err_msg = ''
    """初始化函数__init__()"""

    def __init__(self, err_code=None, err_msg=None):
        """"err_code"""
        """err_msg"""
        self.err_code = self.err_code if self.err_code else err_code
        self.err_msg = self.err_msg if self.err_msg else err_msg

    def __str__(self):
        return 'Error:{0}-{1}'.format(self.err_code, self.err_msg)


class InvalidCtrlExecpt(ApiException):
    """ 当参数不合法时触发
        40001	invalid credential	不合法的调用凭证
    """
    err_code = '40001'
    err_msg = '不合法的调用凭证'


class BadPramsExecption(ApiException):
    """参数不正确"""
    err_code = '40002'
    err_msg = '两个参数必须都是整数'


def div(num1, num2):
    """除法的实现"""
    # 两个数必须为整数
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise BadPramsExecption()
    if num2 == 0:
        raise ApiException('4000000', '除数不能为零')
    return num1 / num2


if __name__ == "__main__":
    try:
        rest = div(5, 0)
        print(rest)
    except BadPramsExecption as e:
        print("==================")
        print(e)
    except ApiException as err:
        print("报错了")
        print(err)
