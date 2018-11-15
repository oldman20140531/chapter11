# -*- coding:utf-8 -*-


class Vehicle:                                      # 定义对象
    def __init__(self, sp=50):          # 提供默认参数值
        '''
        __init__是类的内嵌方法，在类被创建时执行，
        通常把类的属性初始化放在该方法中,可自定义参数，
        作为创建是类属性的初始值,加入自定义参数后，
        必须在创建类时给定对应的参数，或用函数的默认参数
        '''
        print('init a vehicle.')
        self.speed = sp                         # 定义对象的属性
        self.distance = 0

    def drive(self, distance):                  # 定义对象的方法，方法必须包含self，就是对象本身，其属性作为方法中的参数
        self.distance += distance
        print('total drive ', self.distance)
        print('time is ', distance/self.speed)


class Bike(Vehicle):                            # 创建vehicle的子类Bike
    def __init__(self, sp=10):
        super(Bike, self).__init__(sp)          # 继承Vehicle的初始化方法
        print('init a bike.')                   # 在初始化方法中新增一个输出


class Car(Vehicle):                             # 创建vehicle的子类Car
    def __init__(self, sp=50, pr=2.5):          # 在初始化方法中新增一个参数
        super(Car, self).__init__(sp)           # 继承Vehicle的初始化方法
        print('init a car')
        self.price = pr                         # 在初始化方法中新增一个属性price

    def drive(self, distance):                  # 继承Vehicle的drive方法，新增计算和输出价格
        super(Car, self).drive(distance)
        print('cost ', distance*self.price)


c1 = Car()                                      # 创建Car的实例
c1.drive(100)
c1.drive(300)

b1 = Bike()
b1.drive(50)

# print(dir(c1))                                  # 返回对象的所有属性和方法
# print(type(c1))                                 # 返回变量的类型
# print(isinstance(c1, Car))                      # 判断变量是否是instance(实例)类型
