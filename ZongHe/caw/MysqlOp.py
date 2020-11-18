'''
数据库操作
'''

# 链接数据库
import pymysql


def connect(db):
    '''
    :param db: db={"ip":"jy001", "port":4406, "dbName":"future", "username":"root", "pwd":"123456"}
    :return:
    '''
    host = db['ip']
    port = int(db['port'])
    user = db['username']
    name = db["dbName"]
    pwd = db['pwd']

    try:
        conn = pymysql.connect(host=host, port=port, user=user, database=name, password=pwd, charset='utf8')
        print(f"连接数据库成功{host}:{port}")
    except Exception as e:
        print(f"连接数据库异常，异常信息为：{e}")
    return conn


# 断开数据库
def disconnect(conn):
    try:
        conn.close()
        print("断开成功")
    except Exception as e:
        print(f"断开连接失败：{e}")


# 执行sql语句
def execute(conn, sql):
    try:
        cursor = conn.cursor()  # 获取游标
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        print(f"执行成功{sql}")
    except Exception as e:
        print(f"执行SQL语句{sql}失败：{e}")

