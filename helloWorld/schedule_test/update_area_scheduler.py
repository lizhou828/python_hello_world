# -*- coding:utf-8 -*-

"""
@Function:
@File    :          update_area_scheduler.py    
@Contact :          lizhou@glorypty.com
@License :          (C)Copyright 2019-2020

@Modify Time        @Author      @Version        @Desciption
------------        -------      --------        -----------
2019-7-19 11:00     lizhou         1.0         

"""
# 轻量级的定时任务调度的库  https://blog.csdn.net/liao392781/article/details/80521194
# pip install schedule
import schedule
import time

from helloWorld import print_info

# schedule只能用来执行一些小型的定时任务，有一定的局限性：
#
# 1.需要定时运行的函数job不应当是死循环类型的，也就是说，这个线程应该有一个执行完毕的出口。一是因为线程万一僵死，会是非常棘手的问题；二是下一次定时任务还会开启一个新的线程，执行次数多了就会演变成灾难。
#
# 2.如果schedule的时间间隔设置得比job执行的时间短，一样会线程堆积形成灾难，也就是说，我job的执行时间是1个小时，但是我定时任务设置的是5分钟一次，那就会一直堆积线程。
# ---------------------
# 作者：猪笨是念来过倒
# 来源：CSDN
# 原文：https://blog.csdn.net/liao392781/article/details/80521194
# 版权声明：本文为博主原创文章，转载请附上博文链接！

def test1():
    print_info("hello world")

schedule.every(10).seconds.do(test1)
schedule.every(10).minutes.do(test1)
schedule.every().hour.do(test1)
schedule.every().day.at("10:30").do(test1)
schedule.every(5).to(10).days.do(test1)
schedule.every().monday.do(test1)
schedule.every().wednesday.at("13:15").do(test1)


while True:
    schedule.run_pending()
    time.sleep(1)
