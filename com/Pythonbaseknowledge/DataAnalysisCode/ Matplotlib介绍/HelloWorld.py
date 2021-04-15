# -*- coding: utf-8 -*-
# @Time    : 2021/4/15 0015 15:05
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : HelloWorld.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()
