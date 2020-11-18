'''
数据库操作
'''

from Pytest.ZongHe.caw import  MysqlOp


def deleteUser(db,phone):
    '''
    根据手机号删除用户
    :param db:env.ini db字典
    :param phone:
    :return:
    '''
    conn = MysqlOp.connect(db)
    MysqlOp.execute(conn,f"delete from Member where MobilePhone={phone};")
    MysqlOp.disconnect(conn)
