# -*- coding: utf-8 -*-
# @Time : 2021/1/13 0013 13:16
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample2.py
# 集合的数学运算
collect = {'哲学', '经济学', '法学', '教育学'}
collect2 = {"经济学", "哲学", "金融学", '历史学', "文学"}
# 交集，获取两个集合中重复的部分，建立一个集合
c3 = collect.intersection(collect2)
print(c3)
# 更新原有集合
collect.intersection_update(collect2)
print(collect)
print(len(collect))
print(list(collect))
collect_list = []
for i in list(collect):
    print(i)
    collect_list.append(i)
print(collect_list)
print(tuple(collect_list))

# 并集将两个集合所有运算合并，去重
collect = {'哲学', '经济学', '法学', '教育学'}
collect2 = {"经济学", "哲学", "金融学", '历史学', "文学"}
print(collect.union(collect2))
print(list(collect).count("法学"))
# 差集，是指两个集合之间差异的部分differenct代表在A在B中不存在的部分
print(collect.difference(collect2))
print(collect2.difference(collect))
# symmetric_difference代表双向差集
print(collect.symmetric_difference(collect2))

collect.symmetric_difference_update(collect2)
print(collect)
