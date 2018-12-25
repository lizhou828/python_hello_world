# -*- coding:utf-8 -*-
# 基于向量叉乘计算多边形面积
# 采用向量叉乘计算多边形面积。由图知坐标原点（按P点为原点）与多边形任意相邻的两个顶点构成一个三角形，而三角形的面积可由三个顶点构成的两个平面向量的外积求得。任意多边形的面积公式：
# 原文地址：https://blog.csdn.net/xiaoyw71/article/details/79952520

import math

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y


def GetAreaOfPolyGonbyVector(points):
    # 基于向量叉乘计算多边形面积
    area = 0
    if(len(points)<3):

         raise Exception("error")

    for i in range(0,len(points)-1):
        p1 = points[i]
        p2 = points[i + 1]

        triArea = (p1.x*p2.y - p2.x*p1.y)/2
        area += triArea
    return abs(area)

def main():

    points = []

    x = [1,2,3,4,5,6,5,4,3,2]
    y = [1,2,2,3,3,3,2,1,1,1]

    x = [0,2,2,0]
    y = [0,0,2,2]
    for index in range(len(x)):
        points.append(Point(x[index],y[index]))

    area = GetAreaOfPolyGonbyVector(points)
    print(area)
    print(math.ceil(area))


if __name__ == '__main__':
    main()
    print("OK")
