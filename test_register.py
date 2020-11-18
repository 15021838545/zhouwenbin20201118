'''
pytest命名规则：
测试文件已test_开头或结尾
测试类以Test开头
测试方法以test_开头
'''
import requests


# 登陆"http://jy001:8081/futureloan/mvc/api/member/login"
# 注册"http://jy001:8081/futureloan/mvc/api/member/register"

def register(data):
    url01 = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url01, data=data)
    return r


# 测试用例，手机号码格式不正确
def test_register_001():
    data = {"mobilephone": "137123456789", "pwd": "123456abc", "regname": "aaa"}
    expect = {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}
    real = register(data)
    assert real.json()["msg"] == expect["msg"]
    assert real.json()["code"] == expect["code"]


def test_register_002():
    canshu = {"mobilephone": "13745241111", "pwd": "123456abc", "regname": "aaa"}
    jieguo = {"status": 0, "code": "20110", "data": None, "msg": "手机号码已被注册"}
    real = register(canshu)
    assert real.json()["msg"] == jieguo["msg"]
    assert real.json()["code"] == jieguo["code"]


def test_register_003():
    canshu = {"mobilephone": "13745241112", "pwd": "12345678901234567890", "regname": "aaa"}
    jieguo = {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}
    real = register(canshu)
    assert real.json()["msg"] == jieguo["msg"]
    assert real.json()["code"] == jieguo["code"]


def test_register_004():
    canshu = {"mobilephone": "13745241112", "pwd": "", "regname": "aaa"}
    jieguo = {"status": 0, "code": "20103", "data": None, "msg": "密码不能为空"}
    real = register(canshu)
    assert real.json()["msg"] == jieguo["msg"]
    assert real.json()["code"] == jieguo["code"]


def test_register_005():
    canshu = {"mobilephone": "13745241234", "pwd": "123456", "regname": ""}
    jieguo = {"status": 1, "code": "10001", "data": None, "msg": "注册成功"}
    real = register(canshu)
    assert real.json()["msg"] == jieguo["msg"]
    assert real.json()["code"] == jieguo["code"]
