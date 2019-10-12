import os

from pptx.dml.color import RGBColor
from pptx.shapes.graphfrm import GraphicFrame
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches
from pptx import Presentation
from pptx.chart.data import ChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.enum.chart import XL_LEGEND_POSITION
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

		data_dict={"area_14":"12","area_15":"13","area_16":"14","area_17":"15","area_18":"16",
				   "area_14s":"0.2","area_15s":"0.3","area_16s":"0.4","area_17s":"0.5","area_18s":"0.6",
				   "per_14":"22","per_15":"13","per_16":"14","per_17":"15","per_18":"26",
				   "per_14s":"2.2","per_15s":"0.3","per_16s":"0.4","per_17s":"0.5","per_18s":"2.6",}
		graphicFrames = slide4.shapes
		for graphicFrame in graphicFrames:
			if type(graphicFrame) != GraphicFrame or not graphicFrame.has_table:
				continue
			for cell in diyun_ppt_page_handler.iter_cells(graphicFrame.table):
				if "{" not in cell.text and "}" not in cell.text:
					continue
				cell.text = cell.text.format(**data_dict)

			for cell in diyun_ppt_page_handler.iter_cells(graphicFrame.table):
				for paragraph in cell.text_frame.paragraphs:
					for run in paragraph.runs:
						run.font.size = Pt(12)
						run.font.color.rgb = RGBColor(0, 0, 0)  # 黑色字体

	@staticmethod
	def handler_page_5(slide5):
		# 堆积柱形图：定义图表数据 ---------------------
		chart_data = ChartData()
		chart_data.categories = ['2014', '2015', '2016', '2017', '2018']
		production1data = (19.2, 21.4, 16.7,13,15)
		production2data = (9.2, 2.4, 6.7,12,13.5)
		production3data = (9.2, 2.4, 6.7,14.1,5.2)
		productionDataMap ={}
		productionDataMap["production1data"] = production1data
		productionDataMap["production2data"] = production2data
		productionDataMap["production3data"] = production3data

		chart_data.add_series('第一产业', production1data)
		chart_data.add_series('第二产业', production2data)
		chart_data.add_series('第三产业', production3data)


		# 堆积柱形图：将图表添加到幻灯片 --------------------
		left, top, width, height = Inches(1), Inches(1.3), Inches(8), Inches(3.5)
		graphic_frame = slide5.shapes.add_chart(
			XL_CHART_TYPE.COLUMN_STACKED, left, top, width, height, chart_data
		)
		chart = graphic_frame.chart
		chart.has_legend = True
		chart.legend.position = XL_LEGEND_POSITION.BOTTOM
		chart.legend.include_in_layout = False
		graphic_frame.has_title = True
		graphic_frame.chart.chart_title.text_frame.text = "深圳市产业结构"


		# 定制柱状图颜色
		colors = {}
		colors['第一产业'] = 'FFD700'
		colors['第二产业'] = '32CD32'
		colors['第三产业'] = '1E90FF'
		for series in chart.series:
			if series.name in colors:
				fill = series.format.fill  # fill the legend as well
				fill.solid()
				fill.fore_color.rgb = RGBColor.from_string(colors[series.name])


		# 把数据填充到table中
		graphicFrames = slide5.shapes
		for graphicFrame in graphicFrames:
			if type(graphicFrame) != GraphicFrame or not graphicFrame.has_table:
				continue
			for row_index in range(len(graphicFrame.table.rows)):
				if row_index == 0:
					continue
				row_data = productionDataMap.get("production{}data".format(row_index))
				for column_index in range(len(graphicFrame.table.rows[row_index].cells)):
					if column_index == 0:
						continue
					# 插入数据到 每个单元格
					graphicFrame.table.rows[row_index].cells[column_index].text = str(row_data[column_index-1])

					# 处理 每个单元格 的样式
					for paragraph in graphicFrame.table.rows[row_index].cells[column_index].text_frame.paragraphs:
						for run in paragraph.runs:
							run.font.size = Pt(12)
							run.font.color.rgb = RGBColor(0, 0, 0)  # 黑色字体

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
					 "contract_signing_date":"2019-06-25 00:00:00","transaction_price":"280807.0000","land_owner":"广州市瑞业房地产开发有限公司","floor_area_price":"","premium_rate":"0.13"}

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
	def handler_page_16(slide16):
		land_datas = []
		land_data1 = {'land_location': '白云区白云新城AB2906009地块', "land_sn": "ab2906009", "land_use_details": "城镇住宅用地", "type": "挂牌",
		 "land_total_area": "67695.0000",
		 "sale_time": "70", "plot_ratio": "大于1并且小于或等于5.5", "building_density": "小于或等于30", "greening_rate": "大于或等于35",
		 "building_limited_height": "小于或等于120",
		 "open_end_time": "2019-06-14 10:00:00", "cash_deposit": "12300.0000", "publish_time": "2019-05-16 00:00:00",
		 "open_start_time": "2019-06-04 00:00:00", "starting_price": "193660.0000", "price_increase": "3000.0000",
		 "contract_signing_date": "2019-06-25 00:00:00", "transaction_price": "280807.0000",
		 "land_owner": "广州市瑞业房地产开发有限公司", "floor_area_price": "", "premium_rate": "0.13","lng": "113.1051556943977", "lat": "23.0192965357819"}
		land_datas.append(land_data1)

	@staticmethod
	def handler_page_18(slide18):
		table_data = []
		row_data1 = {"name":"东方盛世花园二期","time":"2018-10-08","type":"板楼","price":"73638.73","lng":"113.1051556943977","lat":"23.0192965357819"}
		table_data.append(row_data1)
		row_data2 = {"name":"深业泰富广场","time":"2019-08-08","type":"板塔结合","price":"59228.69","lng":"113.1051356943977","lat":"23.0191965357819"}
		table_data.append(row_data2)
		row_data3 = {"name": "深业泰富广场", "time": "2019-08-08", "type": "板塔结合", "price": "59228.69", "lng": "113.1051356943977", "lat": "23.0191965357819"}
		table_data.append(row_data3)
		row_data4 = {"name": "深业泰富广场", "time": "2019-08-08", "type": "板塔结合", "price": "59228.69","lng": "113.1051356943977", "lat": "23.0191965357819"}
		table_data.append(row_data4)
		row_data5 = {"name": "深业泰富广场", "time": "2019-08-08", "type": "板塔结合", "price": "59228.69","lng": "113.1051356943977", "lat": "23.0191965357819"}
		table_data.append(row_data5)

		row_data6 = {"name": "深业泰富广场", "time": "2019-08-08", "type": "板塔结合", "price": "59228.69","lng": "113.1051356943977", "lat": "23.0191965357819"}
		table_data.append(row_data6)
		row_data7 = {"name": "深业泰富广场", "time": "2019-08-08", "type": "板塔结合", "price": "59228.69","lng": "113.1051356943977", "lat": "23.0191965357819"}
		table_data.append(row_data7)
		row_data8 = {"name": "深业泰富广场", "time": "2019-08-08", "type": "板塔结合", "price": "59228.69","lng": "113.1051356943977", "lat": "23.0191965357819"}
		table_data.append(row_data8)
		row_data9 = {"name": "深业泰富广场", "time": "2019-08-08", "type": "板塔结合", "price": "59228.69","lng": "113.1051356943977", "lat": "23.0191965357819"}
		table_data.append(row_data9)
		row_data10 = {"name": "深业泰富广场", "time": "2019-08-08", "type": "板塔结合", "price": "59228.69","lng": "113.1051356943977", "lat": "23.0191965357819"}
		table_data.append(row_data10)

		# 表格样式 --------------------
		rows = len(table_data)+1
		cols = 5
		top = Cm(2)
		left = Cm(13.5)  # Inches(2.0)
		width = Cm(10)  # Inches(6.0)
		height = Cm(2)  # Inches(0.8)

		# 添加表格到幻灯片 --------------------
		table = slide18.shapes.add_table(rows, cols, left, top, width, height).table
		# 设置单元格宽度
		table.columns[0].width = Cm(1.5)  # Inches(2.0)
		table.columns[1].width = Cm(3)
		table.columns[2].width = Cm(3)
		table.columns[3].width = Cm(2)
		table.columns[4].width = Cm(2.5)

		# 插入数据到table
		for row_index in range(len(table.rows)):
			if row_index == 0:
				table.rows[row_index].cells[0].text="编号"
				table.rows[row_index].cells[1].text = "名称"
				table.rows[row_index].cells[2].text = "开盘时间"
				table.rows[row_index].cells[3].text = "产品类型"
				table.rows[row_index].cells[4].text = "成交价格(元/㎡)"
				continue
			for cell_index in range(len(table.rows[row_index].cells)):
				if cell_index == 0:
					table.rows[row_index].cells[cell_index].text = str(row_index)
				if cell_index == 1:
					table.rows[row_index].cells[cell_index].text = table_data[row_index-1].get("name")
				if cell_index == 2:
					table.rows[row_index].cells[cell_index].text = table_data[row_index-1].get("time")
				if cell_index == 3:
					table.rows[row_index].cells[cell_index].text = table_data[row_index-1].get("type")
				if cell_index == 4:
					table.rows[row_index].cells[cell_index].text = table_data[row_index-1].get("price")

		# 处理table的样式、字体等
		for cell in diyun_ppt_page_handler.iter_cells(table):
					for paragraph in cell.text_frame.paragraphs:
						for run in paragraph.runs:
							run.font.size = Pt(12)
							run.font.color.rgb = RGBColor(0, 0, 0)  # 黑色字体

	@staticmethod
	def handler_page_20(slide20):
		table_data = []
		row_data1 = {"name":"宝安国际机场（飞机场）","distance":"0.8","lng":"113.1051556943977","lat":"23.0192965357819"}
		table_data.append(row_data1)
		row_data2 = {"name":"龙塘新村西(公交站)","distance":"1.8","lng":"113.1051356943977","lat":"23.0191965357819"}
		table_data.append(row_data2)
		row_data3 = {"name": "红山地铁站(公交站)", "distance":"2.8","lng": "113.1051356943977", "lat": "23.0191965357819"}
		table_data.append(row_data3)
		row_data4 = {"name": "深业泰富广场(公交站)", "distance":"3.8","lng": "113.1051356943977", "lat": "23.0191965357819"}
		table_data.append(row_data4)

		# 表格样式 --------------------
		rows = len(table_data)+1
		cols = 3
		top = Cm(2)
		left = Cm(16)  # Inches(2.0)
		width = Cm(10)  # Inches(6.0)
		height = Cm(2)  # Inches(0.8)

		# 添加表格到幻灯片 --------------------
		table = slide20.shapes.add_table(rows, cols, left, top, width, height).table
		# 设置单元格宽度
		table.columns[0].width = Cm(2)  # Inches(2.0)
		table.columns[1].width = Cm(4)
		table.columns[2].width = Cm(3)

		# 插入数据到table
		for row_index in range(len(table.rows)):
			if row_index == 0:
				table.rows[row_index].cells[0].text="编号"
				table.rows[row_index].cells[1].text = "名称"
				table.rows[row_index].cells[2].text = "距离(km)"
				continue
			for cell_index in range(len(table.rows[row_index].cells)):
				if cell_index == 0:
					table.rows[row_index].cells[cell_index].text = str(row_index)
				if cell_index == 1:
					table.rows[row_index].cells[cell_index].text = table_data[row_index-1].get("name")
				if cell_index == 2:
					table.rows[row_index].cells[cell_index].text = table_data[row_index-1].get("distance")

		# 处理table的样式、字体等
		for cell in diyun_ppt_page_handler.iter_cells(table):
					for paragraph in cell.text_frame.paragraphs:
						for run in paragraph.runs:
							run.font.size = Pt(12)
							run.font.color.rgb = RGBColor(0, 0, 0)  # 黑色字体

	@staticmethod
	def handler_page_21(slide21):
		table_data = []
		row_data1 = {"name":"和平实验小学","distance":"0.8","lng":"113.1051556943977","lat":"23.0192965357819"}
		table_data.append(row_data1)
		row_data2 = {"name":"民治小学","distance":"1.8","lng":"113.1051356943977","lat":"23.0191965357819"}
		table_data.append(row_data2)
		row_data3 = {"name": "深圳高级中学(集团)北校区", "distance":"2.8","lng": "113.1051356943977", "lat": "23.0191965357819"}
		table_data.append(row_data3)
		row_data4 = {"name": "希望中学", "distance":"3.8","lng": "113.1051356943977", "lat": "23.0191965357819"}
		table_data.append(row_data4)

		# 表格样式 --------------------
		rows = len(table_data)+1
		cols = 3
		top = Cm(2)
		left = Cm(16)  # Inches(2.0)
		width = Cm(10)  # Inches(6.0)
		height = Cm(2)  # Inches(0.8)

		# 添加表格到幻灯片 --------------------
		table = slide21.shapes.add_table(rows, cols, left, top, width, height).table
		# 设置单元格宽度
		table.columns[0].width = Cm(2)  # Inches(2.0)
		table.columns[1].width = Cm(4)
		table.columns[2].width = Cm(3)

		# 插入数据到table
		for row_index in range(len(table.rows)):
			if row_index == 0:
				table.rows[row_index].cells[0].text="编号"
				table.rows[row_index].cells[1].text = "名称"
				table.rows[row_index].cells[2].text = "距离(km)"
				continue
			for cell_index in range(len(table.rows[row_index].cells)):
				if cell_index == 0:
					table.rows[row_index].cells[cell_index].text = str(row_index)
				if cell_index == 1:
					table.rows[row_index].cells[cell_index].text = table_data[row_index-1].get("name")
				if cell_index == 2:
					table.rows[row_index].cells[cell_index].text = table_data[row_index-1].get("distance")

		# 处理table的样式、字体等
		for cell in diyun_ppt_page_handler.iter_cells(table):
					for paragraph in cell.text_frame.paragraphs:
						for run in paragraph.runs:
							run.font.size = Pt(12)
							run.font.color.rgb = RGBColor(0, 0, 0)  # 黑色字体


	@staticmethod
	def handler_page_22(slide22):
		table_data = []
		row_data1 = {"name":"深圳市第一人民医院","distance":"0.8","lng":"113.1051556943977","lat":"23.0192965357819"}
		table_data.append(row_data1)
		row_data2 = {"name":"龙岗人民医院","distance":"1.8","lng":"113.1051356943977","lat":"23.0191965357819"}
		table_data.append(row_data2)
		row_data3 = {"name": "香港中文大学附属第一人民医院", "distance":"2.8","lng": "113.1051356943977", "lat": "23.0191965357819"}
		table_data.append(row_data3)
		row_data4 = {"name": "南方科技大学附属第一人民医院", "distance":"3.8","lng": "113.1051356943977", "lat": "23.0191965357819"}
		table_data.append(row_data4)

		# 表格样式 --------------------
		rows = len(table_data)+1
		cols = 3
		top = Cm(2)
		left = Cm(16)  # Inches(2.0)
		width = Cm(10)  # Inches(6.0)
		height = Cm(2)  # Inches(0.8)

		# 添加表格到幻灯片 --------------------
		table = slide22.shapes.add_table(rows, cols, left, top, width, height).table
		# 设置单元格宽度
		table.columns[0].width = Cm(2)  # Inches(2.0)
		table.columns[1].width = Cm(4)
		table.columns[2].width = Cm(3)

		# 插入数据到table
		for row_index in range(len(table.rows)):
			if row_index == 0:
				table.rows[row_index].cells[0].text="编号"
				table.rows[row_index].cells[1].text = "名称"
				table.rows[row_index].cells[2].text = "距离(km)"
				continue
			for cell_index in range(len(table.rows[row_index].cells)):
				if cell_index == 0:
					table.rows[row_index].cells[cell_index].text = str(row_index)
				if cell_index == 1:
					table.rows[row_index].cells[cell_index].text = table_data[row_index-1].get("name")
				if cell_index == 2:
					table.rows[row_index].cells[cell_index].text = table_data[row_index-1].get("distance")

		# 处理table的样式、字体等
		for cell in diyun_ppt_page_handler.iter_cells(table):
					for paragraph in cell.text_frame.paragraphs:
						for run in paragraph.runs:
							run.font.size = Pt(12)
							run.font.color.rgb = RGBColor(0, 0, 0)  # 黑色字体

	@staticmethod
	def handler_page_23(slide23):
		table_data = []
		row_data1 = {"name": "九方购物中心(人民路)", "distance": "0.8", "lng": "113.1051556943977", "lat": "23.0192965357819"}
		table_data.append(row_data1)
		row_data2 = {"name": "中海环宇新天地", "distance": "1.8", "lng": "113.1051356943977", "lat": "23.0191965357819"}
		table_data.append(row_data2)
		row_data3 = {"name": "U·ONE优城", "distance": "2.8", "lng": "113.1051356943977", "lat": "23.0191965357819"}
		table_data.append(row_data3)
		row_data4 = {"name": "汇龙时代广场", "distance": "3.8", "lng": "113.1051356943977", "lat": "23.0191965357819"}
		table_data.append(row_data4)

		# 表格样式 --------------------
		rows = len(table_data) + 1
		cols = 3
		top = Cm(2)
		left = Cm(16)  # Inches(2.0)
		width = Cm(10)  # Inches(6.0)
		height = Cm(2)  # Inches(0.8)

		# 添加表格到幻灯片 --------------------
		table = slide23.shapes.add_table(rows, cols, left, top, width, height).table
		# 设置单元格宽度
		table.columns[0].width = Cm(2)  # Inches(2.0)
		table.columns[1].width = Cm(4)
		table.columns[2].width = Cm(3)

		# 插入数据到table
		for row_index in range(len(table.rows)):
			if row_index == 0:
				table.rows[row_index].cells[0].text = "编号"
				table.rows[row_index].cells[1].text = "名称"
				table.rows[row_index].cells[2].text = "距离(km)"
				continue
			for cell_index in range(len(table.rows[row_index].cells)):
				if cell_index == 0:
					table.rows[row_index].cells[cell_index].text = str(row_index)
				if cell_index == 1:
					table.rows[row_index].cells[cell_index].text = table_data[row_index - 1].get("name")
				if cell_index == 2:
					table.rows[row_index].cells[cell_index].text = table_data[row_index - 1].get("distance")

		# 处理table的样式、字体等
		for cell in diyun_ppt_page_handler.iter_cells(table):
			for paragraph in cell.text_frame.paragraphs:
				for run in paragraph.runs:
					run.font.size = Pt(12)
					run.font.color.rgb = RGBColor(0, 0, 0)  # 黑色字体

	@staticmethod
	def handler_page_24(slide24):
		table_data = []
		row_data1 = {"name": "深圳市福田区政府", "distance": "0.8", "lng": "113.1051556943977", "lat": "23.0192965357819"}
		table_data.append(row_data1)
		row_data2 = {"name": "深圳市南山区政府", "distance": "1.8", "lng": "113.1051356943977", "lat": "23.0191965357819"}
		table_data.append(row_data2)
		row_data3 = {"name": "深圳市宝安区政府", "distance": "2.8", "lng": "113.1051356943977", "lat": "23.0191965357819"}
		table_data.append(row_data3)
		row_data4 = {"name": "宝山街道居委会", "distance": "3.8", "lng": "113.1051356943977", "lat": "23.0191965357819"}
		table_data.append(row_data4)

		# 表格样式 --------------------
		rows = len(table_data) + 1
		cols = 3
		top = Cm(2)
		left = Cm(16)  # Inches(2.0)
		width = Cm(10)  # Inches(6.0)
		height = Cm(2)  # Inches(0.8)

		# 添加表格到幻灯片 --------------------
		table = slide24.shapes.add_table(rows, cols, left, top, width, height).table
		# 设置单元格宽度
		table.columns[0].width = Cm(2)  # Inches(2.0)
		table.columns[1].width = Cm(4)
		table.columns[2].width = Cm(3)

		# 插入数据到table
		for row_index in range(len(table.rows)):
			if row_index == 0:
				table.rows[row_index].cells[0].text = "编号"
				table.rows[row_index].cells[1].text = "名称"
				table.rows[row_index].cells[2].text = "距离(km)"
				continue
			for cell_index in range(len(table.rows[row_index].cells)):
				if cell_index == 0:
					table.rows[row_index].cells[cell_index].text = str(row_index)
				if cell_index == 1:
					table.rows[row_index].cells[cell_index].text = table_data[row_index - 1].get("name")
				if cell_index == 2:
					table.rows[row_index].cells[cell_index].text = table_data[row_index - 1].get("distance")

		# 处理table的样式、字体等
		for cell in diyun_ppt_page_handler.iter_cells(table):
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


