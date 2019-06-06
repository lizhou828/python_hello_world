# -*- coding:utf-8 -*-

"""
Python爬虫六：字体反爬处理（猫眼+汽车之家）-2018.10
https://blog.csdn.net/xing851483876/article/details/82928607


@Function:
@File    :          fontToolsTest1.py    
@Contact :          lizhou@glorypty.com
@License :          (C)Copyright 2019-2020

@Modify Time        @Author      @Version        @Desciption
------------        -------      --------        -----------
2019-6-5 13:45     lizhou         1.0         

"""

# pip install fonttools
from fontTools.ttLib import TTFont



# #手动确定一组编码和字符的对应关系
# u_list = ['uni30EB', 'uni4E41', 'uni4E67', 'uni4E82', 'uni4EBE', 'uni4ECF', 'uni4EEF', 'uni9E7D', 'uni9EA5',
#           'uni9F21', 'uni9F70']
# word_list = ['史', '东', '录', '书', '周', '网', '毛', '波', '上', '员', '山']


# 从第一个woff文件（作为基准版）本中获取到的编号
u_list = ['uni30EB', 'uni4E41', 'uni4E67', 'uni4E82', 'uni4EBE', 'uni4ECF', 'uni4EEF', 'uni4F71', 'uni4F7E', 'uni4FE5', 'uni5045', 'uni5072', 'uni5098', 'uni50F3', 'uni50FD', 'uni5121', 'uni5138', 'uni5147', 'uni514E', 'uni516F', 'uni5172', 'uni51A9', 'uni5258', 'uni5268', 'uni527C', 'uni5283', 'uni5287', 'uni52D9', 'uni52FC', 'uni5394', 'uni5399', 'uni53C3', 'uni53D2', 'uni54CB', 'uni54FE', 'uni5521', 'uni5525', 'uni552B', 'uni5588', 'uni55AA', 'uni55B2', 'uni55F1', 'uni55F9', 'uni55FB', 'uni55FC', 'uni5604', 'uni5614', 'uni5619', 'uni5638', 'uni5642', 'uni5664', 'uni567A', 'uni56C9', 'uni56E9', 'uni56EE', 'uni5704', 'uni570B', 'uni5716', 'uni5718', 'uni571C', 'uni5731', 'uni5767', 'uni5837', 'uni58DE', 'uni58FD', 'uni5905', 'uni5924', 'uni5980', 'uni59A0', 'uni5A3F', 'uni5A6B', 'uni5A88', 'uni5AA8', 'uni5AB4', 'uni5ACA', 'uni5AE7', 'uni5AFC', 'uni5B0C', 'uni5B24', 'uni5B3F', 'uni5B4C', 'uni5C05', 'uni5C4D', 'uni5C5F', 'uni5C64', 'uni5C65', 'uni5C7E', 'uni5CBD', 'uni5CEE', 'uni5CEF', 'uni5D2B', 'uni5D36', 'uni5D54', 'uni5D57', 'uni5D7B', 'uni5D7F', 'uni5DDF', 'uni5E51', 'uni5EDA', 'uni5F1C', 'uni5F61', 'uni5F75', 'uni6046', 'uni604F', 'uni608A', 'uni6098', 'uni60A1', 'uni60AA', 'uni60BB', 'uni6105', 'uni616C', 'uni616E', 'uni617E', 'uni6191', 'uni619B', 'uni61DE', 'uni61F2', 'uni61F7', 'uni6228', 'uni622E', 'uni6230', 'uni62E1', 'uni62F9', 'uni6373', 'uni63B1', 'uni63D7', 'uni63F9', 'uni6464', 'uni6473', 'uni64FE', 'uni6503', 'uni6518', 'uni6569', 'uni65E3', 'uni65EA', 'uni6649', 'uni6688', 'uni66AB', 'uni66F1', 'uni66F8', 'uni6702', 'uni67C2', 'uni68FC', 'uni6943', 'uni6A39', 'uni6A46', 'uni6A47', 'uni6A53', 'uni6A74', 'uni6AAD', 'uni6B61', 'uni6B6F', 'uni6BB8', 'uni6BF3', 'uni6CB0', 'uni6CB5', 'uni6D38', 'uni6D55', 'uni6DE5', 'uni6E31', 'uni6E4F', 'uni6E53', 'uni6E54', 'uni6EAB', 'uni6EE6', 'uni6EFD', 'uni6F11', 'uni6F22', 'uni6F34', 'uni6F4D', 'uni6F4E', 'uni6F75', 'uni6F80', 'uni6F95', 'uni6FA4', 'uni6FC6', 'uni6FD5', 'uni6FE0', 'uni6FF1', 'uni6FFA', 'uni701C', 'uni7027', 'uni703B', 'uni70A1', 'uni7104', 'uni7151', 'uni7171', 'uni7177', 'uni718B', 'uni7197', 'uni720D', 'uni723F', 'uni7278', 'uni72CC', 'uni734C', 'uni735E', 'uni7375', 'uni737B', 'uni740E', 'uni743A', 'uni745D', 'uni74AA', 'uni74D2', 'uni74DE', 'uni751E', 'uni75CC', 'uni760B', 'uni761A', 'uni765F', 'uni7662', 'uni769B', 'uni76E7', 'uni76EC', 'uni783D', 'uni78A5', 'uni78C6', 'uni79A2', 'uni79B8', 'uni7A35', 'uni7A4D', 'uni7ABF', 'uni7AF6', 'uni7B9B', 'uni7BA0', 'uni7BDC', 'uni7BFE', 'uni7C06', 'uni7C80', 'uni7C85', 'uni7CD8', 'uni7CE7', 'uni7CFE', 'uni7D01', 'uni7D25', 'uni7DDA', 'uni7DE9', 'uni7E02', 'uni7E23', 'uni7E2E', 'uni7E8C', 'uni7EA9', 'uni7F15', 'uni7F1E', 'uni7F85', 'uni7FB1', 'uni802A', 'uni8045', 'uni805E', 'uni8103', 'uni814E', 'uni81A9', 'uni81D8', 'uni81E5', 'uni8209', 'uni820A', 'uni820E', 'uni8219', 'uni8278', 'uni82A2', 'uni82D0', 'uni82DD', 'uni82F8', 'uni8306', 'uni831A', 'uni834D', 'uni8355', 'uni8388', 'uni838B', 'uni83A3', 'uni83AE', 'uni83C8', 'uni841C', 'uni8420', 'uni842A', 'uni843F', 'uni8443', 'uni8452', 'uni8459', 'uni846E', 'uni8472', 'uni847E', 'uni847F', 'uni84C8', 'uni84DC', 'uni84F3', 'uni84F7', 'uni8500', 'uni8509', 'uni850E', 'uni8520', 'uni854F', 'uni8550', 'uni8554', 'uni855C', 'uni8569', 'uni85CD', 'uni85D9', 'uni86EC', 'uni8742', 'uni87A1', 'uni87BA', 'uni883B', 'uni8846', 'uni885E', 'uni8889', 'uni88D1', 'uni8932', 'uni8956', 'uni8980', 'uni8A01', 'uni8A2C', 'uni8AA6', 'uni8ACD', 'uni8ADF', 'uni8AF4', 'uni8B58', 'uni8B6F', 'uni8B8A', 'uni8C09', 'uni8C5E', 'uni8CD7', 'uni8CE2', 'uni8CEA', 'uni8D7D', 'uni8D9A', 'uni8DAB', 'uni8DAC', 'uni8EDF', 'uni8F25', 'uni8F44', 'uni8F75', 'uni8FA4', 'uni8FC9', 'uni9021', 'uni904A', 'uni904B', 'uni9055', 'uni9084', 'uni9134', 'uni9154', 'uni91E2', 'uni91FF', 'uni9223', 'uni923D', 'uni9272', 'uni92B1', 'uni92B3', 'uni92D6', 'uni9301', 'uni931E', 'uni9322', 'uni9336', 'uni9385', 'uni938D', 'uni9528', 'uni956C', 'uni9581', 'uni9584', 'uni9599', 'uni959E', 'uni95E1', 'uni964F', 'uni967B', 'uni9682', 'uni96A2', 'uni96E3', 'uni971A', 'uni9721', 'uni9729', 'uni9743', 'uni9748', 'uni9773', 'uni9798', 'uni97FB', 'uni9867', 'uni98DC', 'uni9900', 'uni993B', 'uni998F', 'uni99B6', 'uni99BF', 'uni9AD2', 'uni9B26', 'uni9D3B', 'uni9D6C', 'uni9D70', 'uni9D8F', 'uni9E7D', 'uni9EA5', 'uni9F21', 'uni9F70']

# 从第一个woff文件（作为基准版）本中获取到的文字
word_list = ['史', '东', '录', '书', '周', '网', '毛', '范', '统', '所', '微', '成', '印', '机', '于', '开', '复', '载',
             '业', '名', '地', '善', '期', '堡', '列', '田', '脸', '据', '得', '敌', '第', '积', '洁', '欢', '九', '沉',
             '央', '点', '家', '聚', '系', '件', '光', '黄', '义', '魂', '鞋', '活', '兵', '指', '听', '补', '部', '飞',
             '用', '线', '新', '精', '红', '黑', '行', '何', '头', '下', '伦', '市', '展', '性', '设', '要', '克', '军',
             '顶', '里', '大', '失', '乐', '质', '都', '企', '马', '端', '吾', '版', '团', '参', '改', '络', '历', '术',
             '极', '群', '注', '工', '人', '搜', '首', '加', '化', '传', '页', '盒', '量', '党', '通', '主', '论', '张',
             '建', '文', '渔', '津', '退', '众', '海', '廉', '凰', '错', '认', '科', '坛', '具', '频', '热', '选', '发',
             '为', '担', '先', '好', '准', '斯', '革', '弘', '软', '腾', '聘', '深', '当', '有', '度', '厅', '经', '西',
             '无', '不', '牌', '民', '时', '其', '密', '计', '湾', '型', '对', '酷', '我', '产', '典', '本', '电', '近',
             '扫', '讲', '德', '转', '遗', '务', '锋', '祠', '皮', '体', '布', '思', '穿', '规', '款', '责', '推', '态',
             '六', '报', '共', '平', '去', '招', '习', '闻', '定', '讯', '续', '凤', '农', '泽', '关', '华', '挂', '息',
             '宽', '康', '存', '调', '排', '巴', '属', '胡', '七', '引', '理', '拥', '赢', '国', '阿', '舆', '信', '数',
             '抱', '变', '窗', '冀', '绩', '荐', '律', '届', '多', '区', '利', '除', '中', '站', '正', '卫', '代', '知',
             '客', '会', '狗', '决', '办', '淀', '南', '面', '同', '役', '请', '顿', '与', '梦', '动', '想', '明', '李',
             '外', '高', '来', '视', '天', '收', '在', '更', '之', '坚', '践', '日', '示', '府', '洛', '财', '公', '幕',
             '悬', '告', '宣', '承', '临', '扎', '绿', '的', '见', '学', '层', '涯', '优', '省', '广', '末', '城', '能',
             '说', '神', '铁', '修', '困', '强', '程', '争', '负', '个', '申', '字', '常', '哲', '协', '命', '北', '户',
             '汉', '权', '入', '社', '音', '管', '境', '法', '裁', '云', '持', '育', '百', '浙', '犯', '藏', '源', '疆',
             '局', '步', '迎', '政', '土', '资', '标', '事', '如', '丽', '登', '作', '膀', '江', '荣', '治', '十', '位',
             '涉', '博', '技', '赋', '埃', '移', '干', '服', '水', '夫', '素', '做', '制', '艺', '亲', '舟', '情', '臂',
             '健', '勇', '控', '贸', '单', '园', '台', '任', '竞', '浪', '远', '集', '血', '生', '方', '扬', '欧', '狐',
             '恶', '全', '年', '吸', '委', '简', '进', '专', '总', '波', '上', '员', '山']


font1 = TTFont('1_1.woff')
be_p1=[]  #保存所有字符的（x,y）信息
for uni in u_list:
    p1 = []  #保存一个字符的(x,y)信息
    p=font1['glyf'][uni].coordinates #获取对象的x,y信息，返回的是一个GlyphCoordinates对象，可以当作列表操作，每个元素是（x,y）元组
    # p=font1['glyf'][i].flags #获取0、1值，实际用不到
    for f in p:       #把GlyphCoordinates对象改成一个列表
        p1.append(f)
    be_p1.append(p1)



# font2 = TTFont('1_2.woff')
font2 = TTFont('1_5.woff')
uni_list2 = font2.getGlyphOrder()[1:]
on_p1=[]
for i in uni_list2:
    pp1 = []
    p=font2['glyf'][i].coordinates
    for f in p:
        pp1.append(f)
    on_p1.append(pp1)


def comp(l1,l2):
    '''
    #定义一个比较函数，比较两个列表的坐标信息是否相同
    :param l1:
    :param l2:
    :return:
    '''
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

#多次请求字体文件后，对比，发现规律：每次得到的字体文件，只有文字图形相同，编号是动态变化的
# 根据第一次获得的字体文件，获得到编号、文字、文字坐标的信息，作为标准
# 然后用第一次的得到表中的文字坐标信息，去后续得到的字体文件中去匹配，这样就能得到文字在第二次的字体中的编号
# 就相当于是，每次获得到的字体文件，就要实时更新字体字典，

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



print(x_list)
