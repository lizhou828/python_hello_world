# -*- coding:utf-8 -*-
# pip3 install pandas

# pip3 install cryptography
# pip3 install pyOpenSSL
# pip3 install certifi

import requests
import re
import random
import time
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import pandas as pd

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  ###禁止提醒SSL警告

##腾讯地图  开发者密钥ID
key='HQBBZ-7EQ3J-Q3FF2-FIUTE-ZJDOZ-6AF7V'

class dzdp(object):

    def __init__(self,keyword):
        self.keyword=keyword
        self.citylist=[
        '北京','天津','上海','重庆','合肥','宿州','淮北','阜阳','蚌埠','淮南','滁州','马鞍山','芜湖','铜陵','安庆','黄山','六安','池州','宣城','亳州','厦门','福州','南平','三明','莆田','泉州','漳州',
        '龙岩','宁德','兰州','嘉峪关','金昌','白银','天水','酒泉','张掖','武威','庆阳','平凉','定西','陇南','甘南','广州','深圳','清远','韶关','河源','梅州','潮州','汕头','揭阳','汕尾','惠州','东莞',
        '珠海','中山','江门','佛山','肇庆','云浮','阳江','茂名','湛江','贵阳','六盘水','遵义','安顺','毕节','铜仁','石家庄','邯郸','唐山','保定','秦皇岛','邢台','张家口','承德','沧州','廊坊','衡水',
        '哈尔滨','齐齐哈尔','黑河','大庆','伊春','鹤岗','佳木斯','双鸭山','七台河','鸡西','牡丹江','绥化','郑州','开封','洛阳','平顶山','安阳','鹤壁','新乡','焦作','濮阳','许昌','漯河','三门峡','南阳',
        '商丘','周口','驻马店','信阳','济源','巩义','邓州','永城','汝州','武汉','十堰','襄樊','荆门','孝感','黄冈','鄂州','黄石','咸宁','荆州','宜昌','随州','仙桃','天门','潜江','长沙','衡阳',
        '张家界','常德','益阳','岳阳','株洲','湘潭','郴州','永州','邵阳','怀化','娄底','长春','吉林市','白城','松原','四平','辽源','通化','白山','南昌','九江','景德镇','鹰潭','新余','萍乡','赣州',
        '上饶','抚州','宜春','吉安','南京','徐州','连云港','宿迁','淮安','盐城','扬州','泰州','南通','镇江','常州','无锡','苏州','沈阳','大连','朝阳','阜新','铁岭','抚顺','本溪','辽阳','鞍山','丹东',
        '营口','盘锦','锦州','葫芦岛','济南','青岛','聊城','德州','东营','淄博','潍坊','烟台','威海','日照','临沂','枣庄','济宁','泰安','莱芜','滨州','菏泽','西安','延安','铜川','渭南','咸阳','宝鸡',
        '汉中','榆林','商洛','安康','太原','大同','朔州','阳泉','长治','晋城','忻州','吕梁','晋中','临汾','运城','成都','广元','绵阳','德阳','南充','广安','遂宁','内江','乐山','自贡','泸州','宜宾',
        '攀枝花','巴中','达州','资阳','眉山','雅安','昆明','曲靖','玉溪','丽江','昭通','思茅','临沧','保山','杭州','宁波','湖州','嘉兴','舟山','绍兴','衢州','金华','台州','温州','丽水','西宁',
        '海口市','三亚市','南宁','桂林','柳州','梧州','贵港','玉林','钦州','北海','防城港','崇左','百色','河池','来宾','贺州','呼和浩特','包头','乌海','赤峰','呼伦贝尔','通辽','乌兰察布','鄂尔多斯',
        '巴彦淖尔','银川','石嘴山','吴忠','中卫','固原','拉萨','乌鲁木齐','克拉玛依','石河子','阿拉尔','图木舒克','五家渠','北屯'
        ]


    ##城市内搜索结果
    def search_qqmap(self):
        df = pd.DataFrame(columns=('ID', '店名', '地址', '电话', '类别', '纬度', '经度', '邮编', '省', '市', '区'))
        x=0
        for i in self.citylist:
            p=1
            while p>0:
                time.sleep(0.22)
                url='https://apis.map.qq.com/ws/place/v1/search?boundary=region({},0)&page_size=20&page_index={}&keyword={}&orderby=_distance&key={}'.format(i,p,self.keyword,key)
                req=requests.get(url=url,verify=False).json()
                data=req['data']
                print(p,data)
                if data!=[]:
                    for j in data:
                        id=j['id']  ##ID
                        title=j['title']  ##店名
                        address=j['address']  ##地址
                        tel=j['tel']   ##电话
                        category=j['category']   ##类别
                        lat=j['location']['lat']  ##纬度
                        lng=j['location']['lng']  ##经度
                        adcode=j['ad_info']['adcode']  ##邮编
                        province=j['ad_info']['province']   ##省
                        city=j['ad_info']['city']   ##市
                        district=j['ad_info']['district']  ##区
                        print(id, title, address, tel,category, lat, lng,adcode, province, city,district)
                        df.loc[x] = [id, title, address, tel,category, lat, lng,adcode, province, city,district]
                        x = x + 1
                    p = p + 1
                else:
                    p=-1
        df.to_excel(self.keyword+'.xlsx',index=False, encoding="GB18030")

if __name__ == '__main__':
    keyword='综合商场'
    dp=dzdp(keyword)
    dp.search_qqmap()
