# 原文链接：https://www.jianshu.com/p/13a62dfa17a9
# 先下载依赖的模块
# pip3 install pymysql


import pymysql
"""
-------------------------------------------------
   File Name：     db1
   Description :
   Author :       Lenovo
   date：          2018/1/6
-------------------------------------------------
   Change Activity:
                   2018/1/6:
-------------------------------------------------
"""
__author__ = 'Lenovo'

# 1、数据库的连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='money_note', charset='utf8')
# print(conn) #查看是否连接成功  成功的话返回：pymysql.connections.Connection object at 0x000000B3A9AEAA90>

# 2、创建操作的游标
cursor = conn.cursor()

# 3、设置输入输出的字符编码以及自动提交
cursor.execute('set names utf8')
cursor.execute('set autocommit = 1') #0:false   1:true

# 4、编写sql语句：crud
# sql  = "insert into tb_user (name, pwd) values('zlc','123456')"  #增
# sql  = "insert into tb_user (name, pwd) values('zlc_1','123456')"  #增
# sql = "delete from tb_user where id={0}".format(2)   #删
# sql = "update tb_user set pwd='1111111' where name = 'zlc_1'"  #改
sql = 'select * from users'
print(sql)

# 5、执行sql并且得到结果集
cursor.execute(sql)

# 得到结果集有三种方式：全部 cursor.fetchall()    单个 cursor.fetchone()  多条 cursor.fetchmany(n)
result = cursor.fetchall()
print(result)

# 6、关闭游标和连接
cursor.close()
conn.close()

