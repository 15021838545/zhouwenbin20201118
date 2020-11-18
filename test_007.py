'''
接口测试场景比较难模拟，需要大量的工作才能完成
依赖第三方的接口，但是第三方的接口没有开发完成
测试环境不充分的情况下，怎么做接口测试
Mock
'''
import requests
import mock


class AliPay:
    def zhifu(self, data):
        # 接口功能尚未开发完成
        # 接口地址、get\post入参，返回值已经定义好了，有对应的接口文档
        r = requests.post("alipay interface", data=data).json()
        return r


class TestMock:
    def test_alipay(self):
        # 对要模拟的类创建一个对象
        aliPay = AliPay()
        # 模拟zhifu返回值为{"code":200,"msg":"支付成功"}
        aliPay.zhifu = mock.Mock(return_value={"code": 200, "msg": "支付成功"})
        data = {"OrderId": "1234567890", "Amount": 128.5, "Type": "支付宝"}
        r = aliPay.zhifu(data)
        print(r)


# member/withdraw 取现
class WithdRaw:
    def withdraw(self, data):
        r = requests.post("member/withdraw", data=data).json()
        return r


class TestWithdRaw:
    def test_withdraw01(self):
        aaa = WithdRaw()
        aaa.withdraw = mock.Mock(return_value={"code": 10001, "msg": "取现成功"})
        data = {"mobilephone": "15000000054", "amount": 20.20, "msg": "取现成功"}
        r = aaa.withdraw(data)
        print(r)

    def test_withdraw02(self):
        aaa = WithdRaw()
        aaa.withdraw = mock.Mock(return_value={"code": 20119, "msg": "余额不足，请修改提现额度"})
        data = {"mobilephone": "15000000054", "amount": 20.20, "msg": "余额不足，请修改提现额度"}
        r = aaa.withdraw(data)
        print(r)
        assert r["msg"] == data["msg"]

    def test_withdraw03(self):
        aaa = WithdRaw()
        aaa.withdraw = mock.Mock(return_value={"code": 20109, "msg": "手机格式不正确"})
        data = {"mobilephone": "150000000aa", "amount": 20.20, "msg": "手机格式不正确"}
        r = aaa.withdraw(data)
        print(r)
        assert r["msg"] == data["msg"]
