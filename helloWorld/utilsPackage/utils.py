#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

# 获取当前时间的毫秒数
def getCurrentMillis():
    current = int(1000 * time.time())
    # print("获取当前时间的毫秒数：" + str(current))
    return current