from fontTools.ttLib import TTFont

# 打开本地字体文件
font = TTFont('icomoon.ttf')
# font.saveXML('01.xml')


luan_ma = "霶鏄朤垘橚和痤旎内偲巊鏾朤"

# 读取字体的映射关系
uni_list = font['cmap'].tables[0].ttFont.getGlyphOrder() # 参数'cmap' 表示汉字对应的映射 为unicode编码
print(uni_list)
# 打印的结果为：['.notdef', 'uniECD5', 'uniEC83', 'uniED37', 'uniECE5', 'uniED98', 'uniEC58', 'uniEDFA', 'uniECB9', 'uniED6D', 'uniED1B', 'uniEDCE', 'uniED7D', 'uniEC3C', 'uniECEF', 'uniEC9E', 'uniED51', 'uniEE04', 'uniEDB3', 'uniEC72', 'uniEC20', 'uniECD4', 'uniED87', 'uniED35', 'uniEDE9', 'uniECA8', 'uniEC56', 'uniED0A', 'uniECB8', 'uniED6B', 'uniEC2B', 'uniEDCD', 'uniEC8C', 'uniED40', 'uniECEE', 'uniEDA1', 'uniED4F', 'uniEE03', 'uniECC2']
# 需要注意的是：.notdef 并不是汉字的映射， 而是表示字体家族名称。真实数据是从下标 1 开始。
for x in uni_list[4:]:
    if x.startswith("uni"):
        print("yes")
    x
    print(x)

# utf_list = [ eval(r"u'\u" + x[3:] + "'") for x in uni_list[1:]]
# print(utf_list)

