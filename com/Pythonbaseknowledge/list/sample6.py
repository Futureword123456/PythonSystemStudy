# -*- coding: utf-8 -*-
# @Time : 2021/1/10 0010 13:35
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample6.py

# 其他方法
# 统计出现的次数
persons = ['张三', '赵六', '李四', '王五', '赵六', '钱七', '孙八']
cnt = persons.count("赵六")
print(cnt)

# persons.append(["研发","五四"])
print(persons)
# extend将原始列表增加到末尾，append将整个列表增加到末尾
persons.extend(["研发", "五四"])
print(persons)

# 判断元素是否存在用in
persons.remove("张三")
print("张三" in persons)

# 列表的复制
persons1 = persons.copy()
persons2 = persons
print(persons2)
print(persons1)
print(persons2 is persons1)
print(persons2 is persons)
print(persons1 is persons)

# clear用于清空列表
persons.clear()
print(persons)
print(persons1)
print(persons2)
