# -*- coding: utf-8 -*-
# @Time : 2021/1/10 0010 12:47
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample5.py
# 列表的写操作

persons = ['张三', '赵六', '李四', '王五', '赵六', '钱七', '孙八']
# 列表的增加
persons.append("杨华钟")
print(persons)
# 列表的插入
persons.insert(2, '杨')
print(persons)
# 用insert()实现append()功能
for i in range(1, 10):
    persons.insert(len(persons), '{}'.format(i))
    # print(i)

# persons.insert(len(persons), '{}'.format(i))
print(persons)
# 列表的更新
persons[2] = '宋卫二'
print(persons)
# 范围的更新
persons[3:5] = ['王五', '李四']
print(persons)
# 删除元素（按元素直接删除）
persons.remove('杨华钟')
print(persons)
# 按元素位置删除元素用pop()
persons.pop(5)
print(persons)
# 删除一个范围的元素
persons[4:7] = []
print(persons)

persons[4:13] = []
print(persons)
