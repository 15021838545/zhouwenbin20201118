'''
注册的测试脚本
'''
import pytest
from Pytest.ZongHe.caw import DataRead
from Pytest.ZongHe.baw import Member, DbOp


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_fail.yaml"))
def fail_data(request):
    return request.param


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_pass.yaml"))
def pass_data(request):
    return request.param


# 注册失败
def test_register_fail(fail_data, url, baserequests):
    print(f"测试数据为：{fail_data['casedata']}")
    print(f"测试数据为：{fail_data['expect']}")
    r = Member.register(url, baserequests, fail_data['casedata'])
    print(r.text)
    assert str(r.json()['msg']) == str(fail_data['expect']['msg'])
    assert str(r.json()['status']) == str(fail_data['expect']['status'])
    assert str(r.json()['code']) == str(fail_data['expect']['code'])


# 注册成功
def test_register_pass(pass_data, url, baserequests,db):
    print(f"测试数据为：{pass_data['casedata']}")
    print(f"测试数据为：{pass_data['expect']}")
    phone=pass_data['casedata']["mobilephone"]
    #初始化数据防止已有人注册过了
    DbOp.deleteUser(db, phone)
    #发送请求
    r = Member.register(url, baserequests, pass_data['casedata'])
    print(r.text)
    #检查响应结果
    assert str(r.json()['msg']) == str(pass_data['expect']['msg'])
    assert str(r.json()['status']) == str(pass_data['expect']['status'])
    assert str(r.json()['code']) == str(pass_data['expect']['code'])
    #检查实际有没有注册成功
    r=Member.getList(url,baserequests)
    assert phone in r.text
    #清理环境，根据手机号删除注册用户
    DbOp.deleteUser(db,phone)


# 重复注册
def test_register_repeat():
    pass
