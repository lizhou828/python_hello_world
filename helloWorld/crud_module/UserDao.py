# -*- coding:utf-8 -*-

# 创建以个 UserDao，继承BaseDao之后调用父类初始化方法，传递一个 User 对象给父类，我们就可以很方便的对 User 进行CRUD了。

import random
import math

# 引入同一目录下的py文件（来自指定py文件下，导入该文件下的某个类）
from helloWorld.crud_module.BaseDao import BaseDao
from helloWorld.crud_module.User import User
from helloWorld.crud_module.Page import Page


class UserDao(BaseDao):

    def __init__(self):
        super().__init__(User)
        pass

userDao = UserDao()

######################################## CRUD
print("查询所有数据" + "="*100)
userList = userDao.selectAll()
for u in userList:
    print(str(u))

print("根据主键查询" + "="*100)
user = userDao.selectByPrimaryKey(100)
print(str(user))
if not user:
    user = User()
    user.set_user_id(100)
    user.set_user_name("test")
    user.set_user_state(1)
    print("执行插入语句" + "="*100)
    result_count = userDao.insert(user)
    print("插入记录数：%s" % result_count)



print("执行删除语句" + "="*100)
result_count = userDao.deleteByPrimaryKey(100)
print("删除记录数：%s" % result_count)


######################################## 更新
print("执行更新语句" + "="*100)
user = User()
user.set_user_id(1)
user.set_user_name("测试更新")
result_count = userDao.updateByPrimaryKey(user)
print("更新记录数：%s" % result_count)

# print(userDao.updateByPrimaryKey())
# print(userDao.update())

######################################## 根据主键更新

# strList = list("QWERTYUI欧帕斯电饭锅和进口量自行车VB你们送人头刚回家个省份和健康的根本就可获得草泥马VB你们从v莫妮卡了VB了")
# for index in range(1000):
#     user = User()
#     user.set_id(index+1)
#     name = ""
#     for i in range(random.randint(3,8)):
#         name += random.chioce(strList)
#     user.set_name(name)
#     user.set_status(1)
#     i += 1
#     userDao.updateByPrimaryKey(user)



######################################## 分页查询

page = Page()
pageNum = 1
limit = 2
page.set_page(pageNum)
page.set_limit(limit)
total_count = userDao.selectCount()
page.set_total_count(total_count)
if total_count % limit == 0:
    total_page = total_count / limit
else:
    total_page = math.ceil(total_count / limit)
page.set_total_page(total_page)
begin = (pageNum - 1) * limit

for user in userDao.selectAllByPage(page):
    print(str(user))