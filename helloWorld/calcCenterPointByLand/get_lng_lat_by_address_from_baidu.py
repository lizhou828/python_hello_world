# -*- coding:utf-8 -*-
#
# 根据省市区+地址描述信息，调用百度地图api的接口，获取该地点的经纬度，如果返回多个经纬度，则选取最近的两个
# 百度地图api相应的接口文档地址：http://lbsyun.baidu.com/index.php?title=webapi/place-suggestion-api

import urllib.request as request
import urllib.parse as parse
import json

# 根据url获取网页内容
def getHtml(url):
    page = request.urlopen(url)
    html = page.read()
    return html.decode('UTF-8')

class Address:
    def __init__(self,province,address):
        self.province = province
        self.address = address

    def __str__(self, *args, **kwargs):
        return self.province + "," + self.address


addressA = "上海市浦申路"
addressB = "上海市北江洲路"
addressC = "上海市浦驰路"
addressD = "上海市立跃路"


def get_two_point_from_address(address):
    # 含有中文参数，使用get方式请求接口时，需要做些urlencode
    p = parse.quote(address.province)
    d = parse.quote(address.address)
    url = "http://api.map.baidu.com/place/v2/suggestion?query=" + d + "&region=" + p + "&city_limit=true&output=json&ak=xUIbNGuPrfOYBpu9iK0k1dmeI3iTlFi1"
    html = getHtml(url)
    # print(html)

    # string to dict数据类型
    j = eval(html)
    if ( j and j["status"] == 0 and j["result"]):
        print("请求成功")

        # 先根据j["result"]["name"] 的进行排序，

        #循环j["result"]  取出前两个，组成list,并返回

        resultList = j["result"];
        # 在resultList集合中，按对象某个属性排序
        resultList.sort(key = lambda r : len(r["name"]),  reverse=False)


        i = 0
        points = []
        for result in resultList:
            if ( len(points) == 2 ) :
                return points
            if(address.address in result["name"]):
                i += 1
                points.append(result)


    else:
        print("请求异常或者无数据...")
        print(j)


if __name__ == '__main__':
    print("hi")
    print(Address("上海市","浦申路"))
    print(get_two_point_from_address(Address("上海市","浦申路")))
    # url = "http://api.map.baidu.com/place/v2/suggestion?query=%E7%AB%8B%E8%B7%83%E8%B7%AF&region=%E4%B8%8A%E6%B5%B7%E5%B8%82&city_limit=true&output=json&ak=xUIbNGuPrfOYBpu9iK0k1dmeI3iTlFi1"
    # html = getHtml(url)
    # print(html)