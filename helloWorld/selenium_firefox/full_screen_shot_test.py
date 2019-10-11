import time

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


def getScreenShot(url):
	'''
	此函数用于根据url访问网页，并截图到本地文件夹
	'''

	options = webdriver.FirefoxProfile()
	brower = webdriver.Firefox(options)
	brower.maximize_window()  # 设置全屏截图
	js_height = "return document.body.clientHeight"
	i = 1
	picName = r"C:\Users\Administrator\Desktop\test_screenshot_" + str(i) + ".png"  # 指定保存文件的文件名
	brower.get(url)  # 获取url


	try:
		brower.get(url)
		k = 1
		height = brower.execute_script(js_height)
		# 获取整张网页的截图，而不只是当前屏幕范围内的
		while True:
			if k * 500 < height:
				js_move = "window.scrollTo(0,{})".format(k * 500)
				print(js_move)
				brower.execute_script(js_move)
				time.sleep(0.2)
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


if __name__ == "__main__":
	url = "https://www.jianshu.com/p/e0dff37273c8"
	getScreenShot(url)