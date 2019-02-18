# -*- coding:utf-8 -*-

from selenium import webdriver
from aip import AipOcr
import os
import urllib.request as request
import io

from PIL import Image


# gif 转 png
def convertImage():
    dirPath = os.getcwd() + "\\images"
    fileList = os.listdir(dirPath)
    for filePath in fileList:
        if filePath.endswith(".gif" ):
            fileFullPath = dirPath + "\\" + filePath
            newFileName = getNewFileName(fileFullPath)
            im = Image.open(fileFullPath)
            for i, frame in enumerate(iter_frames(im)):
                frame.save(os.getcwd() + "\\images\\"+newFileName, **frame.info)
        else:
            continue

def iter_frames(im):
    try:
        i= 0
        while 1:
            im.seek(i)
            imframe = im.copy()
            if i == 0:
                palette = imframe.getpalette()
            else:
                imframe.putpalette(palette)
            yield imframe
            i += 1
    except EOFError:
        pass

def getNewFileName(fileFullPath):
    pos = fileFullPath.rfind("\\")
    fileName = fileFullPath[pos+1:]
    fileName = fileName.replace(".gif",".png")
    return fileName



# """ 读取图片 """
def get_file_content_by_url(imgurl):

    # 建立保存图片的本地路径
    path = os.getcwd()+ '\\images'
    if not os.path.isdir(path):
        os.makedirs(path)
    paths = path + '\\'  # 保存在test路径下
    x = imgurl.split(".")[-1]
    img_path_local = '{}{}.gif'.format(paths, x)
    request.urlretrieve(imgurl, img_path_local) #获取url的文件信息，保存到本地磁盘的文件上
    return img_path_local


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 图片中识别字符
def get_words_from_img(_url):

    img_path_local = get_file_content_by_url(_url)
    convertImage()
    img_path_local = img_path_local.replace(".gif",".png")


    # 当前文件的路径下的图片文件
    image = get_file_content(img_path_local)


    """ 你的 APPID AK SK """
    APP_ID = '11460695'
    API_KEY = 'uZnBPApbqURDfO8mB1vtGOoX'
    SECRET_KEY = 'ksu26AhiugpwOwG5ARVYNHqcRQDP08BT'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    # """ 调用通用文字识别, 图片参数为本地图片 """
    return client.basicGeneral(image)




# create a new Firefox session

# driver = webdriver.Firefox()
# driver.implicitly_wait(10)#设置超时时间
# driver.maximize_window()#窗口最大化显示
#
# #  navigate to the application home page
#
# driver.get("http://www.shenzhentong.com/service/invoice_101007009.html")
# card_num = driver.find_element_by_id("card_num")
# card_num.send_keys("卡号")
# # 执行js，修改隐藏域的值
# driver.execute_script("document.getElementById(\"datepicker\").value='2019-02-13'") # 交易日期
#
# card_num = driver.find_element_by_id("imyzm") #验证码img
#
# identify_code = driver.find_element_by_id("identify_code");
# identify_code.send_keys("请输入验证码")



if __name__ == "__main__":
    result = get_words_from_img("http://www.shenzhentong.com/ajax/WaterMark.ashx?s=0.3850060404971378")
    print(result)
