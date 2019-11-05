# -*- coding:utf-8 -*-

"""
@Function:  Python Flask Web开发（3） https://blog.csdn.net/langkew/article/details/51594880
           【Python】【Flask】Flask 后台发送html页面多种方法   https://www.cnblogs.com/mqxs/p/7904960.html
@File    :          controller.py    
@Contact :          lizhou@glorypty.com
@License :          (C)Copyright 2019-2020

@Modify Time        @Author      @Version        @Desciption
------------        -------      --------        -----------
2019-6-26 9:38     lizhou         1.0         

"""
import datetime
import time

from flask import Flask, redirect, abort, request, make_response
import os
import json
from concurrent.futures import ThreadPoolExecutor

from helloWorld import print_info

executor = ThreadPoolExecutor(1)

app = Flask(__name__)  # 实例化flask

@app.route('/')  # 首页路由
def hello_world():
    return 'hello'

@app.route('/status_500')
def status_500():
    return "hello", 500

@app.route('/json')
def do_json():
    hello = {"name":"stranger", "say":"hello"}
    return json.dumps(hello)

@app.route('/set_header')
def set_header():
    resp=make_response('<h1>This document has a modified header!</h1>')
    resp.headers['X-Something']='A value'
    resp.headers['Server']='My special http server'
    return resp


@app.route('/set_cookie') #设置cookie
def set_cookie():
    response=make_response('<h1>This document carries a cookie!</h1>')
    outdate=datetime.datetime.today()+datetime.timedelta(days=30)  #cookie的有效时长30天
    response.set_cookie('username','evancss',expires=outdate)
    return response

@app.route('/get_cookie')    #获取cookie
def get_cookie():
    name=request.cookies.get('username')
    return name


@app.route('/redir') #重定向
def redir():
    return redirect('https://www.baidu.com')

@app.route('/user/<id>')
def get_user(id):
    if int(id)>10:
        abort(404)
    return '<h1>Hello,%s</h1>'%id

@app.route('/test_async')
def update_redis():
    executor.submit(do_async,"我是words参数")
    return 'ok，后台在悄悄的做异步任务'

def do_async(words):
    print_info('start 悄悄的做异步任务：'+ words)
    time.sleep(3)
    print_info('end 悄悄的做异步任务：' + words)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)  # 启动flask





