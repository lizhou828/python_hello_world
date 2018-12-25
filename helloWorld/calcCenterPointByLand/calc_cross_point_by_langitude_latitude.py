# -*- coding:utf-8 -*-
# 已知两条直线上各两点坐标，求两条直线交点坐标
from helloWorld.calcCenterPointByLand.find_center_point_by_other_points import center_geolocation
from helloWorld.calcCenterPointByLand.get_lng_lat_by_address_from_baidu import get_two_point_from_address, Address


class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # __str__()方法，类似java 的toString()方法
    # self 类似java的this , 当前类的实例
    def __str__(self):
        return '(%s,%s)' %(self.x,self.y)

def calc_cross_point(x0,y0,x1,y1,x2,y2,x3,y3):
    a = y1-y0
    b = x1*y0-x0*y1
    c = x1-x0
    d = y3-y2
    e = x3*y2-x2*y3
    f = x3-x2
    y = float(a*e-b*d)/(a*f-c*d)
    x = float(y*c-b)/a
    pt = Point(x,y)
    return pt


if __name__ == '__main__':

    # 根据地块描述的信息，计算该地块在地图上的经纬度
    # 例如:
    # 地块所在城市：上海市
    # 地块描述信息：东至浦申路，南至北江洲路，西至浦驰路，北至立跃路

    roadNorth = get_two_point_from_address(Address("上海市","立跃路"))
    roadWest = get_two_point_from_address(Address("上海市","浦驰路"))
    roadEast = get_two_point_from_address(Address("上海市","浦申路"))
    roadSouth = get_two_point_from_address(Address("上海市","北江洲路"))


    # 计算北边与西边路的交点坐标
    pointA = calc_cross_point(roadNorth[0]["location"]["lng"],roadNorth[0]["location"]["lat"],roadNorth[1]["location"]["lng"],roadNorth[1]["location"]["lat"],
                              roadWest[0]["location"]["lng"],roadWest[0]["location"]["lat"],roadWest[1]["location"]["lng"],roadWest[1]["location"]["lat"]);
    print(pointA)

    # 计算北边与东边路的交点坐标
    pointB = calc_cross_point(roadNorth[0]["location"]["lng"],roadNorth[0]["location"]["lat"],roadNorth[1]["location"]["lng"],roadNorth[1]["location"]["lat"],
                              roadEast[0]["location"]["lng"],roadEast[0]["location"]["lat"],roadEast[1]["location"]["lng"],roadEast[1]["location"]["lat"])
    print(pointB)

    # 计算南边与西边路的交点坐标
    pointC = calc_cross_point(roadSouth[0]["location"]["lng"],roadSouth[0]["location"]["lat"],roadSouth[1]["location"]["lng"],roadSouth[1]["location"]["lat"],
                              roadWest[0]["location"]["lng"],roadWest[0]["location"]["lat"],roadWest[1]["location"]["lng"],roadWest[1]["location"]["lat"])
    print(pointC)

    #计算 南边与东边路的交点坐标
    pointD = calc_cross_point(roadSouth[0]["location"]["lng"],roadSouth[0]["location"]["lat"],roadSouth[1]["location"]["lng"],roadSouth[1]["location"]["lat"],
                              roadEast[0]["location"]["lng"],roadEast[0]["location"]["lat"],roadEast[1]["location"]["lng"],roadEast[1]["location"]["lat"]);
    print(pointD)

    # 根据四个交点，计算中心点坐标
    locations = [[pointA.x,pointA.y], [pointB.x,pointB.y], [pointC.x,pointC.y],[pointD.x,pointD.y]]
    centerPoint = center_geolocation(locations)
    print("计算出的中心点坐标如下：")
    print(list(centerPoint))

    #在百度地图上（http://api.map.baidu.com/lbsapi/getpoint/index.html）输入生成的经纬度，可以校验下，是否命中该地块位置
