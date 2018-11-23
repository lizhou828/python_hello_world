from aip import AipOcr
import os


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

#Windows下Python程序读取中文文件
# image = get_file_content(u'C:\\Users\\Administrator\\Desktop\\无标题.png')

# 当前文件的路径下的图片文件
image = get_file_content(os.getcwd()+ r"\株国土拟征[2018]038号.jpg")

""" 你的 APPID AK SK """
APP_ID = '11460695'
API_KEY = 'uZnBPApbqURDfO8mB1vtGOoX'
SECRET_KEY = 'ksu26AhiugpwOwG5ARVYNHqcRQDP08BT'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
# """ 调用通用文字识别, 图片参数为本地图片 """
result = client.basicGeneral(image);
print(result)

# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"
#
# """ 带参数调用通用文字识别, 图片参数为本地图片 """
# client.basicGeneral(image, options)



# url = "https//www.x.com/sample.jpg"
# """ 调用通用文字识别, 图片参数为远程url图片 """
# client.basicGeneralUrl(url);
#
# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"
#
# """ 带参数调用通用文字识别, 图片参数为远程url图片 """
# client.basicGeneralUrl(url, options)

