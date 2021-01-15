# -*- coding: utf-8 -*-
# @Time : 2021/1/14 0014 16:32
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : yci_assistant.py
# 生活小助理
import random


# randint()函数包含边界值
# r = random.randint(1, 16)
# print(r)
# 生成双色球
def generate_unionlotto(number):
    for j in range(0, int(number)):
        for i in range(0, 6):  # 生成红球
            red = random.randint(1, 33)
            print(red, end=" ")

        blue = random.randint(1, 16)  # 生成蓝球
        print(blue)


# 号码百事通
def find_phone(keyword):
    phone_list = phone_number_srt.split(",")
    for i in phone_list:
        if i.find(keyword) != -1:
            print(i)


def get_wheather(city):
    city_list = wheather_str.split("~")
    wheather_data = {}
    for i in range(0, len(city_list)):  # 用字典进行封装循环用len()可以得到对应的索引值
        w = city_list[i].split(",")
        print(w)
        # print(w)# 列表转换为字典
        wheather = {"name": w[0], "date": w[1], "weather": w[2], "max": w[3], "min": w[4], "wind": w[5]}
        # print(wheather)
        wheather_data[wheather["name"]] = wheather
    # print(wheather_data)
    '''{'北京': {'name': '北京', 'date': '2019年1月12日', 'weather': '多云', 'max': '8°C', 'min': '-4°C', 'wind': '南风3级'}, 
    '上海': {'name': '上海', 'date': '2019年1月12日', 'weather': '小雨', 'max': '9°C', 'min': '6°C', 'wind': '北风2级'}, 
    '广州': {'name': '广州', 'date': '2019年1月12日', 'weather': '阵雨转多云', 'max': '22°C', 'min': '15°C', 
    'wind': '持续无风向微风'}} '''
    if city in wheather_data:
        return wheather_data.get(city)
    else:
        return {}


phone_number_srt = "匪警[110],火警[119],急救中心[120],道路交通事故报警[122],水上求救专用电话[12395],天气预报[12121],报时服务[12117],森林火警[12119]," \
                   "电力服务[95598],红十字会急救台[999],公安短信报警[12110],通用紧急求救[112],信产部IP/网站备案[010-66411166] "

wheather_str = "北京,2019年1月12日,多云,8°C,-4°C,南风3级~上海,2019年1月12日,小雨,9°C,6°C,北风2级~广州,2019年1月12日,阵雨转多云,22°C,15°C,持续无风向微风"

while True:
    print("输入1双色球随机选号")
    print("输入2号码百事通")
    print("输入3明日天气预报")
    print("输入0结束程序")
    c = input("请输入功能编号:")
    if c == "1":
        n = input("你要生成几个双色球号码:")
        generate_unionlotto(n)
    elif c == "2":
        n = input("你要查询的机构或者电话号码:")
        find_phone(keyword=n)

    elif c == "3":
        n = input("你要查询的城市:")
        w = get_wheather(n)
        print(w)
        if "name" in w:
            print("{date} {name} {weather} {max}/{min} {wind}".format_map(w))
        else:
            print("未找到{}天气数据".format(n))
    elif c == "0":
        print("感谢你的使用，再见！@！")
        break

    else:
        print("你是如的功能编号有误，请重新输入")
    print("===================================")