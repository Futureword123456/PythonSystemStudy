# -*- coding: utf-8 -*-
# @Time : 2021/1/25 0025
# @Author : yang
# @Email : 2635681517@qq.com
# @File : test_img.py
# 下载html
# 写正则规则
# 找到img标签
# 找到src
# <img class="" src = "" xx="">
# <img.+src=\".+\".+>
import re


def test_img():
    """"使用正则表达式找到图片的地址"""
    # 读取html
    with open('img.html', encoding='utf-8') as f:
        html = f.read()
        # print(html)
        # 准备正则
        p = re.compile(r'<img.+?src=\"(?P<src>.+?)\".+?>', re.M | re.I)
        # 使用findall找到图片的列表
        list_img = p.findall(html)
        # print(len(list_img))
        for lists in list_img:
            print(lists.replace('&amp;', '&'))
        # 使用urllib，request保存


if __name__ == "__main__":
    test_img()
