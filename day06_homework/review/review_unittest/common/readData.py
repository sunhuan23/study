"""
定义一个读取文件的类：ReadData
    1、定义一个初始化方法：
        1.1 获取文件路径
        1.2 打开文件
        1.3 获取sheet页
        1.4 获取最大行数，代表用例条数
        1.5 获取最大列数，可以知道有多少个键值对
        1.6 获取首行，key
        1.7 组装一个列表并返回，默认为空
    2、定义一个组装数据的方法：readExcel
        2.1 循环每行数据作为测试用例
        2.2 数据和key进行拼接
        2.3 将拼接好的数据增加到列表中
        2.4 将列表返回
    3、定义一个读取json文件的方法：readJson
        2.1 获取json文件的路径
        2.2 打开json文件
        2.3 将所有json转为字典格式
        2.4 关闭文件
        2.5 获取所有的value值组成一个列表
        2.6 将列表返回
    4、定义一个读取yaml文件的方法：readYaml
        2.1 获取yaml文件的路径
        2.2 打开yaml文件
        2.3 将数据转为列表格式
        2.4 关闭yaml文件
        2.5 将列表返回
"""

import os
import xlrd
import json
import yaml
# 定义一个读取文件的类：ReadData
class ReadData:
    #     1、定义一个初始化方法：
    def __init__(self):
        #         1.1 获取文件路径
        self.excel_path = os.path.dirname(os.path.dirname(__file__)) + "/testData/data.xls"
        #         1.2 打开文件
        self.readbook = xlrd.open_workbook(self.excel_path)
        #         1.3 获取sheet页
        self.sheet = self.readbook.sheet_by_index(0)
        #         1.4 获取最大行数，代表用例条数
        self.max_row = self.sheet.nrows
        #         1.5 获取最大列数，可以知道有多少个键值对
        self.max_col = self.sheet.ncols
        #         1.6 获取首行，key
        self.frist_value = self.sheet.row_values(0)
        #         1.7 组装一个列表并返回，默认为空
        self.data_list = []
    #     2、定义一个组装数据的方法：readExcel
    def readExcel(self):
        #         2.1 循环每行数据作为测试用例
        for i in range(1, self.max_row):
            row_value = self.sheet.row_values(i)
        #         2.2 数据和key进行拼接
            data_dict = {self.frist_value[j]:row_value[j] for j in range(self.max_col) }
        #         2.3 将拼接好的数据增加到列表中
            self.data_list.append(data_dict)
        #         2.4 将列表返回
        return self.data_list
    # 3、定义一个读取json文件的方法：readJson
    def readJson(self):
        # 2.1 获取json文件的路径
        json_path = os.path.dirname(os.path.dirname(__file__)) + "/testData/data.json"
        # 2.2 打开json文件
        f = open(json_path, 'r')
        # 2.3 将json转为字典
        json_dict = json.load(f)
        # 2.4 关闭json文件
        f.close()
        # 2.5 获取所有的value值组成一个列表
        data_list = list(json_dict.values())
        # 2.6 将列表返回
        return data_list
    # 4、定义一个读取yaml文件的方法：readYaml
    def readYaml(self):
        #     2.1 获取yaml文件的路径
        yaml_path = os.path.dirname(os.path.dirname(__file__)) + "/testData/data.yaml"
        #     2.2 打开yaml文件
        f = open(yaml_path, 'r')
        #     2.3 将数据读取出来
        data_list = yaml.load(f,Loader=yaml.FullLoader)
        #     2.4 将yaml文件关闭
        f.close()
        #     2.5 将列表返回
        return data_list



if __name__ == '__main__':
    read = ReadData()
    # print(read.readExcel())
    # print(read.readJson())
    print(read.readYaml())
