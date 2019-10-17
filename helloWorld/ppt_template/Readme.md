# python生成ppt的方法
    这篇文章主要为大家详细介绍了python生成ppt的方法，通过python生成ppt文件，具有一定的参考价值，感兴趣的小伙伴们可以参考一下
    
# 第三方库安装
    pip3 install python-pptx
    
# 技术方案、系统、架构等调研
## 技术方案有：
    java的实现有poi库
    python的实现有python-pptx库
## 系统方面：
    开发环境Windows10
    生产环境CentOS7
## 第三方包的适用条件与局限性等：
    poi库，代码繁琐，在pptx中生成并插入图表后，再打开时提示“有损坏的内容，并开始尝试修复”，点击修复后，部分图表丢失
    python-pptx库 ，需要依赖微软的office组件，在Linux系统中并没有这些组件
    经了解后，Linux系统中的，可以安装 openoffice、wps等软件，但跟微软的office组件有一定的兼容性问题
## 解决方案    
    1、用依赖微软组件的方式，生产环境需要部署windows机，并安装office模块
    2、不用依赖微软组件的方式，需要先采坑，生成的pptx文件尽量与微软的office兼容，尽量没有问题
            
    
# 参考文档

[python-pptx官方文档](https://python-pptx.readthedocs.io/en/stable/user/quickstart.html)
麻痹的，还是官方文档能解决问题!!!!!
[python pptx change entire table font size](https://stackoverflow.com/questions/40343921/python-pptx-change-entire-table-font-size)

[python-pptx库中文文档及使用样例](https://blog.csdn.net/u011932355/article/details/73287248)

[python生成ppt的方法](https://www.jb51.net/article/141636.htm)    

[实战 | Python自动生成PPT分析报告](https://www.sohu.com/a/164157866_505802)

[利用python自动生成数据分析PPT报告](https://github.com/lizhou828/py-pptx)

[python-pptx对已有ppt进行修改注意事项](https://blog.csdn.net/u013747832/article/details/78682817)

[python提取PPT中的文字（包括图片中的文字)](https://blog.csdn.net/qq_41020281/article/details/99894064)

[小白学Python（4）——用Python创建PPT](https://www.cnblogs.com/adam012019/p/11344980.html)





[java使用poi操作PPT读取模板流，生成新PPT文件](https://blog.csdn.net/ccmedu/article/details/79267147)

[poi生成动态模板ppt报告](https://blog.csdn.net/HuHui_/article/details/83350049)

[poi操作ppt生成图表](https://blog.csdn.net/starandsea/article/details/51741328)

[POI之PPT中生成表格简单实例](https://blog.csdn.net/huangwenyi1010/article/details/51705402)

[Java POI导出ppt简单实现](http://www.anyrt.com/blog/list/poippt.html)

[用Java实现PPT转换成PDF的一种方式－－openoffice的使用](https://blog.csdn.net/u010188178/article/details/83344418)

[java实现PPT转化为PDF](https://www.jb51.net/article/141641.htm)
