# -*- coding:utf-8 -*-

"""
@Function:  Python Flask Web开发（3） https://blog.csdn.net/langkew/article/details/51594880 Web端 VR全景图的各种实现
           【Python】【Flask】Flask 后台发送html页面多种方法   https://www.cnblogs.com/mqxs/p/7904960.html
           flask中使用模板引擎返回网页  https://blog.csdn.net/longting_/article/details/80629153
@File    :          controller.py    
@Contact :          lizhou@glorypty.com
@License :          (C)Copyright 2019-2020

@Modify Time        @Author      @Version        @Desciption
------------        -------      --------        -----------
2019-6-26 9:38     lizhou         1.0         

"""

from flask import Flask
import os
import json

# 实例化flask
# static_url_path='' 表示要在当前文件下，建立个static的静态资源目录
app = Flask(__name__,static_url_path='')


@app.route('/')  # 首页路由
def hello_world():
    return 'hello1111'


@app.route('/threejs', methods=['GET'])
def three():
    # 官网 https: // threejs.org
    # 例子 https: // threejs.org / examples /  # css3d_panorama
    # 源码 https://github.com/mrdoob/three.js
    return app.send_static_file("threeJS/css3d_panorama.html")  # 在static文件夹下查找页面和静态资源文件

@app.route('/aframe', methods=['GET'])
def aframe():
    # 官网 https://aframe.io
    # 例子 https://aframe.io/examples/showcase/sky/
    #源码  https://github.com/aframevr/aframe
    return app.send_static_file("aframe/index.html")  # homepage.html在html文件夹下


@app.route('/pannellum', methods=['GET'])
def pannellum():
    # 官网 https://pannellum.org
    # 例子 https://pannellum.org/documentation/examples/simple-example/
    #源码  https://github.com/mpetroff/pannellum/
    return app.send_static_file("pannellum/index.html")  # homepage.html在html文件夹下


@app.route('/haoshitong_ppt', methods=['GET'])
def haoshitong_ppt():
    return app.send_static_file("haoshitong.pptx")

@app.route('/vhall', methods=['GET'])
def vhall():
    return app.send_static_file("vhall.pdf")


@app.route('/vhall_xlsx', methods=['GET'])
def vhall_xlsx():
    return app.send_static_file("vhall.xlsx")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)  # 启动flask
