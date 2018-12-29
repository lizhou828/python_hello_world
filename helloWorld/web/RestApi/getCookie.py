# -*- coding:utf-8 -*-
# 爬取数据遇到状态码“521”
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

@app.route('/cookie', methods=['GET', 'POST'])
def cookie():
    cookie = return_cookie("http://www.66ip.cn/","GBK")
    return '<h1>' + cookie + '</h1>'



headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36',
    }

def get_html(url,charset):
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



def return_cookie(url,charset):
    first_html = get_html(url,charset)
    # 执行JS获取Cookie
    cookie_str = executejs(first_html)

    # 将Cookie转换为字典格式
    cookie = parse_cookie(cookie_str)
    print('cookies = ',cookie)
    return cookie



if __name__ == '__main__':
    # 设置Flask为任何地址均可以访问，post设置为‘0.0.0.0’，  解决在局域网内通过服务器IP地址访问不了
    # debug=True
    app.run(host='0.0.0.0', port=9000,debug=True)
