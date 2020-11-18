'''

'''
import  pytest

from Pytest.ZongHe.baw import DbOp, Member
from Pytest.ZongHe.caw import DataRead


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_data.yaml"))
def login_data(request):
    return request.param


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_setup.yaml"))
def login_setup(request):
    return request.param

#测试前置
@pytest.fixture()
def register(login_setup,url,baserequests,db):
    #注册
    phone=login_setup['casedata']["mobilephone"]
    #初始化数据防止已有人注册过了
    DbOp.deleteUser(db, phone)
    zhuce=Member.register(url, baserequests, login_setup['casedata'])
    print("注册成功")
    yield
    #删除注册用户
    DbOp.deleteUser(db, phone)


def test_login(register,login_data,url,baserequests):
    r=Member.login(url, baserequests, login_data['casedata'])
    assert r.json()['msg']==login_data['expect']['msg']

