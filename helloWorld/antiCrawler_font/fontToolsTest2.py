from fontTools.ttLib import TTFont

# 打开本地字体文件
font = TTFont('icomoon.ttf')
# font.saveXML('01.xml')

# 预先用 fontCreator软件读取ttf字体文件，然后手动把字体文件截成图片，通过ocr识别出文字，然后人工手动校准下(英文、数组、标点符号、笔画复杂的中文等可能识别有误)
# 最后把识别出的文字放到这里
words = r'疆政渔权化公同件下学9神血裁d外上o《办1魂舟平引远幕b务与服典区飞育如家伦程吾Q补持集户里r加民极-所东铁膀城遗负讲思臂动知厅争省转马哲生七示治届洛.艺财频代有山迎5藏贸计的脸入' \
        r'标毛载在机黄凰退做宣市情招音浙博我B新技当冀调主吸请六4十巴其卫m多》江九境第得土淀人简据埃梦地选密”录软荐网具专电共指员廉康盒术企u亲委报控告赢体舆干建去不堡群悬6精历数想e窗存' \
        r'军顿排更聘津沉皮客祠T善酷性c园日络经部源设好面积绿站听命水成胡首属展狗优南国德范鞋8史习全弘海党通抱役湾顶3:本息移端克洁步度业夫列改搜腾。层信J周宽兵义微要用工说欧讯临7版云态方' \
        r'赋2浪勇局修文承V一名注,进泽产常近利视印律质关会款大认责单推书任P何天管量开健竞线复收北规扎字统|都申明0素末光y革乐黑热发活理协位行农之制总为作P准于科田年型除广高点波拥－布头登' \
        r'涉践扬C定闻荣涯华时法府敌对先绩团恶红穿深凤欢坚事决中来系丽正错论张能失坛D资期犯传、“强页锋担社参狐续聚扫台李变无困个众西挂斯百央牌见阿汉'

# 读取字体的映射关系
uni_list = font['cmap'].tables[0].ttFont.getGlyphOrder() # 参数'cmap' 表示汉字对应的映射 为unicode编码
print(uni_list)
# 打印的结果为：['.notdef', 'uniECD5', 'uniEC83', 'uniED37', 'uniECE5', 'uniED98', 'uniEC58', 'uniEDFA', 'uniECB9', 'uniED6D', 'uniED1B', 'uniEDCE', 'uniED7D', 'uniEC3C', 'uniECEF', 'uniEC9E', 'uniED51', 'uniEE04', 'uniEDB3', 'uniEC72', 'uniEC20', 'uniECD4', 'uniED87', 'uniED35', 'uniEDE9', 'uniECA8', 'uniEC56', 'uniED0A', 'uniECB8', 'uniED6B', 'uniEC2B', 'uniEDCD', 'uniEC8C', 'uniED40', 'uniECEE', 'uniEDA1', 'uniED4F', 'uniEE03', 'uniECC2']
# 需要注意的是：.notdef 并不是汉字的映射， 而是表示字体家族名称。真实数据是从下标 1 开始。
font_dic = {}
for unicode,words  in zip(uni_list[4:],words):
    print(unicode,":",words)
    key = "u"+ unicode[3:].lower()
    font_dic[key] = words

print(font_dic)



