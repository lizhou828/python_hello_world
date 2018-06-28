#通用文字识别接口(百度云)


##文档地址：

    https://cloud.baidu.com/doc/OCR/OCR-Python-SDK.html#.E6.96.B0.E5.BB.BAAipOcr

##准备步骤：
    安装OCR Python SDK (支持Python版本：2.7.+ ,3.+)  ,  OCR Python SDK目录结构:
    ├── README.md
    ├── aip                   //SDK目录
    │   ├── __init__.py       //导出类
    │   ├── base.py           //aip基类
    │   ├── http.py           //http请求
    │   └── ocr.py //OCR
    └── setup.py              //setuptools安装
 
    •如果已安装pip，执行pip install baidu-aip即可。
    •如果已安装setuptools，执行python setup.py install即可。
    
    
## 接口调用

    from aip import AipOcr

    """ 你的 APPID AK SK """
    APP_ID = '你的 App ID'
    API_KEY = '你的 Api Key'
    SECRET_KEY = '你的 Secret Key'
    
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    
    在上面代码中，常量APP_ID在百度云控制台中创建，常量API_KEY与SECRET_KEY是在创建完毕应用后，系统分配给用户的，均为字符串，用于标识用户，为访问做签名验证，可在AI服务控制台中的应用列表中查看。
    注意：如您以前是百度云的老用户，其中API_KEY对应百度云的“Access Key ID”，SECRET_KEY对应百度云的“Access Key Secret”。
