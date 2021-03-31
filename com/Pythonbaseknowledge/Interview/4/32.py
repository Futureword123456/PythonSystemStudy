# -*- coding: utf-8 -*-
# @Time : 2021/3/8 0008
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 32.py
"""Python list 常用操作"""
# 1、list的创建
list1 = ["a", "b", "mpilgrim", "z", "example"]
print(list1)
print(list1[1])
print(list1[:3])
print(list1[1:4])
"""包含左边不包含右边正索引从0开始，负索引从-1开始"""
# 2、list 负数索引
print(list1[-3])
print(list1[1:-1])
# 3.list 增加元素
# append()每次只能添加一个列表
list1.append('yang')
print(list1)
list1.insert(1, 'hua')
print(list1)
# extend()可以添加多个列表
list1.extend(['ui', 'yui', 'oiu'])
print(list1)
# 4.list 搜索index()得到对应位置的索引
print(list1.index('ui'))
# 5.list 删除元素
list1.remove('ui')
print(list1)
list1.pop(2)
print(list1)
# 6.list 运算符
list1 = list1 + ['tze', 'h']
print(list1)
list1 = list1 * 1
print(list1)
# 7.使用join链接list成为字符串
# 8.list 分割字符串
# join()列表转字符串
list1 = ','.join(list1)
print(list1)

print(list1.split(','))

# 9.list 的映射解析
li = [1, 5, 3, 6, 8]
li1 = []
for i in li:
    print(i * 2, end=' ')
    li1.append(i * 2)
print(li1)
# 10.dictionary 中的解析
# params.items()把字典转换为元组
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print(params.keys())
print(params.values())
print(params.items())
list2 = []
list3 = []
for i in params.items():
    # print(list(i)[0])
    list2.append(list(i)[0])
    list3.append(list(i)[1])
print(list2)
print(list3)
# 11.list 过滤

if __name__ == "__main__":
    pass
