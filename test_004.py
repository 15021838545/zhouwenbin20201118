'''
funtion级别有funtion、module、class、sassion
'''
import pytest


@pytest.fixture(scope='class')
def login():
    print("前置")
    yield
    print("后置")


class TestQuery():
    def test_001(self):
        print("测试功能用例1")

    def test_002(self, login):
        print("测试功能用例2")

    def test_003(self):
        print("测试功能用例3")


class TestDelete():
    def test_001(self, login):
        print("测试功能用例11")

    def test_002(self):
        print("测试功能用例12")

    def test_003(self):
        print("测试功能用例13")
