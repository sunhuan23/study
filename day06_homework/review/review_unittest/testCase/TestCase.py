"""
导包
    1、获取测试数据
    2、创建一个测试用例类
        2.1 创建一个测试用例方法
        2.2 获取测试数据内，请求所需要的重要字段
        2.3 进行接口请求
        2.4 进行断言
"""
# 导包
import unittest
import requests
from day06.review.review_unittest.common.readData import ReadData
from ddt import ddt,data,unpack
from day06.review.review_unittest.common.ConfigHttp import ConfigHttp
from day06.review.review_unittest.common.PublicAssertion import PublicAssertion
from  day06.review.review_unittest.common.log import logger
#     1、获取测试数据
readdata = ReadData()
datalist = readdata.readExcel()
print(datalist)
#     2、创建一个测试用例类
@ddt
class TestCase(unittest.TestCase):
    #         2.1 创建一个测试用例方法
    @data(*datalist)
    @unpack
    def test_case(self,**kwargs):
        #         2.3 进行接口请求
        logger.debug(kwargs)
        ch = ConfigHttp(kwargs)
        res = ch.confighttp()
        #         2.4 进行断言
        pa = PublicAssertion(kwargs['expect'],res)
        pa.publicAssertion()
if __name__ == '__main__':
    unittest.main(verbosity=2)
