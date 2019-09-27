# pip install pdfkit
import pdfkit
# python pdfkit wkhtmltopdf生成pdf  https://blog.csdn.net/qq_42631707/article/details/99735884
# wkhtmltopdf 缩放问题   https://blog.csdn.net/churujianghu/article/details/75076255
# pdfkit源码  https://github.com/JazzCore/python-pdfkit

# 设置方式
# options = {
# 		'encoding': "utf-8",
# 		'disable-smart-shrinking':''
# }
options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
	'disable-smart-shrinking':False
}


install_path = r'D:\ProgramFiles\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=install_path)
url = "'https://www.cnblogs.com/xingzhui/p/7887212.html"
# url = "https://www.jianshu.com/p/a95cfad04206"
# url ="https://blog.csdn.net/qq_42631707/article/details/99735884"
out_put_file_path = "out.pdf"
pdfkit.from_url(url,out_put_file_path,options=options,configuration=config)