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

class DirectionDesc():
    # area 表示地块所在的省市区
    # north,south,east,west 表示地块的四至信息
    # address_info 表示地块的描述信息
    def __init__(self,area,north,south,east,west,address_info):
        self.area = area
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.address_info = address_info
        # Python三目运算符不像Java,但也有自己的三目运算符：　　　
        # 条件为真时的结果 if 判段的条件 else 条件为假时的结果
        # 例如: print(x if(x>y) else y)
        self.directionCount = (1 if(north) else 0) + (1 if(south) else 0) + (1 if(east) else 0) + (1 if(west) else 0)

    # __str__()方法，类似java 的toString()方法
    # self 类似java的this , 当前类的实例
    def __str__(self):
        return '(%s,%s,%s,%s)' %(self.north,self.south,self.east,self.west)


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

# 解析省市区
def parseRegion(region):
    if not region:
        return region
    elif "上海市" in region:
        return "上海市"

    elif "北京市" in region:
        if region.endswith("北京市本级"):
            return "北京市"
        else:
            region = region.replace(" > 北京市市辖区 > ","")
            region = region.replace(" > 北京市所辖县 > ","")
            return region

    elif "天津市" in region:
        if region.endswith("天津市本级"):
            return "天津市"
        else:
            region = region.replace(" > 天津市市辖区 > ","")
            region = region.replace(" > 天津市所辖县 > ","")
            return region

    elif "重庆市" in region:
        if region.endswith("重庆市本级"):
            return "重庆市"
        else:
            region = region.replace(" > 重庆市市辖区 > ","")
            region = region.replace(" > 重庆市所辖县 > ","")
            return region

    elif region.endswith("市本级"):
        lastIndex = region.rfind(">") -1
        if len(region) >= lastIndex:
            region = region[0:lastIndex]
            region = region.replace(" > ","")
            return region
        else:
            return region
    else:
        return region.replace(" > " ,"")

# 根据地块描述信息，解析出地块的四至
def parseDirectionDesc(addressInfo):
    directionDesc = DirectionDesc();
    if "东" not in addressInfo and"东" not in addressInfo and "东" not in addressInfo and "东" not in addressInfo :
        directionDesc.address_info = addressInfo
    else:
        # TODO
        print("todo")

    return directionDesc


# 传入的对象是Address("上海市","妙丰路")的集合
def calc_lng_lat_by_address(region,addressInfo):
    directionDesc = parseDirectionDesc(addressInfo)
    directionDesc.area = parseRegion(region);



    if directionDesc.directionCount == 4 :
        # todo  四个方位都能解析到坐标
        roadNorth = get_two_point_from_address(Address(directionDesc.area,directionDesc.north))
        roadWest = get_two_point_from_address(Address(directionDesc.area,directionDesc.west))
        roadEast = get_two_point_from_address(Address(directionDesc.area,directionDesc.east))
        roadSouth = get_two_point_from_address(Address(directionDesc.area,directionDesc.south))

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

    elif directionDesc.directionCount == 3 :
        # 出现 expected an indented block报错的原因 : https://blog.csdn.net/qq_28301007/article/details/79009980
        print("能解析到三个方位的坐标")
    elif directionDesc.directionCount == 2 :
        print("能解析到两个方位的坐标")
    else:
        # 四个方位都解析不到坐标，则返回空
        return None









if __name__ == '__main__':

    # 根据地块描述的信息，计算该地块在地图上的经纬度
    # 例如:
    # 地块所在城市：上海市
    # 地块描述信息：东至浦申路，南至北江洲路，西至浦驰路，北至立跃路


    # roadNorth = get_two_point_from_address(Address("上海市","立跃路"))
    # roadWest = get_two_point_from_address(Address("上海市","浦驰路"))
    # roadEast = get_two_point_from_address(Address("上海市","浦申路"))
    # roadSouth = get_two_point_from_address(Address("上海市","北江洲路"))
    #
    #
    # # 计算北边与西边路的交点坐标
    # pointA = calc_cross_point(roadNorth[0]["location"]["lng"],roadNorth[0]["location"]["lat"],roadNorth[1]["location"]["lng"],roadNorth[1]["location"]["lat"],
    #                           roadWest[0]["location"]["lng"],roadWest[0]["location"]["lat"],roadWest[1]["location"]["lng"],roadWest[1]["location"]["lat"]);
    # print(pointA)
    #
    # # 计算北边与东边路的交点坐标
    # pointB = calc_cross_point(roadNorth[0]["location"]["lng"],roadNorth[0]["location"]["lat"],roadNorth[1]["location"]["lng"],roadNorth[1]["location"]["lat"],
    #                           roadEast[0]["location"]["lng"],roadEast[0]["location"]["lat"],roadEast[1]["location"]["lng"],roadEast[1]["location"]["lat"])
    # print(pointB)
    #
    # # 计算南边与西边路的交点坐标
    # pointC = calc_cross_point(roadSouth[0]["location"]["lng"],roadSouth[0]["location"]["lat"],roadSouth[1]["location"]["lng"],roadSouth[1]["location"]["lat"],
    #                           roadWest[0]["location"]["lng"],roadWest[0]["location"]["lat"],roadWest[1]["location"]["lng"],roadWest[1]["location"]["lat"])
    # print(pointC)
    #
    # #计算 南边与东边路的交点坐标
    # pointD = calc_cross_point(roadSouth[0]["location"]["lng"],roadSouth[0]["location"]["lat"],roadSouth[1]["location"]["lng"],roadSouth[1]["location"]["lat"],
    #                           roadEast[0]["location"]["lng"],roadEast[0]["location"]["lat"],roadEast[1]["location"]["lng"],roadEast[1]["location"]["lat"]);
    # print(pointD)
    #
    # # 根据四个交点，计算中心点坐标
    # locations = [[pointA.x,pointA.y], [pointB.x,pointB.y], [pointC.x,pointC.y],[pointD.x,pointD.y]]
    # centerPoint = center_geolocation(locations)
    # print("计算出的中心点坐标如下：")
    # print(list(centerPoint))
    # #在百度地图上（http://api.map.baidu.com/lbsapi/getpoint/index.html）输入生成的经纬度，可以校验下，是否命中该地块位置


    region = "上海市 > 上海市市辖区 > 黄浦区";
    print("解析前的region=" + region)
    region = parseRegion(region)
    print("解析后的region=" + region)

    region = "重庆市 > 重庆市市辖区 > 黔江区"
    print("解析前的region=" + region)
    region = parseRegion(region)
    print("解析后的region=" + region)


    region = "天津市 > 天津市市辖区 > 塘沽区"
    print("解析前的region=" + region)
    region = parseRegion(region)
    print("解析后的region=" + region)

    region = "北京市 > 北京市市辖区 > 房山区"
    print("解析前的region=" + region)
    region = parseRegion(region)
    print("解析后的region=" + region)

    region = "北京市 > 北京市市辖区 > 北京市本级"
    print("解析前的region=" + region)
    region = parseRegion(region)
    print("解析后的region=" + region)

    region = "湖北省 > 襄樊市 > 襄樊市本级"
    print("解析前的region=" + region)
    region = parseRegion(region)
    print("解析后的region=" + region)









