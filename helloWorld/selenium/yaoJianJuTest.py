# -*- coding:utf-8 -*-
# 原文：https://blog.csdn.net/baby_hua/article/details/80571109

from selenium import webdriver


def filterDetailUrl(_href):
    # javascript:commitForECMA(callbackC,"content.jsp?tableId=41&tableName=TABLE41&tableView=药品经营企业&Id=415528",null)
    if "content.jsp?tableId" in _href:
        stringArray = _href.split(",")
        for hrefStr in stringArray:
            if "content.jsp?tableId" in hrefStr:
                hrefStr = hrefStr.replace("\"","");
                return hrefStr


# create a new Firefox session

driver = webdriver.Firefox()
driver.implicitly_wait(10)#设置超时时间
driver.maximize_window()#窗口最大化显示

#  navigate to the application home page

driver.get("http://app1.sfda.gov.cn/datasearch/face3/base.jsp?tableId=41&tableName=TABLE41&title=%D2%A9%C6%B7%BE%AD%D3%AA%C6%F3%D2%B5&bcId=118715854214917952033010551784")

divElement = driver.find_element_by_id("content")
print(divElement)
detailUrlPrefix = "http://app1.sfda.gov.cn/datasearch/face3/"
aList = divElement.find_elements_by_tag_name("a")
for a in aList:
    print("链接内容：" + a.text)
    print("得到详情页链接：" + detailUrlPrefix + filterDetailUrl(a.get_attribute("href")))

#  close the browser window
driver.quit()



