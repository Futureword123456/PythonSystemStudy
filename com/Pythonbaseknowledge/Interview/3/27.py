# -*- coding: utf-8 -*-
# @Time : 2021/3/7 0007
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 27.pyt包括 open，read，write："""
# 写数据
# with open('text.txt','w',encoding='utf-8') as f:
#     f.write("长江大学")
#     print("写入成功")
# 读取文件内容
with open('text.txt','r',encoding='utf-8') as f:
   text = f.read()
   print(text)

if __name__ == "__main__":
    pass