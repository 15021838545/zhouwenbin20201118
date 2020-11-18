'''
脚本层的公共方法
'''
from Pytest.ZongHe.caw import DataRead
from Pytest.ZongHe.caw.BaseRequests import BaseRequests
import pytest


# 从环境文件中读取url
@pytest.fixture(scope='session')
def url():
    return DataRead.readini("ZongHe/data_env/teachar.ini", "url")


@pytest.fixture(scope='session')
def baserequests():
    return BaseRequests()


# 从环境文件中读取db
@pytest.fixture(scope='session')
def db():
    # 从ini中读取出来是字符串，将字符串转成字典，使用eval()函数
    return eval(DataRead.readini("ZongHe/data_env/teachar.ini", "db"))
