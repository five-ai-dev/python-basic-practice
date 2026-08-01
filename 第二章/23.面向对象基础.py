# 定义类 --->不推荐 动态的为对象添加属性
# class Car:
#     pass
#
#
# # 创建对象
# c1 = Car()
# #动态的为对象添加属性
# c1.color = "red"
# c1.brand = "BWM"
# c1.name = "m4"
# c1.price = 1000000
# print(c1.name)
# print(c1.__dict__)# 将对象的所有属性以字典的形式输出出来



# # 定义类
# class Car:
#     #__init__方法是初始化的方法，会在对象创建时自动调用，可以在该方法中为对象设置对应的属性
#     #self： 是第一个参数，表示当前所创立出来的实例对象
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car类型的对象初始化完毕，对象属性已经添加完毕")
# # 创建对象
# c1 = Car("红色","BWM","m4",1000000)
# print(c1.__dict__)








# 定义类
# class Car:
#     #__init__方法是初始化的方法，会在对象创建时自动调用，可以在该方法中为对象设置对应的属性
#     #self： 是第一个参数，表示当前所创立出来的实例对象
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car类型的对象初始化完毕，对象属性已经添加完毕")
# # 定义实例方法
#     def running(self):
#         print(f"{self.brand} {self.name} 正在高速行驶")
#     def total_cost(self,discount,rate = 0.1):
#         """
#         计算提车总费用，包括两部分：车的价格，税费
#         :param discount: 车的折扣
#         :param rate: 车的税费
#         :return: 提车总费用
#         """
#         total_cost = self.price * discount + rate * self.price
#         return total_cost
#
#
# # 测试
# c1 = Car("红色","BWM","m4",1000000)
# # 调用对象中的方法
# c1.running()
# total1 = c1.total_cost(0.9, 0.1)
# print(f"提车总费用是{total1}")
#
# total2 = c1.total_cost(0.9)
# print(f"提车总费用是{total2}")



# class Car:
#     #__init__方法是初始化的方法，会在对象创建时自动调用，可以在该方法中为对象设置对应的属性
#     #self： 是第一个参数，表示当前所创立出来的实例对象
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car类型的对象初始化完毕，对象属性已经添加完毕")
# # 定义实例方法
#     def running(self):
#         print(f"{self.brand} {self.name} 正在高速行驶")
#     def total_cost(self,discount,rate = 0.1):
#         """
#         计算提车总费用，包括两部分：车的价格，税费
#         :param discount: 车的折扣
#         :param rate: 车的税费
#         :return: 提车总费用
#         """
#         total_cost = self.price * discount + rate * self.price
#         return total_cost
#     def __str__(self):
#         return f"{self.color} {self.brand} {self.name} {self.price}"
#     def __eq__(self,other):
#         return self.color == other.color and self.brand == other.brand and self.name == other.name and self.price == other.price
#     def __lt__(self, other):
#         return self.price < other.price
#
#
# # 测试
# c1 = Car("红色","BWM","m4",1000000)
# print(c1)
#
# c2 = Car("红色","BWM","m4",1000000)
# print(c2)

# print(c1 == c2)
# print(c1 < c2)

#------------------------实例属性与类属性--------------------------
class Car:
    #__init__方法是初始化的方法，会在对象创建时自动调用，可以在该方法中为对象设置对应的属性
    #self： 是第一个参数，表示当前所创立出来的实例对象
    wheel = 4
    tax_rate = 0.1
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        self.wheel = 2
        print("Car类型的对象初始化完毕，对象属性已经添加完毕")
# 定义实例方法
    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶")
    def total_cost(self,discount,rate = 0.1):
        """
        计算提车总费用，包括两部分：车的价格，税费
        :param discount: 车的折扣
        :param rate: 车的税费
        :return: 提车总费用
        """
        total_cost = self.price * discount + rate * self.price
        return total_cost
    def __str__(self):
        return f"{self.color} {self.brand} {self.name} {self.price}"
    def __eq__(self,other):
        return self.color == other.color and self.brand == other.brand and self.name == other.name and self.price == other.price
    def __lt__(self, other):
        return self.price < other.price


# 测试
c1 = Car("红色","BWM","m4",1000000)
print(c1)
print(c1.name)
print(c1.wheel)#实例.属性，通过实例对象查找属性时，会先查找实例属性，实例属性不存在时再查找类属性。
print(Car.wheel)# 类名.属性
# c2 = Car("红色","BWM","m4",1000000)
# print(c2)










