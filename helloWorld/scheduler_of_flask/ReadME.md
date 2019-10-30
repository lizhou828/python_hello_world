# 安装模块
    pip install flask
    pip install Flask-APScheduler
    
    uWSGI是C语言编写，Gunicorn是Python，
    如果是计算密集型的应用，uWSGI比较合适作为web服务器；如果是IO密集型的应用，Gunicorn则更合适作为web服务器
    windows环境下不支持Gunicorn
    
    
    
# 参考文档
[flask中使用模板引擎返回网页](https://blog.csdn.net/longting_/article/details/80629153)

[Flask使用教程-加载静态文件及显示前端页面](https://blog.csdn.net/qq_37561761/article/details/79329180)

[python框架之flask自定义配置文件的两种方法！](https://blog.csdn.net/weixin_43343144/article/details/86572314)

[Python Flask Web开发（3）]( https://blog.csdn.net/langkew/article/details/51594880)

[【Python】【Flask】Flask 后台发送html页面多种方法   ](https://www.cnblogs.com/mqxs/p/7904960.html)
    
[APScheduler（Python化的Cron）使用总结 定时任务](  https://www.cnblogs.com/zhaoyingjie/p/9664081.html)

[python3+flask 开发web(九)——flask_apscheduler定时任务框架]( 原文地址:https://blog.csdn.net/weixin_39430584/article/details/83509237 )

[源码]( https://github.com/viniciuschiele/flask-apscheduler)
         
[使用MVC编程模型通过flask蓝图实现前端后台新闻发布系统](  http://www.manongjc.com/detail/7-ypubaihttzmbweo.html)

[Flask 处理高并发、多线程的配置](https://www.jianshu.com/p/79489cfc6fb9)

[Flask+Gunicorn+Nginx 支持高并发下的Flask架构部署](https://blog.csdn.net/carolcoral/article/details/89399254)

[分享一个flask高并发部署方案](https://blog.csdn.net/zmy941110/article/details/89639883)
以gunicorn作为web服务器，运行项目（部分代码）

[部署python项目到linux服务器 ](https://www.lanshiqin.com/d8d0505b/)    
以python命令运行项目    

[uwsgi部署flask项目到linux服务器](https://blog.51cto.com/12482328/2087117) 

[nginx+uwsgi 和nginx+gunicorn区别、如何部署](https://www.jianshu.com/p/be2b587a900e

[gunicorn 详解](https://www.jianshu.com/p/69e75fc3e08e)

[gunicorn官方文档](http://docs.gunicorn.org/en/stable/)

[gunicorn、uwsgi性能测试](https://blog.csdn.net/weixin_34112030/article/details/92911057)

[Gunicorn , uWSGI同步异步测试以及应用场景总结](https://blog.csdn.net/orangleliu/article/details/49275687)

[Python Web 部署是 uWSGI 还是 gunicorn 更优？](https://hacpai.com/article/1458191908235)

[Python中如何使用pip安装自己的第三方模块](https://www.linuxidc.com/Linux/2016-11/137015.htm)