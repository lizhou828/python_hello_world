# -*- coding:utf-8 -*-
# 参考文章地址：
# Python的Flask框架开发RESTful API https://www.jianshu.com/p/ed1f819a7b58

# 安装flask
# pip install flask


from flask import  Flask,jsonify,request,make_response,abort

app = Flask(__name__)


MY_URL = '/api/v1/'
hello='今天天气真好呀'
not_hello = '为什么今天天气不好呀'

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>hello world</h1>'


#get
@app.route(MY_URL + 'get/',methods=['GET'])
def get_task():
    print("get is running...")
    if not 'abc' in request.args.to_dict():
        abort(404)
    return str(request.args.to_dict())



# add方法 请求示例：
#
# 请求头：
# Content-Type ：  application/json
#
# 请求内容：
# {
# 	"id": "3",
# 	"name": "liz"
# }

@app.route(MY_URL + 'add', methods=['POST'])
def add_task():
    print(request.json)
    if not request.json or 'id' not in request.json or 'name' not in request.json:
        abort(400)
    task = {
        'id': request.json['id'],
        'name': request.json['name']
    }

    return jsonify({'code': '200','message':'ok','data':task})


#post
@app.route(MY_URL + 'post/',methods=['POST'])
def post_task():
    print("post is running...")
    print(request.json)
    if not request.json:
        abort(404)
    global hello
    # Python中的作用域及global用法  https://www.cnblogs.com/summer-cool/p/3884595.html
    hello = hello + str(request.json)
    return hello




#404处理
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}),404)

if __name__ == '__main__':
    # 设置Flask为任何地址均可以访问，post设置为‘0.0.0.0’，  解决在局域网内通过服务器IP地址访问不了
     app.run(host='0.0.0.0', port=5000)
