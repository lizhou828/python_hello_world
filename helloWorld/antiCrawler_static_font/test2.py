# -*- coding:utf-8 -*-

"""
@Function:
@File    :          test2.py    
@Contact :          lizhou@glorypty.com
@License :          (C)Copyright 2019-2020

@Modify Time        @Author      @Version        @Desciption
------------        -------      --------        -----------
2019-5-30 17:52     lizhou         1.0         

"""

from fontTools.ttLib import TTFont

#打开本地字体文件
# font = TTFont('icomoon.ttf')
#
# # 读取字体的映射关系
# uni_list = font['cmap'].tables[0].ttFont.getGlyphOrder() # 参数'cmap' 表示汉字对应的映射 为unicode编码
# print(uni_list)


words = r'疆政渔权化公同件下学9神血裁d外上o《办1魂舟平引远幕b务与服典区飞育如家伦程吾Q补持集户里r加民极-所东铁膀城遗负讲思臂动知厅争省转马哲生七示治届洛.艺财频代有山迎5藏贸计的脸入' \
        r'标毛载在机黄凰退做宣市情招音浙博我B新技当冀调主吸请六4十巴其卫m多》江九境第得土淀人简据埃梦地选密”录软荐网具专电共指员廉康盒术企u亲委报控告赢体舆干建去不堡群悬6精历数想e窗存' \
        r'军顿排更聘津沉皮客祠T善酷性c园日络经部源设好面积绿站听命水成胡首属展狗优南国德范鞋8史习全弘海党通抱役湾顶3:本息移端克洁步度业夫列改搜腾。层信J周宽兵义微要用工说欧讯临7版云态方' \
        r'赋2浪勇局修文承V一名注,进泽产常近利视印律质关会款大认责单推书任P何天管量开健竞线复收北规扎字统|都申明0素末光y革乐黑热发活理协位行农之制总为作P准于科田年型除广高点波拥－布头登' \
        r'涉践扬C定闻荣涯华时法府敌对先绩团恶红穿深凤欢坚事决中来系丽正错论张能失坛D资期犯传、“强页锋担社参狐续聚扫台李变无困个众西挂斯百央牌见阿汉'


dic_str = "{'u8716': '线', 'u85a4': '开', 'u8a34': 'y', 'u6be0': '委', 'u7b76': '夫', 'u5958': '思', 'u694e': '软', 'u5bd8': '财', 'u6c54': '体', 'u9741': '丽', 'u69ac': '专', 'u9b7a': '狐', 'u4e20': '权', 'u8eaa': 'P', 'u802c': '文', 'u9e84': '挂', 'u6cd0': '舆', 'u6176': '音', 'u60c4': '凰', 'u924c': '登', 'u72da': '好', 'u51ca': '1', 'u7b39': '克', 'u995a': 'D', 'u9ee0': '百', 'u5518': '家', 'u97fa': '论', 'u73fe': '水', 'u6592': '江', 'u690e': '录', 'u7bf0': '。', 'u961e': '穿', 'u515e': '办', 'u5956': '讲', 'u612e': '宣', 'u94a2': '先', 'u8f02': '型', 'u70b8': '皮', 'u61f8': 'B', 'u729a': '源', 'u7f3e': '2', 'u550a': '育', 'u842a': '认', 'u95ca': '红', 'u6e7c': '历', 'u6b15': '亲', 'u856c': '何', 'u8502': '任', 'u9496': '对', 'u780e': '全', 'u6a5a': '共', 'u695e': '荐', 'u9e42': '西', 'u7066': '沉', 'u8036': 'V', 'u792c': '海', 'u68e7': '”', 'u8094': '名', 'u6840': '梦', 'u5b08': '治', 'u686e': '选', 'u73d4': '听', 'u7052': '津', 'u5a24': '争', 'u534c': '幕', 'u7756': '8', 'u7396': '站', 'u951e': '恶', 'u7ab7': ':', 'u53a0': '务', 'u613e': '市', 'u84f0': '书', 'u8f60': '高', 'u610a': '做', 'u9296': 'C', 'u98b6': '坛', 'u5de4': '脸', 'u59ae': '臂', 'u9a34': '、', 'u7360': '积', 'u69aa': '具', 'u5476': '服', 'u6c1c': '告', 'u9864': '张', 'u552d': '伦', 'u6f24': 'e', 'u8a08': '末', 'u5850': '铁', 'u7fa8': '局', 'u8ec4': '于', 'u638e': '主', 'u5cdf': '贸', 'u75e4': '国', 'u6fe2': '军', 'u8f98': '点', 'u9c42': '续', 'u5afc': '示', 'u7998': '党', 'u701e': '聘', 'u309e': '政', 'u7efc': '赋', 'u82d2': '律', 'u5bd4': '艺', 'u9a44': '“', 'u968a': '事', 'u8316': '质', 'u5bf4': '代', 'u6ec8': '数', 'u6230': '新', 'u5514': '如', 'u9e97': '斯', 'u67f4': '据', 'u63ac': '吸', 'u7216': '日', 'u7a90': '3', 'u9cfa': '李', 'u6722': '淀', 'u534d': 'b', 'u63b5': '六', 'u5af2': '生', 'u9278': '践', 'u6666': '得', 'u8106': '注', 'u8aae': '黑', 'u4e6c': '同', 'u5484': '典', 'u6f97': '窗', 'u9a74': '强', 'u3479': '渔', 'u8218': '视', 'u8ed8': '田', 'u72c2': '设', 'u5208': '魂', 'u7f70': '浪', 'u4f64': '9', 'u7d34': '用', 'u7564': '属', 'u7ed0': '态', 'u9a0e': '传', 'u7bb4': '搜', 'u963a': '深', 'u4e96': '件', 'u5675': 'r', 'u4fe0': '裁', 'u8944': '明', 'u6ac0': '企', 'u700a': '顿', 'u8958': '0', 'u5a68': '转', 'u9c48': '聚', 'u7cd6': '宽', 'u5896': '遗', 'u7b08': '移', 'u5fb2': '载', 'u9026': '拥', 'u8de2': '总', 'u5437': '与', 'u764e': '范', 'u6d3c': '不', 'u7a8e': '顶', 'u948c': '敌', 'u927a': '扬', 'u77fa': '习', 'u57a0': '极', 'u7288': '部', 'u5c28': '山', 'u9f96': '阿', 'u7b48': '度', 'u7d92': '欧', 'u61de': '我', 'u57fc': '东', 'u6bf2': '报', 'u8bc8': '行', 'u8e26': '为', 'u9716': '决', 'u7c33': '信', 'u69c3': '电', 'u7b3e': '洁', 'u8826': '扎', 'u60d2': '退', 'u915a': '布', 'u70f4': '祠', 'u8aa0': '乐', 'u750c': '胡', 'u7234': '经', 'u7cf4': '义', 'u6bfe': '控', 'u6142': '情', 'u759e': '狗', 'u79b0': '抱', 'u7f85': '勇', 'u8630': '竞', 'u9a78': '页', 'u9660': '坚', 'u81ba': '利', 'u738c': '绿', 'u97b4': '错', 'u892c': '申', 'u5d8c': '计', 'u7012': '排', 'u9d5a': '困', 'u8b30': '理', 'u8056': '一', 'u506c': 'd', 'u5b28': '届', 'u5e2e': '入', 'u6a64': '指', 'u754e': '首', 'u56d8': '加', 'u5342': '远', 'u8480': '单', 'u7b32': '端', 'u5a06': '厅', 'u7d78': '说', 'u6290': '技', 'u6403': '十', 'u79aa': '通', 'u8c50': '农', 'u67c6': '简', 'u54d6': '区', 'u7b93': '改', 'u5af4': '七', 'u73da': '命', 'u62b6': '当', 'u5556': '程', 'u4f12': '下', 'u4e21': '化', 'u88a4': '统', 'u7ac4': '本', 'u9272': '涉', 'u7220': '络', 'u9cf8': '台', 'u50a0': 'o', 'u7b7f': '列', 'u6a72': '廉', 'u92ee': '闻', 'u8926': '都', 'u8186': '进', 'u92ec': '定', 'u7114': '善', 'u99d2': '犯', 'u7c72': '周', 'u6e50': '精', 'u7d12': '要', 'u6d90': '堡', 'u7c30': '层', 'u5798': '民', 'u7c54': 'J', 'u989e': '能', 'u8e76': '作', 'u9362': '荣', 'u8ec6': '科', 'u7be6': '腾', 'u7206': '园', 'u846a': '责', 'u5624': '户', 'u9c50': '扫', 'u50c4': '《', 'u7db4': '临', 'u834c': '关', 'u6d98': '群', 'u655e': '多', 'u6a6a': '员', 'u60b3': '黄', 'u52d4': '平', 'u9468': '府', 'u93fe': '法', 'u6cd8': '干', 'u687a': '密', 'u8eb0': '准', 'u8497': '推', 'u9736': '中', 'u6f16': '想', 'u5b94': '.', 'u55ae': 'Q', 'u87f0': '规', 'u6b14': 'u', 'u88b6': '|', 'u8a18': '光', 'u6982': '网', 'u6060': '机', 'u63b1': '请', 'u9b48': '担', 'u61d3': '博', 'u6832': '埃', 'u5072': '外', 'u4f66': '神', 'u7470': '成', 'u5a56': '省', 'u7cea': '兵', 'u7e64': '云', 'u646a': '巴', 'u4f8c': '血', 'u7ed6': '方', 'u7e5e': '版', 'u75de': '南', 'u63e6': '4', 'u973a': '来', 'u8992': '素', 'u6844': '地', 'u6510': '卫', 'u652a': 'm', 'u8a6e': '革', 'u55ee': '补', 'u858e': '管', 'u98b1': '失', 'u8268': '印', 'u5570': '吾', 'u93c4': '华', 'u9642': '欢', 'u6c30': '赢', 'u71d2': 'c', 'u5882': '城', 'u615a': '招', 'u83f4': '大', 'u6320': '调', 'u6a92': '术', 'u6fb6': '存', 'u732e': '面', 'u8ee8': '年', 'u562c': '里', 'u9b74': '参', 'u83e8': '款', 'u8b28': '活', 'u94b2': '绩', 'u8fd6': '波', 'u974c': '正', 'u5c3c': '迎', 'u5c64': '藏', 'u973e': '系', 'u9b66': '社', 'u8aca': '热', 'u6724': '人', 'u9dee': '众', 'u5b6c': '洛', 'u62f6': '冀', 'u8596': '量', 'u57ac': '-', 'u78de': '弘', 'u5096': '上', 'u9160': '头', 'u79b8': '役', 'u6a7c': '盒', 'u9d16': '变', 'u5618': '集', 'u5c4c': '5', 'u6e12': '6', 'u85bc': '健', 'u7d60': '工', 'u4f3a': '学', 'u810c': ',', 'u7d9a': '讯', 'u66a2': '土', 'u9992': '期', 'u94c4': '团', 'u5fc0': '在', 'u75da': '优', 'u54dc': '飞', 'u5930': '负', 'u65ce': '境', 'u850a': 'P', 'u879c': '北', 'u9640': '凤', 'u856d': '天', 'u93b6': '涯', 'u7596': '展', 'u307a': '疆', 'u766c': '鞋', 'u5dca': '的', 'u59fc': '知', 'u9d44': '无', 'u8034': '承', 'u9f21': '央', 'u8190': '泽', 'u7016': '更', 'u6d05': '建', 'u7aec': '息', 'u8784': '收', 'u9f94': '见', 'u7b40': '步', 'u75f0': '德', 'u4e5a': '公', 'u9118': '－', 'u77ec': '史', 'u9f68': '牌', 'u57b0': '所', 'u81a2': '常', 'u5bf6': '有', 'u7b58': '业', 'u8d04': '之', 'u8196': '产', 'u9b00': '锋', 'u6a77': '康', 'u6daa': '悬', 'u7dca': '7', 'u71a6': '性', 'u8b6c': '协', 'u835c': '会', 'u5ac2': '哲', 'u8898': '字', 'u7112': 'T', 'u5e50': '标', 'u93e2': '时', 'u55fc': '持', 'u8d0a': '制', 'u8f08': '除', 'u59d8': '动', 'u9d80': '个', 'u7a40': '湾', 'u801a': '修', 'u8726': '复', 'u6d1c': '去', 'u52e2': '引', 'u61bc': '浙', 'u5ea2': '毛', 'u5aac': '马', 'u5872': '膀', 'u5252': '舟', 'u660e': '第', 'u657c': '》', 'u70f0': '客', 'u718b': '酷', 'u9fb2': '汉', 'u8b85': '位', 'u81ac': '近', 'u65c0': '九', 'u6490': '其', 'u5bf2': '频', 'u8b20': '发', 'u8f28': '广', 'u7d0a': '微', 'u997e': '资'}"

dic = eval(dic_str)
# for key in dic:
#     print(key,":" ,type(key))

for word in words:

    unicode_byte = word.encode("unicode_escape")
    unicode_str = str(unicode_byte, encoding="utf-8")
    # print(word,":" ,unicode_str)
    temp_key = unicode_str[1:]
    if dic.get(temp_key):
        print("！！！！！！！！当心这套字典库中的陷阱！！！！！！！！！！")
        print(temp_key ,":" ,dic.get(temp_key))
        print("！！！！！！！！当心这套字典库中的陷阱！！！！！！！！！！")