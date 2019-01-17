import pymysql

from builtins import int

#连接数据库
def connDB():
    conn = pymysql.connect(host='localhost',user='root',passwd='******',db='student')
    cur = conn.cursor()
    return (conn,cur)

#更新语句，可执行Update，Insert语句
# 这里要讲一下exeUpdate函数，也许在别人的源码中也看到过这一个函数，但参数只有两个：cur与sql，没有conn，
# 如果函数内不加上conn.commit()这一行代码，在新增时不会报错，也会提示成功，
# 但数据库中是不会看到自己新加的数据的，这一句代码的作用: 就类似于保存当前修改，不加上当前这一行代码，当前修改或者新增操作就没有实现。
def exeUpdate(conn,cur,sql):
    sta = cur.execute(sql)
    conn.commit()
    return (sta)

#删除语句，可批量删除
def exeDelete(cur,IDs):
    for eachID in IDs.split(' '):
        sta = cur.execute('delete from students where Id=%d'%int(eachID))
    return (sta)

#查询语句
def exeQuery(cur,sql):
    cur.execute(sql)
    return (cur)

#关闭所有连接
def connClose(conn,cur):
    cur.close()
    conn.close()



#      在这里，基本的增删改查的函数基本完成，
# ---------------------
# 作者：叶长风
# 来源：CSDN
# 原文：https://blog.csdn.net/u012734441/article/details/41283595
# 版权声明：本文为博主原创文章，转载请附上博文链接！