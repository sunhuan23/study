
"""
导包
1、定义一个类
    定义一个初始化方法
        获取config.ini路径
        实例化ConfigParser
        读取config数据
    定义一个读取section的方法
    定义一个读取option的方法
"""
# 导包
import os
from configparser import ConfigParser
# 1、定义一个类
class ReadConfig:
    #     定义一个初始化方法
    def __init__(self):
        #         获取config.ini路径
        self.config_path = os.path.dirname(os.path.dirname(__file__)) + '/config.ini'
        #         实例化ConfigParser
        self.conf = ConfigParser()
        #         读取config数据
        self.conf.read(self.config_path)
    #     定义一个读取section的方法
    def get_config(self,section,option=None):
        if option is None:
            #return self.conf.options(section)
            return self.conf.items(section)
    #     定义一个读取option的方法
        else:
            return self.conf.get(section,option)
if __name__ == '__main__':
    rc = ReadConfig()
    print(rc.get_config('mysql'))
    print(rc.get_config('mysql','port'))

