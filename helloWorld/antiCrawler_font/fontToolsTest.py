# -*- coding:utf-8 -*-
"""
使用fonttools 操作ttf文件，已解决字体反爬虫
@Function:
@File    :          fontTools.py    
@Contact :          lizhou@glorypty.com
@License :          (C)Copyright 2019-2020

@Modify Time        @Author      @Version        @Desciption
------------        -------      --------        -----------
2019-5-30 15:20     lizhou         1.0         

"""


# pip install fonttools

from fontTools.ttLib import TTFont


def comp(l1,l2):  #定义一个比较函数，比较两个列表的坐标信息是否相同
    if len(l1)!=len(l2):
        return False
    else:
        mark=1
        for i in range(len(l1)):
            if abs(l1[i][0]-l2[i][0])<40 and abs(l1[i][1]-l2[i][1])<40:
                pass
            else:
                mark=0
                break
        return mark




#手动确定一组编码和字符的对应关系
u_list=['uni307A', 'uni309E', 'uni3479', 'uni4E20', 'uni4E21', 'uni4E5A', 'uni4E6C', 'uni4E96', 'uni4F12', 'uni4F3A', 'uni4F64', 'uni4F66', 'uni4F8C', 'uni4FE0', 'uni506C', 'uni5072']
word_list=['疆','政','渔','权','化','公','同','件','下','学','9','神','血','裁','d','外']



font1=TTFont('icomoon.ttf')
be_p1=[]  #保存所有字符的（x,y）信息
for uni in u_list:
    p1 = []  #保存一个字符的(x,y)信息
    p=font1['glyf'][uni].coordinates #获取对象的x,y信息，返回的是一个GlyphCoordinates对象，可以当作列表操作，每个元素是（x,y）元组
    # p=font1['glyf'][i].flags #获取0、1值，实际用不到
    for f in p:       #把GlyphCoordinates对象改成一个列表
        p1.append(f)
    be_p1.append(p1)



font2=TTFont('icomoon(1).ttf')
uni_list2=font2.getGlyphOrder()[1:]
on_p1=[]
for i in uni_list2:
    pp1 = []
    p=font2['glyf'][i].coordinates
    for f in p:
        pp1.append(f)
    on_p1.append(pp1)


n2=0
x_list=[]
for d in on_p1:
    n2+=1
    n1=0
    for a in be_p1:
        n1+=1
        if comp(a,d):
            print(uni_list2[n2-1],word_list[n1-1])
            x_list.append(word_list[n1-1])






print(x_list[:16])
print(x_list[16:32])
print(x_list[-6:])


# print(" hi  fontTools.ttLib  ")
#打开本地字体文件
# font = TTFont('icomoon.ttf')
# font.saveXML('01.xml')



# 读取字体的映射关系
# uni_list = font['cmap'].tables[0].ttFont.getGlyphOrder() # 参数'cmap' 表示汉字对应的映射 为unicode编码
# print(uni_list)
# # 打印的结果为：['.notdef', 'uniECD5', 'uniEC83', 'uniED37', 'uniECE5', 'uniED98', 'uniEC58', 'uniEDFA', 'uniECB9', 'uniED6D', 'uniED1B', 'uniEDCE', 'uniED7D', 'uniEC3C', 'uniECEF', 'uniEC9E', 'uniED51', 'uniEE04', 'uniEDB3', 'uniEC72', 'uniEC20', 'uniECD4', 'uniED87', 'uniED35', 'uniEDE9', 'uniECA8', 'uniEC56', 'uniED0A', 'uniECB8', 'uniED6B', 'uniEC2B', 'uniEDCD', 'uniEC8C', 'uniED40', 'uniECEE', 'uniEDA1', 'uniED4F', 'uniEE03', 'uniECC2']
# # 需要注意的是：.notdef 并不是汉字的映射， 而是表示字体家族名称。真实数据是从下标 1 开始。
# utf_list = [ eval(r"u'\u" + x[3:] + "'") for x in uni_list[1:]]
# print(utf_list)
#


# obj_list1=font.getGlyphNames()[1:]   #获取所有字符的对象，去除第一个个
# uni_list1=font.getGlyphOrder()[2:]    #获取所有编码，去除前2个
#      #手动确认编码和数字之间的对应关系，保存到字典中
# dict={'uniEA78': '8', 'uniF411': '2', 'uniE87C': '1', 'uniEAC3': '9', 'uniE9DA': '3', 'uniE06A': '4', 'uniE210': '0', 'uniED72': '7', 'uniECB8': '5', 'uniF2A9': '6'}



# r"D:\github\python_project\01.xml"




