# -*- coding:utf-8 -*-

"""
@Function:
@File    :          execel_test.py    
@Contact :          lizhou@glorypty.com
@License :          (C)Copyright 2019-2020

@Modify Time        @Author      @Version        @Desciption
------------        -------      --------        -----------
2019-6-14 10:51     lizhou         1.0         

"""
# pip install xlwt
import xlwt

# 按照行写入数据
f = xlwt.Workbook() #创建工作簿
sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
l_=['a','b','c','d','e','f']
for i in range(len(l_)):
    sheet1.write(0,i,l_[i])#表格的第一行开始写。第一列，第二列。。。。
#sheet1.write(0,0,start_date,set_style('Times New Roman',220,True))
f.save('execel_test.xls')#保存文件


