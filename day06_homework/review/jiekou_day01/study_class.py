class Washer:
    def wash(self):
        print('我会洗衣服')

    def print_info(self):
        print(f'我的身高是{haier.height}')
        print(f'我的身高是{haier.weight}')

if __name__ == '__main__':
    haier = Washer()
    haier.wash()
    """
    添加和获取对象属性
    """
    haier.height = 10
    haier.weight = 100
    haier.print_info()
"""
魔法方法__init__
"""
class Washer:
    def __init__(self):
        self.height = 11
        self.weight = 22
    def wash(self):
        print('我会洗衣服')

    def print_info(self):
        print(f'我的身高是{self.height}')
        print(f'我的身高是{self.weight}')

if __name__ == '__main__':
    haier = Washer()
    haier.print_info()

"""
带参数的__init__()
"""


class Washer:
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight

    def wash(self):
        print('我会洗衣服')

    def print_info(self):
        print(f'我的身高是{self.height}')
        print(f'我的体重是{self.weight}')
    """
     __str__()
    """
    def __str__(self):
        return f'我的身高是{self.height},我的体重是{self.weight}'
    """
    __del__
    """
    def __del__(self):
        print('被删除了对象')


if __name__ == '__main__':
    haier = Washer(10,100)
    haier.print_info()
    print(haier)
    del haier

"""
需求主线：
烤地瓜
1. 被烤的时间和对应的地⽠状态：
0-3分钟：⽣的
3-5分钟：半⽣不熟
5-8分钟：熟的
超过8分钟：烤糊了
2. 添加的调料：
⽤户可以按⾃⼰的意愿添加调料
1、需要定义类：地瓜类
    需要定义的属性：
        时间
        地瓜状态
        调料列表
    需要定义的方法：烤地瓜
                
                  添加调料
                __str__方法
                
"""
# 1、需要定义类：地瓜类
class potatoes:
    def __init__(self):
        # 需要定义的属性：
        # 时间
        self.time = 0
        # 地瓜状态
        self.status = ''
        # 调料列表
        self.tiaoliao = []
    # 需要定义的方法：烤地瓜
    def bake_potatoes(self,t):
        self.time += t
        if 0<=self.time<3:
            self.status ='生的'
        elif 3<=self.time<5:
            self.status = '半生不熟'
        elif 5<=self.time<8:
            self.status = '熟的'
        else:
            self.status = '烤糊了'

    # 添加调料
    def add_tiaoliao(self,*args):
        self.tiaoliao.extend(args)

    # __str__方法
    def __str__(self):
        return f'地瓜烤了{self.time}分钟，{self.status}，增加了{self.tiaoliao}'
if __name__ == '__main__':
    tudou = potatoes()
    tudou.bake_potatoes(1)
    tudou.bake_potatoes(3)
    tudou.add_tiaoliao('盐','芥末')
    tudou.add_tiaoliao('油')
    print(tudou)

"""
2、小明爱跑步，爱吃东西。
    1）小明体重75.0公斤
    2）每次跑步会减肥0.5公斤
    3）每次吃东西体重会增加1公斤
    4）小美的体重是45.0公斤
需要定义的类：人类
    需要定义的属性：
            名字  外界给予
            体重  外界给予
    需要定义的方法：
            跑步
            每次跑步会减肥0.5公斤
            吃东西
            每次吃东西体重会增加1公斤
"""
# 需要定义的类：人类
class people:
    #     需要定义的属性：
    def __init__(self,name,weight):
        #             名字  外界给予
        self.name = name
        #             体重  外界给予
        self.weight = weight
    #     需要定义的方法：
    #             跑步
    def run(self):
        #             每次跑步会减肥0.5公斤
        self.weight -= 0.5
    #             吃东西
    def eat(self):
        #             每次吃东西体重会增加1公斤
        self.weight += 1
    def __str__(self):
        return f'我的叫{self.name},我的体重{self.weight}'
if __name__ == '__main__':
    xiaom = people('小明',75.0)
    xiaom.run()
    xiaom.run()
    xiaom.run()
    xiaom.eat()
    xiaom.eat()
    print(xiaom)
"""
摆放家具
    需求：
    1）.房子有户型，总面积和家具名称列表
       新房子没有任何的家具
    2）.家具有名字和占地面积，其中
       床：占4平米
       衣柜：占2平面
       餐桌：占1.5平米
    3）.将以上三件家具添加到房子中
    4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
需要定义的类：家具类
            房子类
家具类需要定义的属性：
        家具名称
        家具面积
    需要定义的方法：
        str
房子类需要定义的属性：
        户型     外界给予
        总面积   外界给予
        剩余面积  初始值等于总面积
        家具列表  空列表
    需要定义的方法：
        摆放家具
        __str__
"""
# 家具类需要定义的属性：
class furniture:
    def __init__(self,name,area):
        #         家具名称
        self.name = name
        #         家具面积
        self.area = area
#     需要定义的方法：
    def __str__(self):
        return f'{self.name}的占地面积{self.area}平'

# 房子类需要定义的属性：
class House:
    def __init__(self,model,all_area):
        #         户型     外界给予
        self.model = model
        #         总面积   外界给予
        self.all_area = all_area
        #         剩余面积  初始值等于总面积
        self.s_area = all_area
        #         家具列表  空列表
        self.f_list = []
    #     需要定义的方法：
    def add_furniture(self,jiaju):
        #         摆放家具
        if jiaju.area < self.s_area:
            self.f_list.append(jiaju.name)
            self.s_area -= jiaju.area
        else:
            print('摆不下了')
    def __str__(self):
        return f'房子的户型是{self.model},总面积{self.all_area}平，剩余面积{self.s_area},摆放了{self.f_list}'

if __name__ == '__main__':
    zhuoz = furniture('桌子',11)
    chuang = furniture('床',128)
    sishi = House('四居室',140)
    sishi.add_furniture(zhuoz)
    sishi.add_furniture(chuang)
    print(sishi)

"""
4.士兵开枪
    需求：
    1）.士兵瑞恩有一把AK47
    2）.士兵可以开火(士兵开火扣动的是扳机)
    3）.枪 能够 发射子弹(把子弹发射出去)
    4）.枪 能够 装填子弹 --增加子弹的数量
需要定义的类:枪类
           士兵类
枪类需要定义的属性：
           枪的名称
           枪的子弹
枪类需要定义的方法：
           发射子弹
           状态子弹
           
士兵类需要定义的属性：
           名字：
士兵类需要定义的方法：
           开火
           装子弹
"""

class Gun:
    # 枪类需要定义的属性：
    def __init__(self,name):
        # 枪的名称
        self.name = name
        # 枪的子弹
        self.count = 0
    # 枪类需要定义的方法：
    # 发射子弹
    def put_bullet(self):
        if self.count >0:
            print('biu~')
            self.count -=1
        else:
            print('子弹不足')
    # 装子弹
    def add_bullet(self):
        self.count += 10
    def __str__(self):
        return f'{self.name}有{self.count}发子弹'
class shibing:
    def __init__(self,name,gun):
        self.name = name
        self.gun = gun
    def put_bullet(self):
        self.gun.put_bullet()
    def add_bullet(self):
        self.gun.add_bullet()
    def __str__(self):
        return f'我的名字是{self.name},我有一把{self.gun.name},还有{self.gun.count}发子弹'

if __name__ == '__main__':
    AKF = Gun('AKF')
    # AKF.add_bullet()
    # AKF.put_bullet()
    # AKF.put_bullet()
    ruien = shibing('瑞恩',AKF)
    ruien.add_bullet()
    ruien.put_bullet()
    ruien.put_bullet()

    print(ruien)

