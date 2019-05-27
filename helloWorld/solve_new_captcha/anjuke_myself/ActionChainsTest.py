# -*- coding:utf-8 -*-

"""
@Function:
@File    :          ActionChainsTest.py    
@Contact :          lizhou@glorypty.com
@License :          (C)Copyright 2019-2020

@Modify Time        @Author      @Version        @Desciption
------------        -------      --------        -----------
2019-5-27 17:52     lizhou         1.0         

"""
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui

def click_locxy(dr, x, y, left_click=True):
    '''
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

if __name__ == "__main__":
    dr = webdriver.Firefox()
    dr.get('http://www.baidu.com')
    click_locxy(dr, 100, 0)
    print("第一次点击")

    pyautogui.press('esc')

    # time.sleep(2)
    click_locxy(dr, 500, 500)
    print("第二次点击")
    pyautogui.press('esc')