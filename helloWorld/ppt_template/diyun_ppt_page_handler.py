import os

from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches
from pptx import Presentation
from pptx.chart.data import ChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.util import Cm  # Inches

from helloWorld.ppt_template.screenshot_test import  getScreenShotForDiyunLandReport


class diyun_ppt_page_handler():

	@staticmethod
	def handler_page_1(slide1):
		slide1_shapes = slide1.shapes
		# 第一页幻灯片处理
		title1 = slide1.shapes[5].text.format(landLocation="白云区白云新城AB2906009地块")
		slide1.shapes[5].text = ""
		p1 = slide1_shapes[5].text_frame.paragraphs[0]
		p1.alignment = PP_ALIGN.CENTER
		run1 = p1.add_run()
		run1.text = title1
		font1 = run1.font
		font1.name = '微软雅黑'
		font1.size = Pt(36)
		font1.bold = True
		font1.color.rgb = RGBColor(255, 255, 255)  # 白色字体

		title1 = slide1.shapes[3].text.format(year=2019, month=10)
		slide1.shapes[3].text = ""
		p1 = slide1_shapes[3].text_frame.paragraphs[0]
		p1.alignment = PP_ALIGN.LEFT
		run1 = p1.add_run()
		run1.text = title1
		font1 = run1.font
		font1.name = '微软雅黑'
		font1.size = Pt(18)
		font1.bold = True
		font1.color.rgb = RGBColor(0, 0, 0)  # 黑色字体
		# font1.underline = True  # 文字下划线
		# font1.italic = None


	@staticmethod
	def handler_page_4(slide4):
		slide4_shapes = slide4.shapes
		text = slide4.shapes[4].text.format(year=2018,city_name='广东省深圳市',year_gdp=13351.35,year_gdp_speed=6.5,per_person_gdp=86552,per_person_gdp_speed=7.6)
		slide4.shapes[4].text = ""
		p1 = slide4_shapes[4].text_frame.paragraphs[0]
		run1 = p1.add_run()
		run1.text = text

	@staticmethod
	def handler_page_27(slide27):
		url = "file:///" + os.getcwd() + os.sep + "baidu_maps_in_ppt.html"
		pic_path = getScreenShotForDiyunLandReport(url)
		top = Inches(0.7)
		left = Inches(0.1)
		width = Inches(6)
		height = Inches(5)
		slide27.shapes.add_picture(pic_path, left, top,width, height)




	@staticmethod
	def handler_test_in_last_page(presentation):
		# 使用默认样式，追加一个空白的ppt,并插入柱状图和表格
		slide = presentation.slides.add_slide(presentation.slide_layouts[6])
		shapes = slide.shapes

		# 定义图表数据 ---------------------
		chart_data = ChartData()
		chart_data.categories = ['East', 'West', 'Midwest']
		chart_data.add_series('Series 1', (19.2, 21.4, 16.7))
		chart_data.add_series('Series 2', (9.2, 2.4, 6.7))

		# 将图表添加到幻灯片 --------------------
		left, top, width, height = Inches(0.2), Inches(1), Inches(4.5), Inches(3.5)
		slide.shapes.add_chart(
			XL_CHART_TYPE.COLUMN_CLUSTERED, left, top, width, height, chart_data
		)

		# 定义表格数据 ------
		name_objects = ["object1", "object2", "object3"]
		name_AIs = ["AI1", "AI2", "AI3"]
		val_AI1 = (19.2, 21.4, 16.7)
		val_AI2 = (22.3, 28.6, 15.2)
		val_AI3 = (20.4, 26.3, 14.2)
		val_AIs = [val_AI1, val_AI2, val_AI3]
		# 表格样式 --------------------
		rows = 4
		cols = 4
		top = Cm(12.5)
		left = Cm(0.5)  # Inches(2.0)
		width = Cm(3)  # Inches(6.0)
		height = Cm(0.8)  # Inches(0.8)

		# 添加表格到幻灯片 --------------------
		table = shapes.add_table(rows, cols, left, top, width, height).table

		# 设置单元格宽度
		table.columns[0].width = Cm(3)  # Inches(2.0)
		table.columns[1].width = Cm(3)
		table.columns[2].width = Cm(3)
		table.columns[3].width = Cm(3)

		# 设置标题行
		table.cell(0, 1).text = name_objects[0]
		table.cell(0, 2).text = name_objects[1]
		table.cell(0, 3).text = name_objects[2]

		# 填充数据
		table.cell(1, 0).text = name_AIs[0]
		table.cell(1, 1).text = str(val_AI1[0])
		table.cell(1, 2).text = str(val_AI1[1])
		table.cell(1, 3).text = str(val_AI1[2])

		table.cell(2, 0).text = name_AIs[1]
		table.cell(2, 1).text = str(val_AI2[0])
		table.cell(2, 2).text = str(val_AI2[1])
		table.cell(2, 3).text = str(val_AI2[2])

		table.cell(3, 0).text = name_AIs[2]
		table.cell(3, 1).text = str(val_AI3[0])
		table.cell(3, 2).text = str(val_AI3[1])
		table.cell(3, 3).text = str(val_AI3[2])


