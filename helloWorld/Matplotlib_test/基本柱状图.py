# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

name_list = ['Monday','Tuesday','Friday','Sunday']
num_list = [1.5, 0.6, 7.8, 6]
plt.bar(range(len(num_list)), num_list, fc='red',tick_label=name_list)
# plt.bar(range(len(num_list)), num_list, color='rgb',tick_label=name_list)
plt.show()