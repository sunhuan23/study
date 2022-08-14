"""
需求主线:
小明爱跑步，爱吃东西。
    1）小明体重75.0公斤
    2）每次跑步会减肥0.5公斤
    3）每次吃东西体重会增加1公斤
    4）小美的体重是45.0公斤

需要定义的类:人类
地瓜类的属性:
    体重       weight      float      默认值:0
    名字       name        str
跑步的方法:
    1.跑:running
        weight -= 0.5

    2.吃东西 eating
        weight += 1
        
    3.魔法方法__str__
"""
class People:
    def __init__(self,weight,name):
        self.weight = float(weight)
        self.name = name
    def running(self):
        self.weight -=1
    def eating(self):
        self.weight += 0.5
    def __str__(self):
        return f'{self.name}的体重是{self.weight}'

if __name__ == '__main__':
    xiaoming = People(75.0,'小明')
    xiaoming.running()
    xiaoming.eating()
    print(xiaoming)