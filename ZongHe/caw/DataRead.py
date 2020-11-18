# 读文件的公共方法
import configparser
import os

import yaml


def getProjectPath():
    '''
    获取当前工程路径
    :return:
    '''
    current_file_path=os.path.realpath(__file__)#当前文件路径
    print(current_file_path)
    dir_name=os.path.dirname(current_file_path)#文件所在目录
    print(dir_name)
    dir_name=os.path.dirname(dir_name)#上一级目录
    dir_name = os.path.dirname(dir_name)
    return  dir_name+"\\"


def readini(filePath, key):
    '''
    获取ini文件
    :param filePath:
    :param key:
    :return:
    '''
    real_path=getProjectPath()+filePath
    #调用configparser来解析配置文件
    config=configparser.ConfigParser()
    #读文件
    config.read(real_path)
    #env表示section根据key在对应的section中去value
    value = config.get("env", key)
    return value


def readyaml(filePath):
    real_path=getProjectPath() +filePath
    with open(real_path, 'r', encoding='utf-8') as yaml_file:
        config = yaml.load(yaml_file, Loader=yaml.FullLoader)
    return config


if __name__ == '__main__':
    print(getProjectPath())
    print(readini(r"ZongHe\data_env\env.ini", "url"))
    print(readini(r"ZongHe\data_env\env.ini", "db"))
    config=readyaml(r"ZongHe\data_case\register_fail.yaml")
    print(config)
