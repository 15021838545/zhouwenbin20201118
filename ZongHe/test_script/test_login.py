'''
登陆脚本
'''
import pytest
from Pytest.ZongHe.caw import DataRead
from Pytest.ZongHe.baw import Member, DbOp


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_fail.yaml"))
def fail_denglu(request):
    return request.param


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_pass.yaml"))
def pass_denglu(request):
    return request.param


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_pass.yaml"))
def pass_data(request):
    return request.param


#登陆
def test_fail_denglu(pass_data,fail_denglu,url,baserequests,db,pass_denglu):
    print(f"测试数据为：{pass_data['casedata']}")
    print(f"测试数据为：{pass_data['expect']}")
    print(f"测试数据为：{fail_denglu['canshu']}")
    print(f"测试数据为：{fail_denglu['jieguo']}")

    phone=pass_data['casedata']["mobilephone"]
    #初始化数据防止已有人注册过了
    DbOp.deleteUser(db, phone)
    #发送请求
    zhuce=Member.register(url, baserequests, pass_data['casedata'])
    print("注册成功")

    dengluFail=Member.login(url, baserequests, fail_denglu['canshu'])
    print(dengluFail.text)
    assert str(dengluFail.json()['msg']) == str(fail_denglu['jieguo']['msg'])
    assert str(dengluFail.json()['status']) == str(fail_denglu['jieguo']['status'])
    assert str(dengluFail.json()['code']) == str(fail_denglu['jieguo']['code'])

#
# #登陆成功
# def test_pass_denglu(pass_denglu,url, baserequests):
#
#     print(f"测试数据为：{pass_denglu['canshu']}")
#     print(f"测试数据为：{pass_denglu['jieguo']}")
#     r=Member.login(url, baserequests, pass_denglu['canshu'])
#     print(r.text)
#     assert str(r.json()['msg']) == str(pass_denglu['jieguo']['msg'])
#     assert str(r.json()['status']) == str(pass_denglu['jieguo']['status'])
#     assert str(r.json()['code']) == str(pass_denglu['jieguo']['code'])




