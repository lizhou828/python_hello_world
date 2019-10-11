import time
import os
from PIL import Image

from selenium import webdriver

# options = webdriver.FirefoxProfile()
# # 打开浏览器
# driver = webdriver.Firefox(options)
# driver.maximize_window()  # 设置浏览器全屏显示
# url = "https://www.jb51.net/article/140366.htm"
# picName = r"C:\Users\Administrator\Desktop\test_screenshot.png"
# driver.get(url)
#
# driver.save_screenshot(picName)  # 使用save_screenshot将浏览器正文部分截图，即使正文本分无法一页显示完全，save_screenshot也可以完全截图

def getScreenShotForDiyunLandReport(url):
	pic_path = getFullScreenShot(url)
	pic_path = getScreenShotWithSpecialArea(pic_path)
	return pic_path

def getFullScreenShot(url):
	'''
	此函数用于根据url访问网页，并下拉全屏截图到本地文件夹
	'''

	options = webdriver.FirefoxProfile()
	brower = webdriver.Firefox(options)
	# brower.maximize_window()  # 设置全屏截图
	js_height = "return document.body.clientHeight"
	i = 1
	picName = "baidu_maps_in_ppt" + str(i) + ".png"  # 指定保存文件的文件名
	brower.get(url)  # 获取url


	try:
		brower.get(url)
		k = 1
		height = brower.execute_script(js_height)
		# 获取整张网页的截图，而不只是当前屏幕范围内的
		while True:
			if k * 500 < height:
				js_move = "window.scrollTo(0,{})".format(k * 500)
				# print(js_move)
				brower.execute_script(js_move)
				time.sleep(0.1)
				height = brower.execute_script(js_height)
				k += 1
			else:
				break
		scroll_width = brower.execute_script('return document.body.parentNode.scrollWidth')
		scroll_height = brower.execute_script('return document.body.parentNode.scrollHeight')
		brower.set_window_size(scroll_width, scroll_height)
		brower.get_screenshot_as_file(picName)
		time.sleep(0.1)
	except Exception as e:
		print(picName, e)

	brower.save_screenshot(picName)  # 保存截图
	brower.close()  # 关闭webdriver
	pic_path = os.getcwd() + os.sep + picName
	return pic_path


def getScreenShotWithSpecialArea(full_screen_snap_pic_path):
	'''
	针对网页，截取指定区域的图片
	参考文档：https://blog.csdn.net/xiongzaiabc/article/details/82912280
	:param pic_path:
	:return:
	'''
	full_screen_snap_pic = Image.open(full_screen_snap_pic_path)
	x0 = 250
	y0 = 90
	x1 = x0 + 800
	y1 = y0 + 680
	image_obj = full_screen_snap_pic.crop((x0, y0, x1, y1))
	image_obj.save(full_screen_snap_pic_path)
	return full_screen_snap_pic_path


if __name__ == "__main__":
	url = "file:///"+os.getcwd() + os.sep + "baidu_maps_in_ppt.html"
	getScreenShotForDiyunLandReport(url)
	# full_screen_snap_pic_path = "baidu_maps_in_ppt1.png"
	# getScreenShotWithSpecialArea(full_screen_snap_pic_path)