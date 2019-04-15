# -*- coding:utf-8 -*-

"""
@Function:          自动化测试地云网
@File    :          diyuns_test.py    
@Contact :          lizhou@glorypty.com
@License :          (C)Copyright 2019-2020

@Modify Time        @Author      @Version        @Desciption
------------        -------      --------        -----------
2019-4-12 11:44     lizhou         1.0         

"""

import re
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support.wait import WebDriverWait
import json
from bs4 import BeautifulSoup


class Diyun_AutoTest_PC():
    '''
    地云网PC前端自动化测试
    '''

    host = "http://www.diyuns.com"

    def __init__(self):
        options = webdriver.FirefoxProfile()
        options.set_preference('permissions.default.image', 2)  # 设置火狐浏览器不加载图片，提高抓取数据的效率
        self.driver = webdriver.Firefox(
            options)  # 打开火狐浏览器(提前在火狐浏览器中安装好SeleniumIDE插件、$python3Path/Scripts/geckodriver.exe )

    def firstLand_search(self):
        try:
            self.driver.get(self.host + "/search-list.html?landType=6")
            time.sleep(3)  # 强制等待,等待网页加载完成后，才能再去抓取
            inputElement = self.driver.find_element_by_class_name("ng-pristine")

            keywords = "大浦"
            inputElement.send_keys(keywords)
            js = 'document.getElementsByClassName("ng-fa-icon")[0].click()'
            self.driver.execute_script(js)

            time.sleep(1)
            try:
                resultDivList = self.driver.find_element_by_class_name("search_results_items")
                count = self.driver.find_element_by_class_name("count").text
                if resultDivList and count:
                    print("搜索后，功能正常！关键字：{}，当前页搜索结果有{}条".format(keywords, count))
                    return len(resultDivList.size)
                else:
                    print("搜索后，功能【异常】！关键字：{}，当前页搜索结果有{}条".format(keywords, count))
                    return 0
            except NoSuchElementException as notException:
                print("搜索后，系统无相关数据！关键字：{}".format(keywords))
                return -1
            except Exception as e1:
                print("搜索后，前端页面展示【异常】！关键字：{}".format(keywords))
                return -1
        except Exception as e:
            print(e)
            return -1

    def secondLand_search(self):
        try:
            self.driver.get(self.host + "/search-list.html?landType=2")
            time.sleep(3)  # 强制等待,等待网页加载完成后，才能再去抓取
            inputElement = self.driver.find_element_by_class_name("ng-pristine")

            keywords = "衡阳"
            inputElement.send_keys(keywords)
            js = 'document.getElementsByClassName("ng-fa-icon")[0].click()'
            self.driver.execute_script(js)

            time.sleep(1)
            try:
                resultDivList = self.driver.find_element_by_class_name("search_results_items")
                count = self.driver.find_element_by_class_name("count").text
                if resultDivList and count:
                    print("搜索后，功能正常！关键字：{}，当前页搜索结果有{}条".format(keywords, count))
                    return len(resultDivList.size)
                else:
                    print("搜索后，功能【异常】！关键字：{}，当前页搜索结果有{}条".format(keywords, count))
                    return 0
            except NoSuchElementException as notException:
                print("搜索后，系统无相关数据！关键字：{}".format(keywords))
                return -1
            except Exception as e1:
                print("搜索后，前端页面展示【异常】！关键字：{}".format(keywords))
                return -1

        except Exception as e:
            print(e)
            return -1

    def login(self):
          try:
              self.driver.get(self.host + "/auth/login.html")
              time.sleep(3)  # 强制等待,等待网页加载完成后，才能再去抓取
              mobilePhone = self.driver.find_element_by_name("mobilePhone")
              phoneNum = "13827460306"
              mobilePhone.send_keys(phoneNum)

              password = self.driver.find_element_by_name("password")
              pwd = "123456"
              password.send_keys(pwd)

              js = 'document.getElementsByClassName("login-btn")[0].click()'
              self.driver.execute_script(js)

              time.sleep(1)

              try:
                alertError = self.driver.find_element_by_class_name("alert-danger")
                print("登陆失败：" + alertError.text)
                return 0
              except Exception as e1:
                # 正常登陆
                pass

              time.sleep(1)

              username = self.driver.find_element_by_class_name("username").text
              phoneNum_after_handler = phoneNum[0:3] + "****" + phoneNum[7:11]

              if phoneNum_after_handler in username:
                  print("登陆成功！")
                  return 1
              else:
                  print("登陆失败...")
                  return 0

          except Exception as e:
              print("登陆异常..." + e)
              return -1

    def finish_test(self):
        self.driver.quit()  # 关闭浏览器
        print("测试完成，关闭浏览器!")


if __name__ == "__main__":
    pcAutoTest = Diyun_AutoTest_PC()
    resultCount = pcAutoTest.login()
    print("登陆功能，测试完成!" + "=" * 100)

    resultCount1 = pcAutoTest.firstLand_search()
    print("一手地搜索功能，测试完成!" + "=" * 100)

    resultCount2 = pcAutoTest.secondLand_search()
    print("二手地搜索功能，测试完成!" + "=" * 100)

    pcAutoTest.finish_test()
