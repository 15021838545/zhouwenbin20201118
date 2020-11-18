'''
比较灵活的测试前置和后置，fixture
不受setup teardown命名的限制
'''
import pytest


# 测试前置，使用fixture来修饰
@pytest.fixture(scope='module')
def login():
    print("前置")
    yield
    print("后置")


@pytest.fixture(autouse=True)
def db_op():
    print("连接数据库")
    yield
    print("断开数据库")

def test_001():
    print("测试功能用例1")


# 方法1：将测试前置login作为参数传入
def test_002(login):
    print("测试功能用例2")


# 方法2：usefixtures使用前置login
@pytest.mark.usefixtures('login')
def test_003():
    print("测试功能用例3")
