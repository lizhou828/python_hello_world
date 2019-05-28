# -*- coding:utf-8 -*-

"""

selenium+python破解滑动验证码
https://www.jianshu.com/p/832b76dfe6a1?from=timeline

Python——破解极验滑动验证码
https://www.cnblogs.com/xiao-apple36/p/8878960.html

@Function:
@File    :          AJK_Slide_Captcha.py    
@Contact :          lizhou@glorypty.com
@License :          (C)Copyright 2019-2020

@Modify Time        @Author      @Version        @Desciption
------------        -------      --------        -----------
2019-5-24 13:50     lizhou         1.0         

"""


import random
from io import BytesIO
import json
import re
import time
from urllib.request import urlretrieve

from PIL import Image,ImageGrab
import requests
import execjs
import os
import base64
import cv2
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

import pyautogui
# pip install pyautogui

def get_image(driver,div_path,image_name):
    '''
    下载图片
    :param driver:
    :param div_path:
    :return:
    '''
    time.sleep(2)
    background_image = driver.find_elements_by_xpath(div_path)
    image_url = background_image[0].get_attribute('src')
    # urlretrieve(url=image_url, filename=image_name)

    # response = requests.get(image_url)
    #
    #
    # # 内存中打开图片
    # image = Image.open(BytesIO(response.content))
    #
    #
    # # 图片的base64编码
    # ls_f = base64.b64encode(BytesIO(response.content).read())
    #
    # # base64编码解码
    # imgdata = base64.b64decode(ls_f)
    #
    # # 图片文件保存
    # file = open(image_name+'.jpg','wb')
    # file.write(imgdata)
    # file.close()
    # return image


def get_position(image):
    image = image.resize((284, 160))
    image = image.convert('L')
    yuzhi = 150
    yuzhi2 = 40
    ll = 10
    for i in range(55, image.size[0] - 20):  # 260
        for j in range(0, image.size[1] - 20):  # 160
            flag = True
            for l in range(0, ll):
                pixel = image.getpixel((i, j)) - image.getpixel((i + 1, j + l))
                if pixel < yuzhi2: flag = False
                # pixel = image.getpixel((i - l, j))
                # if pixel<yuzhi:flag=False
            for l in range(0, ll):
                pixel = image.getpixel((i, j + l))
                if pixel < yuzhi: flag = False

            if flag:
                cropedimage = image.crop((i, j, i + 30, j + 30))
                return i - 7


def get_distance(image1,image2):
    '''
      拿到滑动验证码需要移动的距离
      :param image1:没有缺口的图片对象
      :param image2:带缺口的图片对象
      :return:需要移动的距离
      '''
    # print('size', image1.size)

    threshold = 50
    for i in range(0,image1.size[0]):  # 260
        for j in range(0,image1.size[1]):  # 160
            pixel1 = image1.getpixel((i,j))
            pixel2 = image2.getpixel((i,j))
            res_R = abs(pixel1[0]-pixel2[0]) # 计算RGB差
            res_G = abs(pixel1[1] - pixel2[1])  # 计算RGB差
            res_B = abs(pixel1[2] - pixel2[2])  # 计算RGB差
            if res_R > threshold and res_G > threshold and res_B > threshold:
                return i  # 需要移动的距离

def get_track(distance):
    '''
    拿到移动轨迹，模仿人的滑动行为，先匀加速后匀减速
    匀变速运动基本公式：
    ①v=v0+at
    ②s=v0t+(1/2)at²
    ③v²-v0²=2as

    :param distance: 需要移动的距离
    :return: 存放每0.2秒移动的距离
    '''
    # 初速度
    v=0
    # 单位时间为0.2s来统计轨迹，轨迹即0.2内的位移
    t=0.2
    # 位移/轨迹列表，列表内的一个元素代表0.2s的位移
    tracks=[]
    # 当前的位移
    current=0
    # 到达mid值开始减速
    mid=distance * 7/8

    distance += 10  # 先滑过一点，最后再反着滑动回来
    # a = random.randint(1,3)
    while current < distance:
        if current < mid:
            # 加速度越小，单位时间的位移越小,模拟的轨迹就越多越详细
            a = random.randint(2,4)  # 加速运动
        else:
            a = -random.randint(3,5) # 减速运动

        # 初速度
        v0 = v
        # 0.2秒时间内的位移
        s = v0*t+0.5*a*(t**2)
        # 当前的位置
        current += s
        # 添加到轨迹列表
        tracks.append(round(s))

        # 速度已经达到v,该速度作为下次的初速度
        v= v0+a*t

    # 反着滑动到大概准确位置
    for i in range(4):
       tracks.append(-random.randint(2,3))
    for i in range(4):
       tracks.append(-random.randint(1,3))
    return tracks

def AJK_Slide_Captcha_run():
# AJK_Slide_Captcha().run()
    # 您校验错误的次数太多了,请刷新页面

    big_img_path = r"C:\Users\Administrator\Downloads\captcha_img.jpg"
    small_img_path = r"C:\Users\Administrator\Downloads\captcha_img.png"
    if os.path.exists(big_img_path):
        os.remove(big_img_path)

    if os.path.exists(small_img_path):
        os.remove(small_img_path)


    # driver = webdriver.Firefox(profile)
    driver = webdriver.Firefox()

    # driver.implicitly_wait(10) # 隐性等待，最长等10秒
    # 隐形等待是设置了一个最长等待时间，如果在规定时间内网页加载完成，则执行下一步，否则一直等到时间截止，然后执行下一步。注意这里有一个弊端，那就是程序会一直等待整个页面加载完成，也就是一般情况下你看到浏览器标签栏那个小圈不再转，才会执行下一步，但有时候页面想要的元素早就在加载完成了，但是因为个别js之类的东西特别慢，我仍得等到页面全部完成才能执行下一步，我想等我要的元素出来之后就下一步怎么办？有办法，这就要看selenium提供的另一种等待方式——显性等待wait了
    # 需要特别说明的是：隐性等待对整个driver的周期都起作用，所以只要设置一次即可，我曾看到有人把隐性等待当成了sleep在用，走哪儿都来一下…

    driver.maximize_window()#窗口最大化显示
    try:
        driver.get('https://www.anjuke.com/captcha-verify/?callback=shield&from=antispam')
        # 强制等待,等待网页加载完成后，再去处理
        time.sleep(5)

        scrollElement = driver.find_elements_by_class_name('dvc-slider__handler')[0]

        # 1 图片上 缺口的位置的x坐标(需要下载图片)

    #     # 使用pyautogui来右键鼠标下载
    #     # 执行鼠标动作
        click_locxy(driver,850,200)
        # actions = ActionChains(driver)

        pyautogui.typewrite(['down','down','down','down','enter','enter'])
    #     # 单击图片另存之后等1s敲回车
        time.sleep(1)
        pyautogui.typewrite(['enter'])
    #
    #
        pyautogui.press('esc')
    #
        click_locxy(driver,1000,200)
        pyautogui.typewrite(['down','down','down','down','enter','enter'])
    #     # 单击图片另存之后等1s敲回车
        time.sleep(1)
        pyautogui.typewrite(['enter'])


         # 2 对比两张图片的所有RBG像素点，得到不一样像素点的x值，即要移动的距离
        # distance = get_distance(puzzleImg, bgImg)
        distance = get_distance(big_img_path,small_img_path)


        # 3 获得移动轨迹
        track_list = get_track(distance)


        # 之后使用ActionChains类的click_and_hold方法按住滑块：
        ActionChains(driver).click_and_hold(on_element=scrollElement).perform()


        for track in track_list:
            ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform() # 鼠标移动到距离当前位置（x,y）

            # 模拟拖动时的延时
            # random_float = random.random()
            # if random_float > 0.3:
            #    random_float = random_float - 0.3
            # print("随机休眠{}秒".format(random_float))
            time.sleep(0.02)

        print('最后,释放鼠标')
        ActionChains(driver).release(on_element=scrollElement).perform()


        if "您校验错误的次数太多了,请刷新页面" in driver.text:
            driver.refresh()

        # TAB_contentTable = driver.find_element_by_id("TAB_contentTable")
        # print(TAB_contentTable.text)
    except Exception as e:
        print(e)


    # 关闭浏览器
    # driver.quit()


def click_locxy(dr, x, y, left_click=True):
    '''
    使用ActionChains 能连续点击指定坐标
    因为每次移动都是在上一次坐标的基础上（即坐标值是累积的），所以需要用封装一个方法来抵消这种累积（点击完之后将鼠标坐标恢复）
    dr:浏览器
    x:页面x坐标
    y:页面y坐标
    left_click:True为鼠标左键点击，否则为右键点击
    '''
    if left_click:
        ActionChains(dr).move_by_offset(x, y).context_click().perform()
    else:
        ActionChains(dr).move_by_offset(x, y).click().perform()
    ActionChains(dr).move_by_offset(-x, -y).perform()  # 将鼠标位置恢复到移动前





# 判断颜色是否相近
def is_similar_color( x_pixel, y_pixel):
    for i, pixel in enumerate(x_pixel):
        if abs(y_pixel[i] - pixel) > 50:
            return False
    return True

 # 计算距离
def get_offset_distance( cut_image, full_image):
    for x in range(cut_image.width):
        for y in range(cut_image.height):
            cpx = cut_image.getpixel((x, y))
            fpx = full_image.getpixel((x, y))
            if not is_similar_color(cpx, fpx):
                img = cut_image.crop((x, y, x + 40, y + 45))
                # 保存一下计算出来位置图片，看看是不是缺口部分
                img.save("1.jpg")
                return x


if __name__ == '__main__':
    try:
        big_img_path = r"C:\Users\Administrator\Downloads\captcha_img.jpg"
        big_img_path = Image.open(big_img_path)
        big_img_path.save(r'C:\Users\Administrator\Downloads\captcha_big_img.png')

        big_img_path = Image.open(r'C:\Users\Administrator\Downloads\captcha_big_img.png')
        big_img_path = big_img_path.convert("RGB")

        # PIL将png的RGBA四通道改为jpg的RGB三通道方法  https://blog.csdn.net/missyougoon/article/details/85331493

        small_img_path = r"C:\Users\Administrator\Downloads\captcha_img.png"
        small_img_path = Image.open(small_img_path)
        small_img_path = small_img_path.convert("RGB")

        # distance = get_distance(big_img_path,small_img_path)
        # print("distance={}".format(distance))
        distance = get_offset_distance(small_img_path,big_img_path)
        print("distance={}".format(distance))
    except Exception as e:
        print(e)
    #



