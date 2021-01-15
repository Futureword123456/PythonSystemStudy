# -*- coding: utf-8 -*-
# @Time : 2021/1/13 0013 14:20
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample4.py
# 集合的遍历
collect1 = {"经济学", "哲学", "金融学", '历史学', "文学"}
for c in collect1:
    print(c, end="|")
# 如何判断一个元素是否在集合中
print("哲学" in collect1)
print("计算机" in collect1)

# 集合是没有索引的'set' object does not support indexing
# print(collect1[2])
# 新增数据，add()一次只能增加一个元素
collect1.add("计算机")
collect1.add("法学")
print(collect1)
print(list(collect1))
# 用update方法一次添加多个元素，集合是不支持更新操作的
collect1.update(['生物学', '工程学'])
print(collect1)
# 更新操作的要删除原有元素，再创建新元素
# remove如果删除不存在的元素会报错
#collect1.remove("生物学")
# discard()如果遇到不存在时就会忽略
collect1.discard("生物")
collect1.add("医学")
print(collect1)
