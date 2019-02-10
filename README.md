# python_hello_world
 version of Python : 3.5.1
 
《零基础学python》（第二版） https://docs.pythontab.com/learnpython/

#python todo list

## 基本阶段
    * web框架（mvc模式）用于快速开发
    
    
    * 增删改查
    * 模块化开发、部署等
    * 持续集成等
    
## 进阶阶段
    * python高级特性
    * python部分源码研究
    
    
## 高级阶段
    *性能问题
    *调优处理
    
    
## Python几种主流框架比较
    从GitHub中整理出的15个最受欢迎的Python开源框架。这些框架包括事件I/O，OLAP，Web开发，高性能网络通信，测试，爬虫等。
    
    Django: Python Web应用开发框架
    Django 应该是最出名的Python框架，GAE甚至Erlang都有框架受它影响。Django是走大而全的方向，它最出名的是其全自动化的管理后台：只需要使用起ORM，做简单的对象定义，它就能自动生成数据库结构、以及全功能的管理后台。
   
    Diesel：基于Greenlet的事件I/O框架
    Diesel提供一个整洁的API来编写网络客户端和服务器。支持TCP和UDP。
    
    Flask：一个用Python编写的轻量级Web应用框架
    Flask是一个使用Python编写的轻量级Web应用框架。基于Werkzeug WSGI工具箱和Jinja2模板引擎。Flask也被称为“microframework”，因为它使用简单的核心，用extension增加其他功能。Flask没有默认使用的数据库、窗体验证工具。

    Cubes：轻量级Python OLAP框架
    Cubes是一个轻量级Python框架，包含OLAP、多维数据分析和浏览聚合数据（aggregated data）等工具。
    
    Kartograph.py：创造矢量地图的轻量级Python框架
    Kartograph是一个Python库，用来为ESRI生成SVG地图。Kartograph.py目前仍处于beta阶段，你可以在virtualenv环境下来测试。
    
    Pulsar：Python的事件驱动并发框架
    Pulsar是一个事件驱动的并发框架，有了pulsar，你可以写出在不同进程或线程中运行一个或多个活动的异步服务器。
    
    Web2py：全栈式Web框架
    Web2py是一个为Python语言提供的全功能Web应用框架，旨在敏捷快速的开发Web应用，具有快速、安全以及可移植的数据库驱动的应用，兼容Google App Engine。
    
    Falcon：构建云API和网络应用后端的高性能Python框架
    Falcon是一个构建云API的高性能Python框架，它鼓励使用REST架构风格，尽可能以最少的力气做最多的事情。

    Dpark：Python版的Spark
    DPark是Spark的Python克隆，是一个Python实现的分布式计算框架，可以非常方便地实现大规模数据处理和迭代计算。DPark由豆瓣实现，目前豆瓣内部的绝大多数数据分析都使用DPark完成，正日趋完善。

    Buildbot：基于Python的持续集成测试框架
    Buildbot是一个开源框架，可以自动化软件构建、测试和发布等过程。每当代码有改变，服务器要求不同平台上的客户端立即进行代码构建和测试，收集并报告不同平台的构建和测试结果。

    Zerorpc：基于ZeroMQ的高性能分布式RPC框架
    Zerorpc是一个基于ZeroMQ和MessagePack开发的远程过程调用协议（RPC）实现。和 Zerorpc 一起使用的 Service API 被称为 zeroservice。Zerorpc 可以通过编程或命令行方式调用。

    Bottle: 微型Python Web框架
    Bottle是一个简单高效的遵循WSGI的微型python Web框架。说微型，是因为它只有一个文件，除Python标准库外，它不依赖于任何第三方模块。

    Tornado：异步非阻塞IO的Python Web框架
    Tornado的全称是Torado Web Server，从名字上看就可知道它可以用作Web服务器，但同时它也是一个Python Web的开发框架。最初是在FriendFeed公司的网站上使用，FaceBook收购了之后便开源了出来。

    webpy: 轻量级的Python Web框架
    webpy的设计理念力求精简（Keep it simple and powerful），源码很简短，只提供一个框架所必须的东西，不依赖大量的第三方模块，它没有URL路由、没有模板也没有数据库的访问。

    Scrapy：Python的爬虫框架
    Scrapy是一个使用Python编写的，轻量级的，简单轻巧，并且使用起来非常的方便。