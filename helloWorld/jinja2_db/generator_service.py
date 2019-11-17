import pymysql

from helloWorld.jinja2_db.generator_config import HOST
from helloWorld.jinja2_db.generator_config import DATABASE
from helloWorld.jinja2_db.generator_config import PORT
from helloWorld.jinja2_db.generator_config import USER
from helloWorld.jinja2_db.generator_config import PASSWORD
from helloWorld.jinja2_db.generator_config import CHARSET
from helloWorld.jinja2_db.generator_config import TABLE_PREFIX


def connDB():
    conn = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE, charset=CHARSET)
    cur = conn.cursor()
    return (conn, cur)

def exeQuery(cur, sql):
    cur.execute(sql)
    return (cur)

def connClose(conn, cur):
    if conn:
        cur.close()
    if cur:
        conn.close()


def read_tables_from_db(cur):
    '''
    链接数据库，读取所有表的信息
    :return:
    '''

    query_tables_name_sql = """
        select table_name from information_schema.tables where table_schema='%s'
    """ % (DATABASE)

    exeQuery(cur,query_tables_name_sql)
    results = cur.fetchall()
    tables_name = []
    if not results:
        return tables_name
    for result in results:
        tables_name.append(result[0])
    return tables_name

def read_columns_from_table(cur,table_name):
    # 查询表的字段名称和类型
    sql = """SELECT COLUMN_NAME,IS_NULLABLE,DATA_TYPE,COLUMN_TYPE,COLUMN_COMMENT,COLUMN_KEY
                    FROM information_schema.columns
                    WHERE table_schema = '%s' AND table_name = '%s'
                 """ % (DATABASE, table_name)
    # 执行sql
    cur.execute(sql)
    # 返回所有查询结果
    results = cur.fetchall()
    columns = []
    if not results:
        return columns
    for result in results:
        column = {}
        column['name'] = result[0]
        column['is_null'] = True if result[1] == "YES" else False
        column['pk'] = True if result[-1] == "PRI" else False
        column['comment'] = result[-2]
        columns.append(column)
    return columns

def read_tables_info():
    conn, cur = connDB()
    tables_object = []

    try:
        tables_name = read_tables_from_db(cur)
        if not tables_name or len(tables_name) == 0:
            return None
        for table_name in tables_name:
            table = {}
            columns = []
            table['table_name'] = table_name
            table['class_name'] = table_name.replace(TABLE_PREFIX,"").capitalize()
            columns = read_columns_from_table(cur, table_name)
            table['columns'] = columns
            tables_object.append(table)
    except Exception as e :
        print(e)
    finally:
        connClose(conn, cur)
    return tables_object