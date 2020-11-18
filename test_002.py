class Test002:
    def setup_class(self):
        print("测试前置;类里的方法执行前调用")

    def teardown_class(self):
        print("测试后置;类里的方法执行后调用")

    def setup_method(self):
        print("每个方法前执行")

    def teardown_method(self):
        print("每个方法后执行")

    def test_001(self):
        print("测试功能用例1")

    def test_002(self):
        print("测试功能用例2")

    def test_003(self):
        print("测试功能用例3")