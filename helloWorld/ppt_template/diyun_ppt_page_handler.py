import os

from pptx.dml.color import RGBColor
from pptx.shapes.graphfrm import GraphicFrame
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
	def iter_cells(table):
		'''
		遍历table中的每一个单元格
		:param table:
		:return:
		'''
		for row in table.rows:
			for cell in row.cells:
				yield cell

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
	def handler_page_12(slide12):
		# url = "file:///" + os.getcwd() + os.sep + "baidu_maps_in_ppt.html"
		# pic_path = getScreenShotForDiyunLandReport(url)

		pic_path = "baidu_maps_in_ppt1.png"  # 指定保存文件的文件名

		top = Inches(0.7)
		left = Inches(0.1)
		width = Inches(6)
		height = Inches(5)
		slide12.shapes.add_picture(pic_path, left, top, width, height)

	@staticmethod
	def handler_page_14(slide14):
		# 表格样式 --------------------
		rows = 11
		cols = 2
		top = Inches(0.6)
		left = Inches(0.3)
		width = Cm(30)  # Inches(6.0)
		height = Cm(6)  # Inches(0.8)

		# 添加表格到幻灯片 --------------------
		table = slide14.shapes.add_table(rows, cols, left, top, width, height).table
		# 设置单元格宽度
		table.columns[0].width = Cm(12)  # Inches(2.0)
		table.columns[1].width = Cm(12)

		cell00 = table.cell(0, 0)
		cell00.text= "技术经济指标"
		cell01 = table.cell(0, 1)
		cell00.merge(cell01)
		p1 = cell00.text_frame.paragraphs[0]
		p1.alignment = PP_ALIGN.CENTER

		table.cell(1, 0).text = "地块名称"
		table.cell(1, 1).text = ""
		table.cell(2, 0).text = "地块编号"
		table.cell(2, 1).text = ""
		table.cell(3, 0).text = "用地性质"
		table.cell(3, 1).text = ""
		table.cell(4, 0).text = "出让方式"
		table.cell(4, 1).text = ""
		table.cell(5, 0).text = "建设用地面积"
		table.cell(5, 1).text = ""
		table.cell(6, 0).text = "规划建筑面积"
		table.cell(6, 1).text = ""
		table.cell(7, 0).text = "容积率"
		table.cell(7, 1).text = ""
		table.cell(8, 0).text = "建筑密度"
		table.cell(8, 1).text = ""
		table.cell(9, 0).text = "绿化率"
		table.cell(9, 1).text = ""
		table.cell(10, 0).text = "限高"
		table.cell(10, 1).text = ""

		for cell in diyun_ppt_page_handler.iter_cells(table):
			for paragraph in cell.text_frame.paragraphs:
				for run in paragraph.runs:
					run.font.size = Pt(12)
					run.font.color.rgb = RGBColor(0, 0, 0)  # 黑色字体




		# 表格样式 --------------------
		rows = 4
		cols = 4
		top = Inches(5.1)
		left = Inches(0.3)
		width = Cm(15)  # Inches(6.0)
		height = Cm(4)  # Inches(0.8)

		# 添加表格到幻灯片 --------------------
		table1 = slide14.shapes.add_table(rows, cols, left, top, width, height).table
		# 设置单元格宽度
		table1.columns[0].width = Cm(3)  # Inches(2.0)
		table1.columns[1].width = Cm(3)
		table1.columns[2].width = Cm(3)
		table1.columns[3].width = Cm(3)

		cell00 = table1.cell(0, 0)
		cell00.text = "挂牌信息"
		cell03 = table1.cell(0, 3)
		cell00.merge(cell03)
		p1 = cell00.text_frame.paragraphs[0]
		p1.alignment = PP_ALIGN.CENTER

		table1.cell(1, 0).text = "截止时间"
		table1.cell(1, 1).text = ""
		table1.cell(1, 2).text = "保证金"
		table1.cell(1, 3).text = ""
		table1.cell(2, 0).text = "公告时间"
		table1.cell(2, 1).text = ""
		table1.cell(2, 2).text = "起始时间"
		table1.cell(2, 3).text = ""
		table1.cell(3, 0).text = "起始价"
		table1.cell(3, 1).text = ""
		table1.cell(3, 2).text = "推出楼面价"
		table1.cell(3, 3).text = ""
		for cell in diyun_ppt_page_handler.iter_cells(table1):
			for paragraph in cell.text_frame.paragraphs:
				for run in paragraph.runs:
					run.font.size = Pt(12)
					run.font.color.rgb = RGBColor(0, 0, 0)  # 黑色字体

	@staticmethod
	def handler_page_14_new(slide14):
		data_dict = {'land_location':'白云区白云新城AB2906009地块',"land_sn":"ab2906009","land_use_details":"城镇住宅用地","type":"挂牌","land_total_area":"67695.0000",
					 "sale_time":"70","plot_ratio":"大于1并且小于或等于5.5","building_density":"小于或等于30","greening_rate":"大于或等于35","building_limited_height":"小于或等于120",
					 "open_end_time":"2019-06-14 10:00:00","cash_deposit":"12300.0000","publish_time":"2019-05-16 00:00:00","open_start_time":"2019-06-04 00:00:00","starting_price":"193660.0000","price_increase":"3000.0000",
					 "contract_signing_date":"2019-06-25 00:00:00","transaction_price":"280807.0000","land_owner":"广州市瑞业房地产开发有限公司","floor_area_price":"","premium_rate":""}

		graphicFrames = slide14.shapes
		for graphicFrame in graphicFrames:
			if type(graphicFrame) != GraphicFrame or not graphicFrame.has_table:
				continue
			for cell in diyun_ppt_page_handler.iter_cells(graphicFrame.table):
				if "{" not in cell.text and "}" not in cell.text:
					continue
				cell.text = cell.text.format(**data_dict)
				# for paragraph in cell.text_frame.paragraphs:
				# 	for run in paragraph.runs:
				# 		run.text = run.text.format(data_dict)
						# run.font.size = Pt(12)
						# run.font.color.rgb = RGBColor(0, 0, 0)  # 黑色字体

			for cell in diyun_ppt_page_handler.iter_cells(graphicFrame.table):
				for paragraph in cell.text_frame.paragraphs:
					for run in paragraph.runs:
						run.font.size = Pt(12)
						run.font.color.rgb = RGBColor(0, 0, 0)  # 黑色字体



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


