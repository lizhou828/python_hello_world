# -*- coding:utf-8 -*-
# python3+flask 开发web(九)——flask_apscheduler定时任务框架
# 原文地址:https://blog.csdn.net/weixin_39430584/article/details/83509237
# 源码地址：https://github.com/viniciuschiele/flask-apscheduler
import os

import time
from flask_apscheduler import APScheduler
from flask import Flask

# JOBS配置文件中：其中id是一个标识，func指定定时执行的函数，args指定输入参数列表，trigger指定任务类型，如interval表示时间间隔，seconds表示时间周期，单位是秒

# job1的trigger为cron ，表示按照cron时间执行
# job2的trigger为interval，表示

class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': '__main__:job_1',
            'args': (1, 2),
            'trigger': 'cron',
            'hour': 14,
            'minute': 29
        },
        {
            'id': 'job2',
            'func': '__main__:job_1',
            'args': (3, 4),
            'trigger': 'interval',
            'seconds': 5
        }
    ]


def job_1(a, b):  # 一个函数，用来做定时任务的任务。
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) +' ' + str(a) + ' ' + str(b))


app = Flask(__name__)  # 实例化flask

app.config.from_object(Config())  # 为实例化的flask引入配置


@app.route('/')  # 首页路由
def hello_world():
    return 'hello'


if __name__ == '__main__':
    scheduler = APScheduler()  # 实例化APScheduler
    # it is also possible to enable the API directly
    # scheduler.api_enabled = True


    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        # do something only once, before the reloader （创建实例）
        scheduler.init_app(app)  # 把任务列表放进flask

    scheduler.start()  # 启动任务列表

    app.run(host='0.0.0.0', port=9000, debug=True)  # 启动flask


    # 防止定时任务运行两次的问题的解决方案：https://www.cnblogs.com/jessicaDuan/p/7827618.html
    # 1、app.run() 增加 use_reloader=False 配置，
    # 2、 if os.environ.get('WERKZEUG_RUN_MAIN') == 'true' 时实例化scheduler


