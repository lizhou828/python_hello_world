# python使用PDF模板生成文件

## 策略
    根据对已有的PDF模板文件，往每一页加入文本、图表、表格、图片等内容，生成最终的pdf文件

## reportlab生成pdf的方式
### canvas
    这种方式能手动调控布局，但是不能生成图表、表格、
    代码如下：
    canvas = canvas.Canvas("reportlab_test1.pdf")
    canvas.drawString(300,3,"Hello,World " + str(index))
    canvas.showPage() # 关闭当前页，打开新的一页
    canvas.save()
    
### SimpleDocTemplate.build()
    这种方式能生成图表、表格、但不方便对插入的组件进行布局    
    布局的折中方式：通过表格 或者嵌套表格的方式，进行简单的布局

#参考文档
[python和java代码例子](https://www.programcreek.com/python/)

reportlab
[Python reportlab.platypus.SimpleDocTemplate() Examples ](https://www.programcreek.com/python/example/51068/reportlab.platypus.SimpleDocTemplate)
[Python reportlab.platypus.TableStyle() Examples ](https://www.programcreek.com/python/example/51066/reportlab.platypus.TableStyle) 
[pdf 模板：可以使用 pyPdf 和 reportlab 包。](http://stackoverflow.com/questions/1180115/add-text-to-existing-pdf-using-python)
[Python3用ReportLab生成pdf报表,不学何来惊喜?](https://www.jianshu.com/p/a09186fc3131)
[reportlab 中文问题[已解决]](https://www.jianshu.com/p/41284e4e25f5)
[python之reportlab生成PDF文件](https://www.cnblogs.com/zoe-yan/p/11356410.html)
[python reportlab 生成table （比较全面，一篇足够）](https://blog.csdn.net/weixin_40161254/article/details/84827805)
[python reportlab 生成pdf (二) SimpleDocTemplate](https://blog.csdn.net/kingken212/article/details/47209791/)
[python+reportlab实战：生成一个带表格图片的PDF](https://blog.csdn.net/jtscript/article/details/45217697)
[reportlab 页脚和页眉的使用](https://blog.csdn.net/liyadian/article/details/81253117)
[pyhton之Reportlab模块](https://www.cnblogs.com/hujq1029/p/7767980.html)
[python之reportlab生成PDF测试报告](https://www.cnblogs.com/zoe-yan/p/11356410.html)

html Jinja WeasyPrint
[使用Pandas、Jinja和WeasyPrint制作pdf报告](https://blog.csdn.net/sinat_38682860/article/details/88725246)
[我用Python做了一份PDF报告！！！](http://www.sohu.com/a/302773259_671965)
[Python数据生成pdf文件](https://www.cnblogs.com/webRobot/p/6999665.html)

PyPDF2
[Python实现PyPDF2处理PDF文件的方法示例](https://www.jb51.net/article/170793.htm)

PdfKit
[Python将html转化为pdf(PdfKit)](https://www.cnblogs.com/xingzhui/p/7887212.html)
[Create PDF files from templates with Python and Google Scripts](https://www.codementor.io/garethdwyer/create-pdf-files-from-templates-with-python-and-google-scripts-p63kal1vb)

[java 根据PDF模板生成PDF文件(基于iTextSharp)](https://my.oschina.net/lichaoqiang/blog/1834149)
[java 根据PDF模板生成PDF文件并导出](https://blog.csdn.net/m0_37123168/article/details/89599184)
[java根据模板生成pdf文件并导出](https://blog.csdn.net/WeakCH/article/details/82887147)
[Java生成PDF文件---iText ](https://www.cnblogs.com/qlqwjy/p/8213989.html)