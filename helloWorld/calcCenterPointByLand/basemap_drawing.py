# -*- coding:utf-8 -*-
# python basemap 画出经纬度并标定
# https://matplotlib.org/basemap/users/graticule.html


# python -m pip install --upgrade pip             # 升级pip（python3.4之后的版本都自带了PIP，但是需要升级之后才能使用）
# pip install --force-reinstall --upgrade pip     # 重新安装pip
# pip list　　　　　　　　　　　　　　　　　　　　　　　　# 查看已安装的库
# pip list --format=columns
#
# pip show   matplotlib               # 查看matplotlib
# pip install   matplotlib            # 安装matplotlib
# pip install -U   matplotlib         # 更新matplotlib
# pip uninstall    matplotlib         # 卸载matplotlib





# from mpl_toolkits.basemap import Basemap;
# import matplotlib.pyplot as plt
# import numpy as np
# # setup Lambert Conformal basemap.
# m = Basemap(width=12000000,height=9000000,projection='lcc',
#             resolution='c',lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
# # draw coastlines.
# m.drawcoastlines()
# # draw a boundary around the map, fill the background.
# # this background will end up being the ocean color, since
# # the continents will be drawn on top.
# m.drawmapboundary(fill_color='aqua')
# # fill continents, set lake color same as ocean color.
# m.fillcontinents(color='coral',lake_color='aqua')
# # draw parallels and meridians.
# # label parallels on right and top
# # meridians on bottom and left
# parallels = np.arange(0.,81,10.)
# # labels = [left,right,top,bottom]
# m.drawparallels(parallels,labels=[False,True,True,False])
# meridians = np.arange(10.,351.,20.)
# m.drawmeridians(meridians,labels=[True,False,False,True])
# plt.show()