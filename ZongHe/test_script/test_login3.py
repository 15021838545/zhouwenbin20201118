'''
登陆脚本
'''
import pytest
from Pytest.ZongHe.caw import DataRead
from Pytest.ZongHe.baw import Member, DbOp


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_fail.yaml"))
def fail_denglu(request):
    return request.param



@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_pass.yaml"))
def pass_data(request):
    return request.param

@pytest.fixture()
def test_zhuce(pass_data,db,url,baserequests):
    phone=pass_data['casedata']["mobilephone"]
    #初始化数据防止已有人注册过了
    DbOp.deleteUser(db, phone)
    #发送请求
    zhuce=Member.register(url, baserequests, pass_data['casedata'])
    print("注册成功")
    yield
    #删除注册用户
    DbOp.deleteUser(db, phone)


def test_denglu(test_zhuce,url,baserequests,fail_denglu):
    dengluFail=Member.login(url, baserequests, fail_denglu['canshu'])
    print(dengluFail.text)
    assert str(dengluFail.json()['msg']) == str(fail_denglu['jieguo']['msg'])
    assert str(dengluFail.json()['status']) == str(fail_denglu['jieguo']['status'])
    assert str(dengluFail.json()['code']) == str(fail_denglu['jieguo']['code'])