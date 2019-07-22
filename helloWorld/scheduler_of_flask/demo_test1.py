# -*- coding:utf-8 -*-
import time
from flask import Flask
from flask_apscheduler import APScheduler


# APScheduler（Python化的Cron）使用总结 定时任务  https://www.cnblogs.com/zhaoyingjie/p/9664081.html

class Config(object):
    SCHEDULER_API_ENABLED = True


scheduler = APScheduler()


# interval examples
@scheduler.task('interval', id='do_job_1', seconds=5, misfire_grace_time=900)
def job1():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) +  '    Job 1 executed')


# cron examples
@scheduler.task('cron', id='do_job_2',hour='14', minute='37')
def job2():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) +  '    Job 2 executed')


# @scheduler.task('cron', id='do_job_3', week='*', day_of_week='sun')
# def job3():
#     print('Job 3 executed')


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(Config())

    # it is also possible to enable the API directly
    # scheduler.api_enabled = True


    scheduler.init_app(app)  # 把任务列表放进flask
    scheduler.start()  # 启动任务列表

    app.run(host='0.0.0.0', port=9001, debug=True, use_reloader=False)  # 启动flask