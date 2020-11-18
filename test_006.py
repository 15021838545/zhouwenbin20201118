'''
mark标记
skip：这个版本有缺陷，导致某个用例执行不通过时可以跳过这个用例执行，等待缺陷解决后再执行
自定义标记：随着代码规模增大，包含功能测试、接口测试、性能测试、冒烟测试，筛选自己想要执行的测试用例
'''
import pytest


def test_001():
    print("测试功能用例1")


@pytest.mark.skip(reason="有缺陷，缺陷号为123456789，等待缺陷解决后再执行")
def test_002():
    print("测试功能用例2")


@pytest.mark.bbb
def test_003():
    print("测试功能用例3")


@pytest.mark.aaa
class TestUserMark:
    @pytest.mark.bbb
    def test_004(self):
        print("测试功能用例4")

    def test_005(self):
        print("测试功能用例5")

    def test_006(self):
        print("测试功能用例6")
