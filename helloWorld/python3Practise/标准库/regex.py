# -*- coding:utf-8 -*-

import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))

print(re.search('com', 'www.runoob.com'))
result = re.search('共\d+页','共13页  共377条记录')
print(result.group())
page = result.group().replace("共","").replace("页","")
page = int(page)
print("page = %d ,type of page = %s" % (page,type(page)))