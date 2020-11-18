'''
用户模块接口（注册、登陆、充值、用户列表、取现。。。）

注册"http://jy001:8081/futureloan/mvc/api/member/register"
'''


def register(url, baserequests, data):
    '''
    发送注册接口
    :param url: http//jy001:8081/
    :param baserequests: 一个BaseRequests实例
    :param data: 接口参数
    :return:
    '''
    # 注册
    # "http://jy001:8081/futureloan/mvc/api/member/register"
    url = url + "futureloan/mvc/api/member/register"
    r = baserequests.post(url, data=data)
    return r


def login(url, baserequests, data):
    url = url + "futureloan/mvc/api/member/login"
    r = baserequests.post(url, data=data)
    return r


def getList(url, baserequests):
    url = url + "futureloan/mvc/api/member/list"
    r = baserequests.get(url)
    return r
