"""
导包
定义一个对外函数：log
    1.1 使用basicConfig配置日志
    1.2 获取一个日志记录器
    1.3 返回日志记录器给外界使用

"""
import logging
# def log():
#     # 使用basicConfig配置日志
#     logging.basicConfig(level=logging.DEBUG,
#                                  format="日志:%(name)s-级别:%(levelname)s-时间%(asctime)s-模块%(module)s.py-第%(lineno)d行:%(message)s")
#     # 获取一个日志记录器
#     logger = logging.getLogger('Test')
#     # 返回日志记录器给外界使用
#     return logger


"""
定义一个对外的函数
    1.1 设置日志记录器
    1.2 设置日志级别
    1.3 设置日志格式
    1.4 创建并添加handler-控制台
    1.4 创建并添加handler-文件
"""
# 定义一个对外的函数
import os
path = os.path.dirname(os.path.dirname(__file__)) + '/testLog/'
def log():
    # 设置日志记录器
    logger = logging.getLogger('Test')
    # 设置日志级别
    logger.setLevel(logging.DEBUG)
    # 设置日志格式
    format1 = logging.Formatter("日志:%(name)s-级别:%(levelname)s-时间%(asctime)s-模块%(module)s.py-第%(lineno)d行:%(message)s")
    #创建并添加handler-控制台
    sh = logging.StreamHandler()
    sh.setFormatter(format1)
    logger.addHandler(sh)
    fh = logging.FileHandler(path + 'log.log')
    fh.setFormatter(format1)
    logger.addHandler(fh)
    return logger
logger = log()

if __name__ == '__main__':
    log = log()
    log.debug('这是debug')