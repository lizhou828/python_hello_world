# # -*- coding:utf-8 -*-
#
# """
# @Function:
# @File    :          create_area_execel.py
# @Contact :          lizhou@glorypty.com
# @License :          (C)Copyright 2019-2020
#
# @Modify Time        @Author      @Version        @Desciption
# ------------        -------      --------        -----------
# 2019-6-14 11:23     lizhou         1.0
#
# """
#
# # pip install xlwt
# import xlwt
#
# from com.diyun.python.crud_module.dao.areaDao import AreaDao
# from com.diyun.python.crud_module.domain.area import Area
#
# areaDao = AreaDao()
# def get_province_and_city():
#     dic = {}
#     query = Area()
#     query.set_level(1)
#     province_list = areaDao.selectByProperties(query)
#     print(province_list)
#
#     for province in province_list:
#         query = Area()
#         query.set_level(2)
#         query.set_parent_id(province.get_id())
#         city_list = areaDao.selectByProperties(query)
#         city_name_list = []
#         for city in city_list:
#             city_name_list.append(city.get_area_name())
#         dic[province.get_area_name()] = city_name_list
#     return dic
#
# def get_city_and_county():
#     dic = {}
#     query = Area()
#     query.set_level(2)
#     city_list = areaDao.selectByProperties(query)
#     print(city_list)
#
#     for city in city_list:
#         query = Area()
#         query.set_level(3)
#         query.set_parent_id(city.get_id())
#         county_list = areaDao.selectByProperties(query)
#         county_name_list = []
#         if not county_list:
#             dic[city.get_area_name()] = []
#             continue
#         for county in county_list:
#             county_name_list.append(county.get_area_name())
#         if dic.__sizeof__() > 0 and dic.get(city.get_area_name()):
#             dic[city.get_area_name() + str(city.get_parent_id())] = county_name_list
#         else:
#             dic[city.get_area_name()] = county_name_list
#     return dic
#
#
# # 按照行写入数据
# # f = xlwt.Workbook() #创建工作簿
# # sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
# # l_=['a','b','c','d','e','f']
# # for i in range(len(l_)):
# #     sheet1.write(0,i,l_[i])#表格的第一行开始写。第一列，第二列。。。。
# # #sheet1.write(0,0,start_date,set_style('Times New Roman',220,True))
# # f.save('execel_test.xls')#保存文件
# #
#
#
# if __name__ == "__main__":
#     # dic = get_province_and_city()
#     # print(dic)
#
#     # dic = get_city_and_county()
#     # print(dic)
#
#     f = xlwt.Workbook() #创建工作簿
#     sheet1 = f.add_sheet(u'省市',cell_overwrite_ok=True) #按列写入
#     province_dic = get_province_and_city()
#
#     column_index = 0
#     for k,v in province_dic.items():
#         sheet1.write(0,column_index,k)
#         sheet1.write(1,column_index,len(v))
#         row_index = 2
#         for city in v:
#             sheet1.write(row_index,column_index,city)
#             row_index += 1
#         column_index += 1
#
#     sheet2 = f.add_sheet(u'市县',cell_overwrite_ok=True) #按行写入
#     county_dic = get_city_and_county()
#     row_index = 0
#     for k,v in county_dic.items():
#         sheet2.write(row_index,0,k)
#         sheet2.write(row_index,1,len(v))
#         column_index = 2
#         for county in v:
#             sheet2.write(row_index,column_index,county)
#             column_index += 1
#         row_index += 1
#
#     f.save('execel_test.xls')#保存文件