# 函数的使用技巧-1
# 1. 为参数设置默认值,只需要在形参后面增加 "= 具体值" 即可
def calc_exchange_rate(amt, source="CNY", target="USD"):
    print(target)
    if source == "CNY" and target == "USD":
        # 6.7516 : 1
        result = amt / 6.7516
        # print(result)
        print("汇率计算成功")
        return result
    elif source == "CNY" and target == "EUR":
        result = amt / 7.7512
        return result


print(calc_exchange_rate(100))


# 2. 以形参形式传参(关键字传参)
def health_check(name, age, height, weight, hr, hbp, lbp, glu):
    print("您的健康状况良好")


health_check(name="张三", height=178, age=32, weight=85.5, hr=70, hbp=120, lbp=80, glu=4.3)

# 3.混合形式传参
# * 代表之后所有参数传参时必须使用关键字传参
def health_check1(name, age, *, height, weight, hr, hbp, lbp, glu):
    print("您的健康状况良好")


health_check1("张三", 32, height=178, weight=85.5, hr=70, hbp=120, lbp=80, glu=4.3)
