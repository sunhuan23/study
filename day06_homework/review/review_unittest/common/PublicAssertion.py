"""
导包：
    创建一个类
        创建一个初始化方法
            获取用例预期结果
            获取用例实际结果
        创建一个对外的断言方法


"""
import unittest
from jsonpath import jsonpath

class PublicAssertion(unittest.TestCase):
    def __init__(self,expect,res):
        super().__init__()
        self.expect = eval(expect)
        self.res = res.json()
    def publicAssertion(self):
        for k,v in self.expect.items():
           value =  jsonpath(self.res,'$..'+k)[0]
           self.assertEqual(str(value),v,'测试不通过')
