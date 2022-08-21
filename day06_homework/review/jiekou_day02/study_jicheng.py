"""
继承
"""
"""
单继承

"""
# 定义一个师傅类
class Master:
    def __init__(self):
        self.gongfu = '[五香配方]'
    def make_cake(self):
        print(f'使用{self.gongfu}制作了煎饼')
# 定义一个徒弟类，继承师傅
class Prentice(Master):
    pass

if __name__ == '__main__':
    xiaom = Prentice()
    xiaom.make_cake()

"""
多继承
徒弟想去学校再学一下啊
"""

class Master:
    def __init__(self):
        self.gongfu = '[五香配方]'
    def make_cake(self):
        print(f'使用{self.gongfu}制作了煎饼')
class School:
    def __init__(self):
        self.gongfu = '[香辣配方]'

    def make_cake(self):
        print(f'使用{self.gongfu}制作了煎饼')
# 定义一个徒弟类，继承师傅
class Prentice(School,Master):
    pass

if __name__ == '__main__':
    xiaom = Prentice()
    xiaom.make_cake()
"""
子类重写父类的同名属性和方法
"""
class Master:
    def __init__(self):
        self.gongfu = '[五香配方]'
    def make_cake(self):
        print(f'使用{self.gongfu}制作了煎饼')
class School:
    def __init__(self):
        self.gongfu = '[香辣配方]'

    def make_cake(self):
        print(f'使用{self.gongfu}制作了煎饼')
# 定义一个徒弟类，继承师傅
class Prentice(School,Master):
    def __init__(self):
        self.gongfu = '[独创配方]'
    def make_cake(self):
        print(f'使用{self.gongfu}制作了煎饼')
if __name__ == '__main__':
    xiaom = Prentice()
    xiaom.make_cake()

"""
⼦类调⽤⽗类的同名⽅法和属性
"""
class Master:
    def __init__(self):
        self.gongfu = '[五香配方]'
    def make_cake(self):
        print(f'使用{self.gongfu}制作了煎饼')
class School:
    def __init__(self):
        self.gongfu = '[香辣配方]'

    def make_cake(self):
        print(f'使用{self.gongfu}制作了煎饼')
# 定义一个徒弟类，继承师傅
class Prentice(School,Master):
    def __init__(self):
        self.gongfu = '[独创配方]'
    def make_cake(self):
        print(f'使用{self.gongfu}制作了煎饼')
    def master_make_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    def school_make_cake(self):
        School.__init__(self)
        School.make_cake(self)

if __name__ == '__main__':
    xiaom = Prentice()
    xiaom.make_cake()
    xiaom.master_make_cake()
    xiaom.school_make_cake()

"""
多层继承

"""
class Master:
    def __init__(self):
        self.gongfu = '[五香配方]'
    def make_cake(self):
        print(f'使用{self.gongfu}制作了煎饼')
class School:
    def __init__(self):
        self.gongfu = '[香辣配方]'

    def make_cake(self):
        print(f'使用{self.gongfu}制作了煎饼')
# 定义一个徒弟类，继承师傅
class Prentice(School,Master):
    def __init__(self):
        self.gongfu = '[独创配方]'
    def make_cake(self):
        self.__init__()
        print(f'使用{self.gongfu}制作了煎饼')
    def master_make_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    def school_make_cake(self):
        School.__init__(self)
        School.make_cake(self)
class zisun(Prentice):
    pass

if __name__ == '__main__':
    xiaom = zisun()
    xiaom.school_make_cake()
    xiaom.make_cake()

"""
super()调⽤⽗类⽅法

"""
class Master:
    def __init__(self):
        self.gongfu = '[五香配方]'
    def make_cake(self):
        print(f'使用{self.gongfu}制作了煎饼')
class School:
    def __init__(self):
        self.gongfu = '[香辣配方]'

    def make_cake(self):
        print(f'使用{self.gongfu}制作了煎饼')
# 定义一个徒弟类，继承师傅
class Prentice(School,Master):
    def __init__(self):
        super().__init__()
        self.gongfu = '[独创配方]'
    def make_cake(self):
        self.__init__()
        print(f'使用{self.gongfu}制作了煎饼')
    def master_make_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    def school_make_cake(self):
        School.__init__(self)
        School.make_cake(self)
    def super_make_cake(self):
        super().__init__()
        super().make_cake()
class zisun(Prentice):
    pass

if __name__ == '__main__':
    xiaom = Prentice()
    xiaom.super_make_cake()
    print(xiaom.gongfu)

"""
定义私有属性和⽅法
在属性和方法前增加两个下划线__
不能继承给子类的属性和方法需要添加私有权限
"""

class Master:
    def __init__(self):
        self.gongfu = '[五香配方]'
        self.__money = 100
    def make_cake(self):
        print(f'使用{self.gongfu}制作了煎饼')
    def get_money(self):
        print(self.__money)
    def set_money(self):
        self.__money -= 10
    def __get_info(self):
        print('私有方法')
    def print_info(self):
        self.__get_info()
# 定义一个徒弟类，继承师傅
class Prentice(Master):
    pass
if __name__ == '__main__':
    xiaom = Prentice()
    xiaom.make_cake()
    xiaom.set_money()
    xiaom.get_money()
    xiaom.print_info()

