# -*- coding:utf-8 -*-

# Python 输入多个经纬度坐标，找出中心点
# 原文链接 https://blog.csdn.net/sunny_12138/article/details/60883233

from math import cos, sin, atan2, sqrt, pi, radians, degrees


def center_geolocation(geolocations):
    x = 0
    y = 0
    z = 0

    lenth = len(geolocations)
    for lon, lat in geolocations:
        lon = radians(float(lon))
        lat = radians(float(lat))

        x += cos(lat) * cos(lon)
        y += cos(lat) * sin(lon)
        z += sin(lat)

    x = float(x / lenth)
    y = float(y / lenth)
    z = float(z / lenth)

    return (degrees(atan2(y, x)), degrees(atan2(z, sqrt(x * x + y * y))))

if __name__ == '__main__':
    # 求(在四边形的交点处的)四个点的中心点坐标（较准确，前提是知道四个相交点的坐标）
    locations = [[121.505547,31.092202], [121.508206,31.092901], [121.50932,31.089987],[121.506297,31.089179]]
    print(center_geolocation(locations))


    # 这种方式求中心点的有误差，大概在500m左右，还需大量测试
    locations = [
        # 北边路上的坐标
        [121.493694,31.089185], [121.5015,31.091179], [121.508668,31.093097],[121.516537,31.095771],

        # 南边路上的坐标
        [121.497134,31.086827], [121.502551,31.088164], [121.509585,31.089981],[121.512998,31.090862],

        # 西边路上的坐标
        [121.506117,31.089502], [121.507168,31.086486], [121.508686,31.082018],[121.510061,31.077951],

        # 东边路上的坐标
        [121.509683,31.089424], [121.510815,31.085682], [121.512944,31.079605],[121.513905,31.075662],
    ]
    print(center_geolocation(locations))

