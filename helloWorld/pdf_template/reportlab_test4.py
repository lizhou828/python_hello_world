from reportlab.pdfbase import pdfmetrics

from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,Image,Table,TableStyle

from reportlab.lib.pagesizes import letter

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib import colors

from reportlab.graphics.charts.barcharts import VerticalBarChart

from reportlab.graphics.charts.legends import Legend

from reportlab.graphics.shapes import Drawing

# 注册字体
pdfmetrics.registerFont(TTFont('SimSun', "simsun.ttc"))


class Graphs:

	def __init__(self):
		pass

	# 绘制标题

	@staticmethod
	def draw_title():

		style = getSampleStyleSheet()

		ct = style['Normal']

		ct.fontName = 'SimSun'

		ct.fontSize = 18

		# 设置行距

		ct.leading = 50

		# 颜色

		ct.textColor = colors.green

		# 居中

		ct.alignment = 1

		# 添加标题并居中

		title = Paragraph('程序员的兴趣调查报告', ct)

		return title

	# 绘制内容

	@staticmethod
	def draw_text():

		style = getSampleStyleSheet()

		# 常规字体(非粗体或斜体)
		ct = style['Normal']

		# 使用的字体s
		ct.fontName = 'SimSun'
		ct.fontSize = 14

		# 设置自动换行
		ct.wordWrap = 'CJK'

		# 居左对齐
		ct.alignment = 0

		# 第一行开头空格
		ct.firstLineIndent = 32

		# 设置行距
		ct.leading = 30

		text = Paragraph('程序员，是互联网、移动互联网和即将到来的物联网时期的弄潮儿。'
						 '这群特立独行的人才，不知平时最喜欢什么?他们的兴趣真想让人一探究竟。'
						 '经过七七49天的调研，终于形成了一份不具备权威性的统计报告--《程序员2019年上半年兴趣调查报告》，现公布出来，以飨读者。', ct)

		return text


	# 绘制表格
	@staticmethod
	def draw_table(*args):
		col_width = 60
		style = [
			('FONTNAME', (0, 0), (-1, -1), 'SimSun'),  # 字体
			('BACKGROUND', (0, 0), (-1, 0), '#d5dae6'),  # 设置第一行背景颜色
			('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # 对齐
			('VALIGN', (-1, 0), (-2, 0), 'MIDDLE'),  # 对齐
			('GRID', (0, 0), (-1, -1), 0.5, colors.grey),  # 设置表格框线为grey色，线宽为0.5
		]
		table = Table(args, colWidths=col_width, style=style)
		return table

	# 创建图表
	@staticmethod
	def draw_bar(bar_data=[], ax=[], items=[]):
		drawing = Drawing(500, 250)
		bc = VerticalBarChart()
		bc.x = 35
		bc.y = 100
		bc.height = 120
		bc.width = 350
		bc.data = bar_data
		bc.strokeColor = colors.black
		bc.valueAxis.valueMin = 0
		bc.valueAxis.valueMax = 100
		bc.valueAxis.valueStep = 10
		bc.categoryAxis.labels.dx = 8
		bc.categoryAxis.labels.dy = -10
		bc.categoryAxis.labels.angle = 20
		bc.categoryAxis.categoryNames = ax

		# 图示
		leg = Legend()
		leg.fontName = 'SimSun'
		leg.alignment = 'right'
		leg.boxAnchor = 'ne'
		leg.x = 465
		leg.y = 220
		leg.dxTextSpace = 10
		leg.columnMaximum = 3
		leg.colorNamePairs = items
		drawing.add(leg)
		drawing.add(bc)
		return drawing

if __name__ == "__main__":
		content = list()

		# 添加标题
		content.append(Graphs.draw_title())

		# 添加段落
		content.append(Graphs.draw_text())

		# 添加表格数据
		data = [('兴趣', '2019-1', '2019-2', '2019-3', '2019-4', '2019-5', '2019-6'),
				('开发', 50, 80, 60, 35, 40, 45),
				('编程', 25, 60, 55, 45, 60, 80),
				('敲代码', 30, 90, 75, 80, 50, 46)]

		content.append(Graphs.draw_table(*data))

		# 添加图表
		b_data = [(50, 80, 60, 35, 40, 45), (25, 60, 55, 45, 60, 80), (30, 90, 75, 80, 50, 46)]
		ax_data = ['2019-1', '2019-2', '2019-3', '2019-4', '2019-5', '2019-6']
		leg_items = [(colors.red, '开发'), (colors.green, '编程'), (colors.blue, '敲代码')]
		content.append(Graphs.draw_bar(b_data, ax_data, leg_items))

		# 生成pdf文件
		doc = SimpleDocTemplate('reportlab_test4.pdf', pagesize=letter)
		doc.build(content)

# 作者：我如实说
# 链接：https://www.jianshu.com/p/a09186fc3131
# 来源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
