"""
将小于房子剩余面积的家具摆放到房子中
"""
"""
家具类:
    属性:
        名字  字符串   外界给与
        面积   数值    外界给与
    方法:
        魔法方法str

房子类:
    属性:
        面积       数值    外界给与
        家具列表    列表    初始为空
        剩余面积    数值    默认等于面积
    方法:
        摆放家具
            参数:家具
            判断房子剩余面积是否大于家具面积
                是:将家具摆放进家具列表
                剩余面积-=家具面积
                否:提示装不下了
        
        魔法方法str
"""

# 家具类:
class furniture:
    # 属性:
    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        return f"家具名称{self.name},家具面积{self.area}平"

class House():
    def __init__(self,erea):
        self.erea = erea
        self.r_erea = erea
        self.furniture = []

    def put_f(self,furniture):
        if self.r_erea >= furniture.area:
            self.furniture.append(furniture.name)
            self.r_erea -= furniture.area
        else:
            print("装不下了")

    def __str__(self):
        return f'房子总面积{self.erea}平,剩余面积{self.r_erea}平，摆放了{self.furniture}'


# 调试
if __name__ == '__main__':
    # 实例化
    table = furniture("桌子",5)
    print(table)
    bed = furniture('床',95)
    print(bed)
    h = House(100)
    h.put_f(table)
    h.put_f(bed)
    print(h)