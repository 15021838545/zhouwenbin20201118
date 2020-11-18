'''
测试前置和后置
模块级（每个模块执行一次）和函数级（每个函数执行一次）通常一起使用
'''


def setup_module():
    print("测试前置")


def teardown_module():
    print("测试后置")


def setup_function():
    print("测试前置function：每个函数执行一次")


def teardown_function():
    print("测试后置function：每个函数执行一次")


def test_001():
    print("测试功能用例1")


def test_002():
    print("测试功能用例2")


def test_003():
    print("测试功能用例3")
