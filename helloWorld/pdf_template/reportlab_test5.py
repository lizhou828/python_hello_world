from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch, mm, cm

from reportlab.platypus import Paragraph, SimpleDocTemplate, PageBreak,Image, Table, TableStyle,Spacer
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet

from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing, Rect
from reportlab.graphics.charts.textlabels import Label





# 参考文档
# pyhton之Reportlab模块  https://www.cnblogs.com/hujq1029/p/7767980.html

# 注册字体
# simsun.ttc 下载地址：https://github.com/StellarCN/scp_zh/tree/master/fonts
#simsun.ttc 文件下载后，放在：${python_home}\Lib\site-packages\reportlab\fonts 目录下
pdfmetrics.registerFont(TTFont('SimSun', "simsun.ttc"))

def text_test():
	Style = getSampleStyleSheet()

	bt = Style['Normal']  # 字体的样式
	# bt.fontName='song'    #使用的字体
	bt.fontSize = 14  # 字号
	bt.wordWrap = 'CJK'  # 该属性支持自动换行，'CJK'是中文模式换行，用于英文中会截断单词造成阅读困难，可改为'Normal'
	bt.firstLineIndent = 32  # 该属性支持第一行开头空格
	bt.leading = 20  # 该属性是设置行距

	ct = Style['Normal']
	ct.fontName='SimSun'
	ct.fontSize = 12
	ct.alignment = 1  # 居中

	ct.textColor = colors.red

	t = Paragraph('你瞅啥?', bt)
	return t

def autoLegender( title=''):
	'''
		在边框中添加文字
	:param title:
	:return:
	'''

	width = 448
	height = 230
	d = Drawing(width,height)
	lab = Label()
	lab.x = 220  #x和y是文字的位置坐标
	lab.y = 210
	lab.setText(title)
	lab.fontName = 'SimSun' #增加对中文字体的支持
	lab.fontSize = 20
	d.add(lab)
	d.background = Rect(0,0,width,height,strokeWidth=1,strokeColor="#868686",fillColor=None) #边框颜色

	return d


def table_model(data):
	width = 7.2  # 总宽度
	colWidths = (width / len(data[0])) * inch  # 每列的宽度

	dis_list = []
	for x in data:
		# dis_list.append(map(lambda i: Paragraph('%s' % i, cn), x))
		dis_list.append(x)

	style = [
		# ('FONTNAME', (0, 0), (-1, -1), 'song'),  # 字体
		('FONTSIZE', (0, 0), (-1, 0), 15),  # 字体大小
		('BACKGROUND', (0, 0), (-1, 0), HexColor('#d5dae6')),  # 设置第一行背景颜色
		('BACKGROUND', (0, 1), (-1, 1), HexColor('#d5dae6')),  # 设置第二行背景颜色

		# 合并 （'SPAN',(第一个方格的左上角坐标)，(第二个方格的左上角坐标))，合并后的值为靠上一行的值，按照长方形合并
		('SPAN', (0, 0), (0, 1)),
		('SPAN', (1, 0), (2, 0)),
		('SPAN', (3, 0), (4, 0)),
		('SPAN', (5, 0), (7, 0)),

		('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # 对齐
		('VALIGN', (-1, 0), (-2, 0), 'MIDDLE'),  # 对齐
		('LINEBEFORE', (0, 0), (0, -1), 0.1, colors.grey),  # 设置表格左边线颜色为灰色，线宽为0.1
		('TEXTCOLOR', (0, 0), (-1, 0), colors.royalblue),  # 设置表格内文字颜色
		('TEXTCOLOR', (0, -1), (-1, -1), colors.red),  # 设置表格内文字颜色
		('GRID', (0, 0), (-1, -1), 0.5, colors.grey),  # 设置表格框线为grey色，线宽为0.5
	]

	component_table = Table(dis_list, colWidths=colWidths, style=style)

	return component_table


def draw_pie_autoLegender( chart,title=''):
	width = 448
	height = 230
	d = Drawing(width,height)
	lab = Label()
	lab.x = 220  #x和y是文字的位置坐标
	lab.y = 210
	lab.setText(title)
	lab.fontName = 'SimSun' #增加对中文字体的支持
	lab.fontSize = 20
	d.add(lab)
	d.background = Rect(0,0,width,height,strokeWidth=1,strokeColor="#868686",fillColor=None) #边框颜色
	d.add(chart)

	return d

def draw_pie(data=[], labels=[], use_colors=[], width=360,):
    '''更多属性请查询reportlab.graphics.charts.piecharts.WedgeProperties'''

    pie = Pie()
    pie.x = 60 # x,y饼图在框中的坐标
    pie.y = 20
    pie.slices.label_boxStrokeColor = colors.white  #标签边框的颜色

    pie.data = data      # 饼图上的数据
    pie.labels = labels  # 数据的标签
    pie.simpleLabels = 0 # 0 标签在标注线的右侧；1 在线上边
    pie.sameRadii = 1    # 0 饼图是椭圆；1 饼图是圆形

    pie.slices.strokeColor = colors.red       # 圆饼的边界颜色
    pie.strokeWidth=1                         # 圆饼周围空白区域的宽度
    pie.strokeColor= colors.white             # 整体饼图边界的颜色
    pie.slices.label_pointer_piePad = 10       # 圆饼和标签的距离
    pie.slices.label_pointer_edgePad = 25    # 标签和外边框的距离
    pie.width = width
    pie.direction = 'clockwise'
    pie.pointerLabelMode  = 'LeftRight'
    # for i in range(len(labels)):
    #     pie.slices[i].fontName = 'song' #设置中文
    for i, col in enumerate(use_colors):
         pie.slices[i].fillColor  = col
    return pie


if __name__ == "__main__":
	elements = []

	# 设置上下左右的外边距
	leftMargin = 0.1*inch
	rightMargin = 0.1*inch
	topMargin=0.1*inch
	bottomMargin=0.1* inch

	pdf = SimpleDocTemplate('reportlab_test5.pdf', pagesize=landscape(letter) ,
							leftMargin=leftMargin,rightMargin=rightMargin,topMargin=topMargin, bottomMargin=bottomMargin) #设置页面横向

	title_style = ParagraphStyle(name="TitleStyle", fontName="SimSun", fontSize=48, alignment=TA_LEFT )
	sub_title_style = ParagraphStyle(name="SubTitleStyle", fontName="SimSun", fontSize=32,textColor=colors.HexColor(0x666666), alignment=TA_LEFT)
	content_style = ParagraphStyle(name="ContentStyle", fontName="SimSun", fontSize=18, leading=25, spaceAfter=20,underlineWidth=1, alignment=TA_LEFT )
	foot_style = ParagraphStyle(name="FootStyle", fontName="SimSun", fontSize=14,textColor=colors.HexColor(0xB4B4B4),leading=25, spaceAfter=20, alignment=TA_CENTER)

	page1 = text_test()
	elements.append(page1)
	elements.append(Spacer(1, 10 * mm))
	elements.append(Paragraph("测试报告", title_style))
	elements.append(Spacer(1, 10 * mm))
	elements.append(Paragraph("Test Report of XXX", sub_title_style))
	elements.append(Spacer(1, 15 * mm))
	elements.append(Paragraph("报告编号：" + "007", content_style))
	elements.append(Paragraph("计划名称：" + "xxx软件测试报告", content_style))
	elements.append(Paragraph("报告日期：" + "2019-10-23", content_style))
	elements.append(Paragraph(" 负责人：" + "测试组", content_style))
	elements.append(Spacer(1, 15 * mm))
	elements.append(Paragraph("内部文档，请勿外传", foot_style))
	elements.append(PageBreak())

	# page2 = autoLegender("你好！")
	# elements.append(page2)
	# elements.append(PageBreak())

	# elements.append(Spacer(1, 5.5* inch))
	elements.append(Spacer(1, 1 * mm))
	Style = getSampleStyleSheet()
	n = Style['Normal']
	data = [[0, 1, 2, 3, 4, 5, 6, 7],
			[00, 11, 22, 33, 44, 55, 66, 77],
			[000, 111, 222, 333, 444, 555, 666, 777],
			[0000, 1111, 2222, 3333, 4444, 5555, 6666, 7777], ]
	page3_table = table_model(data)
	elements.append(Paragraph('Title', n))
	elements.append(page3_table)


	data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
	labs = ['0000000', '1111111', '2222222', '3333333', '4444444',
			'5555555', '6666666', '7777777', '8888888', '9999999']
	color = [HexColor("#696969"), HexColor("#A9A9A9"), HexColor("#D8BFD8"),
			 HexColor("#DCDCDC"), HexColor('#E6E6FA'), HexColor("#B0C4DE"),
			 HexColor("#778899"), HexColor('#B0C4DE'), HexColor("#6495ED"),
			 HexColor("#483D8B")
			 ]
	page4 = draw_pie_autoLegender(draw_pie(data, labs, color), "饼状图")
	elements.append(Spacer(1, 2 * inch))
	elements.append(Spacer(1, 2 * inch))
	elements.append(Spacer(1, 2 * inch))

	elements.append(page4)
	elements.append(PageBreak())

	# img = Image('./地云土地报告PPT模板/PPT封面.png')
	# img.drawHeight = 16 * cm
	# img.drawWidth = 33 * cm
	# # img.hAlign = TA_LEFT
	# elements.append(img)
	# text_test = text_test()
	# elements.append(text_test)


	# elements.append(PageBreak())
	#
	# img = Image('./地云土地报告PPT模板/toubu.png')
	# img.drawHeight = 16 * cm
	# img.drawWidth = 33 * cm
	# elements.append(img)
	# elements.append(PageBreak())

	# todo SimpleDocTemplate.build()的方式创建PDF, 目前没法插入背景图片（平铺与拉伸）,也没法在背景图上加文字

	pdf.build(elements)

