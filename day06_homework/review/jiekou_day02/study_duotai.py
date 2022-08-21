"""
多态
"""
"""
⾯向对象三⼤特性
封装
    将属性和⽅法书写到类的⾥⾯的操作即为封装
    封装可以为属性和⽅法添加私有权限
继承
    ⼦类默认继承⽗类的所有属性和⽅法
    ⼦类可以重写⽗类属性和⽅法
多态
    基于继承，传⼊不同的对象，产⽣不同的结果
"""
class Dog:
    def work(self):
        print('指哪打哪')
class ArmyDog(Dog):
    def work(self):
        print('追击坏人')
class DrugDog(Dog):
    def work(self):
        print('追击毒品')

class Person:
    def work_with_dog(self,dog):
        dog.work()
if __name__ == '__main__':
    d1 = Dog()
    d2 = ArmyDog()
    d3 = DrugDog()
    p1 = Person()
    p1.work_with_dog(d1)
    p1.work_with_dog(d2)


"""
类属性和类实例
1、类属性就是 类对象 所拥有的属性，它被 该类的所有实例对象 所共有。
2、类属性可以使⽤ 类对象 或 实例对象 访问。
"""
class dog:
    tooth = 10


print(dog.tooth)
wangcai = dog()
print(wangcai.tooth)

"""
修改类实例
"""
class dog:
    tooth = 10

dog.tooth = 8
print(dog.tooth)
wangcai = dog()
# 改变wangcai的属性，不会形象其他属性
wangcai.tooth = 6
print(wangcai.tooth)
print(dog.tooth)

"""
类方法
1、需要⽤装饰器 @classmethod 来标识其为类⽅法，对于类⽅法，第⼀个参数必须是类对象，⼀般以
cls 作为第⼀个参数。
"""
class dog:
    __tooth = 10
    @classmethod
    def get_tooch(cls):
        return cls.__tooth

wangcai = dog()
print(wangcai.get_tooch())

"""
静态方法：
1、需要通过装饰器 @staticmethod 来进⾏修饰，静态⽅法既不需要传递类对象也不需要传递实例对象
（形参没有self/cls）。
2、静态⽅法 也能够通过 实例对象 和 类对象 去访问。

静态方法的使用场景
1、当⽅法中 既不需要使⽤实例对象(如实例对象，实例属性)，也不需要使⽤类对象 (如类属性、类⽅
法、创建实例等)时，定义静态⽅法
2、取消不需要的参数传递，有利于 减少不必要的内存占⽤和性能消耗
"""
class dog:
    @staticmethod
    def info_print():
        print('这是⼀个狗类，⽤于创建狗实例....')
dog.info_print()
wangcai = dog()
wangcai.info_print()
