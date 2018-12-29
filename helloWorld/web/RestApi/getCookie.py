# -*- coding:utf-8 -*-
# 爬取www.66ip.cn网站数据时，遇到状态码“521”的问题和js代码混淆的问题
# https://blog.csdn.net/meetliuxin/article/details/82882095

# 预先安装 execjs的包
# pip install PyExecJS

from flask import  Flask,jsonify,request,make_response,abort
import requests
import re
import execjs

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>hello world</h1>'


# 多个参数传递
# 如果是application/json方式
# from flask_restful import request
# dict = request.json()
#
# 如果是application/x-www-form-urlencoded方式
# from flask_restful import request
# dict = request.form


# 请求的json数据格式如下
# {
#   "url":"",
#   "user-agent":""
# }
@app.route('/generalCookie', methods=['POST'])
def cookie():
    if not request.json or 'url' not in request.json or 'user-agent' not in request.json:
        return jsonify({'code': '400','message':'bad request','data':""})

    postParams = request.json
    headers = {
        'user-agent': postParams["user-agent"],
    }
    cookie = return_cookie(postParams["url"],"GBK",headers)
    return jsonify({'code': '200','message':'ok','data':cookie})

def get_html(url,charset,headers):
    first_html = requests.get(url=url,headers=headers).content.decode(charset)
    return first_html


def executejs(first_html):
    # 提取其中的JS加密函数
    js_string = ''.join(re.findall(r'(function .*?)</script>', first_html))

    # 提取其中执行JS函数的参数
    js_arg = ''.join(re.findall(r'setTimeout\(\"\D+\((\d+)\)\"', first_html))
    js_name = re.findall(r'function (\w+)',js_string)[0]

    # 修改JS函数，使其返回Cookie内容
    js_string = js_string.replace('eval("qo=eval;qo(po);")', 'return po')

    func = execjs.compile(js_string)
    return func.call(js_name,js_arg)

def parse_cookie(string):
    string = string.replace("document.cookie='", "")
    clearance = string.split(';')[0]
    return {clearance.split('=')[0]: clearance.split('=')[1]}



def return_cookie(url,charset ,headers):
    first_html = get_html(url,charset,headers)
    # 执行JS获取Cookie
    cookie_str = executejs(first_html)

    # 将Cookie转换为字典格式
    cookie = parse_cookie(cookie_str)
    print('cookies = ',cookie)
    return cookie



#404处理
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}),404)



if __name__ == '__main__':
    # 设置Flask为任何地址均可以访问，post设置为‘0.0.0.0’，  解决在局域网内通过服务器IP地址访问不了
    # debug=True
    app.run(host='0.0.0.0', port=9000,debug=True)
