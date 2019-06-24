# -*- coding:utf-8 -*-

"""
@Function: python之xlwt模块列宽width、行高Heights详解  https://blog.csdn.net/forfuture3513/article/details/52662502
@File    :          gen_execel_everyday.py    
@Contact :          lizhou@glorypty.com
@License :          (C)Copyright 2019-2020

@Modify Time        @Author      @Version        @Desciption
------------        -------      --------        -----------
2019-6-21 17:08     lizhou         1.0         

"""

# pip install xlwt
import os

import xlwt
import datetime
import time

# 按照行写入数据
# f = xlwt.Workbook() #创建工作簿
# sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
# l_=['a','b','c','d','e','f']
# for i in range(len(l_)):
#     sheet1.write(0,i,l_[i])#表格的第一行开始写。第一列，第二列。。。。
# #sheet1.write(0,0,start_date,set_style('Times New Roman',220,True))
# f.save('execel_files/test.xls')#保存文件
from com.diyun.python.landchina.dao.remisenoticedetailDao import RemisenoticedetailDao
from com.diyun.python.landchina.dao.remisenoticeselldetailDao import RemisenoticeselldetailDao

from helloWorld import print_info


def gen_remise_notice():
    # 按照行写入数据
    f = xlwt.Workbook()  # 创建工作簿
    sheet1 = f.add_sheet(u'土拍预告', cell_overwrite_ok=True)  # 创建sheet
    header1 = ['省份','城市', '区域', '地块编号', '用地性质', '出让方式', '拍地时间']
    for i in range(len(header1)):
        # 设置表头
        sheet1.write(0, i, header1[i])  # 表格的第一行开始写。第一列，第二列。。。。
        # 设置列宽度
        # xlwt中列宽的值表示方法：默认字体0的1/256为衡量单位。
        # xlwt创建时使用的默认宽度为2960，既11个字符0的宽度
        # 所以我们在设置列宽时可以用如下方法：
        # width = 256 * 20    256为衡量单位，20表示20个字符宽度
        sheet1.col(i).width = 256*20


    # sheet1.write(0,0,start_date,set_style('Times New Roman',220,True))
    remisenoticedetailDao = RemisenoticedetailDao()
    result_list = remisenoticedetailDao.find_tomorrow_data()
    if result_list and len(result_list) > 0:
        for row_index in range(len(result_list)):
            # row_index +1  第一行是表头，数据从第二行开始
            if not result_list[row_index].get_city_name():
                area = result_list[row_index].get_administrativearea()
                city_county = get_city_county(area)
                sheet1.write(row_index + 1, 0, city_county[0])
                sheet1.write(row_index + 1, 1, city_county[1])
                sheet1.write(row_index + 1, 2, city_county[2])
            else:
                sheet1.write(row_index + 1, 0, result_list[row_index].get_province_name())
                sheet1.write(row_index + 1, 1, result_list[row_index].get_city_name())
                sheet1.write(row_index + 1, 2, result_list[row_index].get_county_name())

            type_str = get_remise_notice_type_str(result_list[row_index].get_type())  # "类型（1招标、2拍卖、3挂牌、4公开公告、5公告调整、6其他公告）"
            sheet1.write(row_index + 1, 3, result_list[row_index].get_land_sn())
            sheet1.write(row_index + 1, 4, result_list[row_index].get_land_use_details())
            sheet1.write(row_index + 1, 5, type_str)
            sheet1.write(row_index + 1, 6, result_list[row_index].get_open_start_time())

    sheet2 = f.add_sheet(u'土地成交', cell_overwrite_ok=True)  # 创建sheet
    header2 = ['省份', '城市', '区域', '地块编号', '用地性质', '企业', '竞得时间', '竞得方式', '土地面积(公顷)', '成交总价', '成交楼面价', '溢价率', '出让条件']
    for i in range(len(header2)):
        sheet2.write(0, i, header2[i])  # 表格的第一行开始写。第一列，第二列。。。。
        # 设置列宽度
        # xlwt中列宽的值表示方法：默认字体0的1/256为衡量单位。
        # xlwt创建时使用的默认宽度为2960，既11个字符0的宽度
        # 所以我们在设置列宽时可以用如下方法：
        # width = 256 * 20    256为衡量单位，20表示20个字符宽度
        sheet2.col(i).width = 256*20


    remisenoticeselldetailDao = RemisenoticeselldetailDao()
    result_list = remisenoticeselldetailDao.find_today_data()
    if result_list and len(result_list) > 0:
        for row_index in range(len(result_list)):
            # row_index +1  第一行是表头，数据从第二行开始
            if not result_list[row_index].get_city_name():  # 出现老旧的行政区名称（不在国家统计局的行政区内）
                area = result_list[row_index].get_administrativearea()
                sheet2.write(row_index + 1, 0, "")
                sheet2.write(row_index + 1, 1, area)
                sheet2.write(row_index + 1, 2, "")
            else:
                sheet2.write(row_index + 1, 0, result_list[row_index].get_province_name())
                sheet2.write(row_index + 1, 1, result_list[row_index].get_city_name())
                sheet2.write(row_index + 1, 2, result_list[row_index].get_county_name())

            sheet2.write(row_index + 1, 3, result_list[row_index].get_land_sn())
            sheet2.write(row_index + 1, 4, result_list[row_index].get_land_use_details())
            sheet2.write(row_index + 1, 5, result_list[row_index].get_landowner())
            sheet2.write(row_index + 1, 6, result_list[row_index].get_contract_signing_date())
            sheet2.write(row_index + 1, 7, result_list[row_index].get_land_supply_mode())
            sheet2.write(row_index + 1, 8, result_list[row_index].get_land_total_area())
            sheet2.write(row_index + 1, 9, result_list[row_index].get_transaction_price())
            # sheet2.write(row_index+1,10,)
            # sheet2.write(row_index+1,11,)
            # sheet2.write(row_index+1,12,)

    today = datetime.date.today()
    date_str = "%s-%s-%s" % (today.year, today.month, today.day)
    file_path = os.path.split(os.path.realpath(__file__))[0] + r'/execel_files/' + date_str + '.xls'
    if os.path.isfile(file_path):
        # 如果存在同名的文件则先删除掉
        os.remove(file_path)
    else:
        pass
    f.save(file_path)


def get_remise_notice_type_str(_type):
    if not _type or _type == 6:
        return "其他公告"
    elif 1 == _type:
        return "招标"
    elif 2 == _type:
        return "拍卖"
    elif 3 == _type:
        return "挂牌"
    elif 4 == _type:
        return "公开公告"
    elif 5 == _type:
        return "公告调整"
    else:
        return "其他公告"


def get_city_county(area_str):
    if not area_str or len(area_str) == 0 or ">" not in area_str:
        return "", ""
    str_list = area_str.split(">")
    if not str_list or len(str_list) != 3:
        return "", ""
    return str_list[0], str_list[1], str_list[2]


if __name__ == "__main__":
    # result = get_city_county("内蒙古 > 兴安盟 > 突泉县")
    # print(result)
    # print(type(result))
    start = time.time()
    gen_remise_notice()
    end = time.time()
    print_info("xls文件生成完成，耗时：{}秒".format('%.2f' % (end - start)))
