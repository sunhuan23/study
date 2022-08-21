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
#     1、获取测试数据
readdata = ReadData()
datalist = readdata.readExcel()
print(datalist)
#     2、创建一个测试用例类
class TestCase(unittest.TestCase):
    #         2.1 创建一个测试用例方法
    def test_case(self):
        #         2.2 获取测试数据内，请求所需要的重要字段
        url = datalist[0]["interfaceUrl"]
        method = datalist[0]["method"]
        value = datalist[0]["value"]
        expect = datalist[0]["expect"]
        #         2.3 进行接口请求
        if method.lower() == 'get':
            res = requests.get(url=url,params=eval(value))
        elif method.lower() == 'post':
            res = requests.post(url=url,data=eval(value))
        #         2.4 进行断言
        print(res.text)
        self.assertEqual(res.json()["errorCode"],eval(expect),'测试不通过')
if __name__ == '__main__':
    unittest.main()
