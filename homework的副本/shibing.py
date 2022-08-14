"""
士兵开枪
"""
"""
4.士兵开枪
    需求：
    1）.士兵瑞恩有一把AK47
    2）.士兵可以开火(士兵开火扣动的是扳机)
    3）.枪 能够 发射子弹(把子弹发射出去)
    4）.枪 能够 装填子弹 --增加子弹的数量

需要定义的类：士兵、枪
士兵类的属性：
        士兵的名字   str   外界给与
        
士兵类的方法：
        开火
        
        
枪类的属性：
        枪的子弹数量  int  
枪类的方法：
        发射子弹
        装填子弹
"""
class Gun:
    def __init__(self):
        self.count = 10
    def hair(self):
        if self.count >0:
            self.count -= 1
        else:
            print('子弹不足')
    def add_bullet(self):
        if self.count<10:
            self.count += 10-self.count


class Soldiers:
    def __init__(self,name,modle):
        self.name = name
        self.modle = modle
    def fire(self,gun):
        gun.hair()
        self.count = gun.count
    def add_b(self,gun):
        gun.add_bullet()
        self.count = gun.count

    def __str__(self):
        return f'{self.name}有一把{self.modle},有{self.count}枚子弹'

if __name__ == '__main__':
    gun01 = Gun()
    ruien = Soldiers('瑞恩', 'AK47')
    for i in range(1,12):
        ruien.fire(gun01)
        print(ruien)
        if i>10:
            ruien.add_b(gun01)
            print(ruien)



