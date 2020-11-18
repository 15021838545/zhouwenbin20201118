'''
fixture 可以带参数和返回值
'''


#测试前置：准备测试数据，在测试用例中使用测试数据。测试数据使用fixture的返回值来表示
import pytest,requests


# @pytest.fixture()
# def username_pwd():
#     return {"username":"root","pwd":123456}
#
#
# def test_login(username_pwd):
#     print(f"测试数据为：{username_pwd['username']}")
#
#
# @pytest.fixture(params=['root','admin','administrator','12323'])
# def data(request):
#     return request.param
#
#
# @pytest.fixture(params=[
#     {"aaa":'root',"bbb":'成功'},
#     {"aaa":'administrator',"bbb":'成功'}])
# def data1(request):
#     return request.param
#
#
# def test_login2(data):
#     print(f"用户名：{data}测试")
#
#
# def test_login3(data1):
#     print(f"用户名：{data1['aaa']}测试结果为：{data1['bbb']}")


def register(data):
    url01 = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url01, data=data)
    return r


# @pytest.fixture(params=[
#     {"mobilephone": "137123456789", "pwd": "123456abc", "regname": "aaa","status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"},
#     {"mobilephone": "13745241111", "pwd": "123456abc", "regname": "aaa","status": 0, "code": "20110", "data": None, "msg": "手机号码已被注册"},
#     {"mobilephone": "13745241112", "pwd": "12345678901234567890", "regname": "aaa","status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"},
#     {"mobilephone": "13745241112", "pwd": "", "regname": "aaa","status": 0, "code": "20103", "data": None, "msg": "密码不能为空"},
#     {"mobilephone": "15021123669", "pwd": "123456", "regname": "","status": 1, "code": "10001", "data": None, "msg": "注册成功"}
# ])
# def data4(request):
#     return request.param
#
#
# def test_login4(data4):
#     print(f"mobilephone：{data4['mobilephone']},pwd：{data4['pwd']},regname:{data4['regname']}")
#     real = register(data4)
#     assert real.json()["msg"] == data4["msg"]
#     assert real.json()["code"] == data4["code"]


@pytest.fixture(params=[
    {'zhou':{"mobilephone": "137123456789", "pwd": "123456", "regname": ""},'wen':{"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}}
])
def data5(request):
    return request.param


def test_login5(data5):
    print(f"aaa：{data5['wen']['msg']}")
    print(f"aaa：{data5['zhou']['mobilephone']}")
    real = register(data5['zhou'])
    assert real.json()["msg"] == data5['wen']["msg"]



