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

    locations = [[121.505547,31.092202], [121.508206,31.092901], [121.50932,31.089987],[121.506297,31.089179]]
    print(center_geolocation(locations));
