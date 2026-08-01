"""
采用面向对象的编程思想，完成教务系统的开发。教务管理系统可以管理在校学生的信息，通过控制台菜单与用户交互，具体功能如下：
    1. 添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
        1.1 输入学生姓名，语文成绩、数学成绩、英语成绩
        1.2 检查学生姓名是否已经存在，如果不存在，再添加（存在则，不添加）
        1.3 验证成绩范围（0-100）
        1.4 创建学生对象并添加到系统
    2. 修改学生成绩： 根据输入的学生姓名，修改对应的学生成绩
        2.1 输入要修改的学生姓名
        2.2 根据姓名查找该学生， 显示该生当前成绩信息
        2.3 输入新的语文、数学、英语成绩
        2.4 更新学生成绩数据
    3. 删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
    4. 查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
        4.1 输出格式：“姓名: 张三 | 语文： 85 | 数学： 90 | 英语： 95| 总分：270”
    5. 展示全部学生成绩：展示出系统中所有学生的成绩
"""
from os import name
from unittest import case

#学生类
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"学生姓名:{self.name}|  语文:{self.chinese} | 数学: {self.math} | 英语: {self.english}| 总分: {self.chinese + self.math + self.english}"

    # 修改学生信息
    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english


# 测试
# if __name__ == "__main__":
#     s1 = Student("小智", 95, 98, 97)
#     print(s1)
#     s1.update_score(english=96)
#     print(s1)
class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"
    def __init__(self):
        self.student = []
    #添加学生成绩
    def add_student(self):
        name = input("请输入学生姓名")

        # 判断学生姓名是否存在，如果存在，则添加失败（不能重复添加）
        for s in self.student:
            if s.name == name:
                print("该学生已经存在")
                return
        chinese = int(input("请输入学生语文成绩"))
        math = int(input("请输入学生数学成绩"))
        english = int(input("请输入学生英语成绩"))

        # 判断分数是否在0-100之间
        if 0<= chinese <=100 and 0<= math <= 100 and 0<= english <= 100:
            stu = Student(name, chinese, math, english)
            self.student.append(stu)
            print("学生信息添加成功")
        else:
            print("各科成绩必须在0-100之间")
    #修改学生成绩
    def update_student(self):
        name = input("请输入学生姓名")

        #根据学生姓名找到该学生信息
        for s in self.student:
            if s.name == name:
                print(f"当前成绩为{s}")
                chinese = int(input("请输入修改后的语文成绩"))
                math = int(input("请输入修改后的数学成绩"))
                english = int(input("请输入修改后的英语成绩"))
                # 判断分数是否在0-100之间
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese,math,english)
                    print("成绩修改成功")
                    print(f"修改后的成绩:{s}")
                    return
                else:
                    print("各科成绩必须得在0-100之间")
                    return
        print("未找到该学生，修改失败")


    #删除学生成绩
    def delete_student(self):
        name = input("请输入学生姓名")

        for s in self.student:
            if s.name == name:
                self.student.remove(s)
                print("该学生信息删除成功")
                return
        print("系统里无该学生，删除失败")
    #查询指定学生成绩
    def query_student(self):
        name = input("请输入学生姓名")
        for s in self.student:
            if s.name == name:
                print(f"该学生信息是{s}")
                return
        print("没有查到该学生")


    #展示全部学生成绩
    def list_student(self):
        for s in self.student:
            print(s)
    #运行系统
    def run(self):
        print(f"欢迎使用教务管理系统v{EduManagement.system_version}")

        while True:
            print()
            print("####################################")
            print("1.添加学生 2.修改学生 3.删除学生 4.查询指定学生 5.查询全部学生 6.退出系统 ")
            print("####################################")
            print()
            choice = input("请选择要执行的操作，输入1-6")
            try:
                match choice:
                    case "1":
                        self.add_student()
                    case "2":
                        self.update_student()
                    case "3":
                        self.delete_student()
                    case "4":
                        self.query_student()
                    case "5":
                        self.list_student()
                    case "6":
                        print("bye bye~")
                        break
                    case _:
                        print("输入错误，请输入1-6进行操作")
            except ValueError:
                print("输入的数据有问题，请检查后重新输入")
            except Exception:
                print("程序错误，请重新选择")
#测试-
if __name__ == "__main__":
    edu_management = EduManagement()
    edu_management.run()


# 采用面向对象编程思想完成如下需求
# 采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
# 系统采用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：
"""
1. 添加购物车： 用户根据提示录入商品名称、以及该商品的价格，数量，保存该商品信息到购物车。
2. 修改购物车： 要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量、输入完成后修改该商品信息
3. 删除购物车： 要求用户输入要删除的购物车名称，根据名称删除购物车中的商品
4. 查询购物车： 将购物车中的商品信息展示出来，格式为：“商品名称： xxx, 商品价格：xxx, 商品数量： xxx"。
5. 退出购物车


"""


# goods shoppingcart
# class Goods:
#     def __init__(self, name, price, count):
#         self.name = name
#         self.price = price
#         self.count = count
#
#     def __str__(self):
#         return f"商品名称:{self.name}, 商品价格:{self.price}, 商品数量:{self.count}"
#
#     def update_goods(self, name=None, price=None, count=None):
#         if name is not None:
#             self.name = name
#         if price is not None:
#             self.price = price
#         if count is not None:
#             self.count = count
#
#
# class ShoppingCart:
#     system_version = "1.0.0"
#     system_name = "购物车管理系统"
#
#     def __init__(self):
#         self.goods = []
#
#     # 添加购物车
#     def add_goods(self):
#         name = input("请输入要添加的商品名称")
#         # 判断商品是否存在，如果存在，则添加失败
#         for s in self.goods:
#             if s.name == name:
#                 print("该商品已经存在，添加失败")
#                 return
#         price = float(input("请输入商品价格"))
#         count = int(input("请输入商品数量"))
#         g = Goods(name, price, count)
#         self.goods.append(g)
#         print("商品添加完毕")
#
#     # 修改购物车
#     def update_goods(self):
#         name = input("请输入要修改的商品名称")
#         for s in self.goods:
#             if s.name == name:
#                 print(f"当前商品信息为{s}")
#                 price = float(input("请输入修改后商品价格"))
#                 count = int(input("请输入修改后商品数量"))
#                 s.update_goods(name, price, count)
#                 print("购物车商品修改成功")
#                 print(f"修改后为{s}")
#                 return
#         print("未找到该商品，修改失败")
#
#     # 删除购物车
#     def delete_goods(self):
#         name = input("请输入要删除的商品名称")
#         for s in self.goods:
#             if s.name == name:
#                 self.goods.remove(s)
#                 print("该商品删除成功")
#                 return
#         print("未找到该商品，删除失败")
#
#     # 查询购物车
#     def list_goods(self):
#         if len(self.goods) == 0:
#             print("购物车为空")
#             return
#         for s in self.goods:
#             print(s)
#     # 运行系统
#
#
#     def run(self):
#         print(f"欢迎大家使用购物车管理系统v{ShoppingCart.system_version}")
#         while True:
#            print()
#            print( " ##############################")
#            print("1:添加购物车, 2:修改购物车, 3:删除购物车, 4:查询购物车, 5:退出系统, ")
#            print(  "##############################")
#            print()
#            choice = int(input("请输入数字1-5进行操作"))
#            match choice:
#              case 1:
#                 self.add_goods()
#              case 2:
#                 self.update_goods()
#              case 3:
#                 self.delete_goods()
#              case 4:
#                 self.list_goods()
#              case 5:
#                 print("bye~")
#                 break
#              case _:
#                 print("操作无效，请输入数字1-5进行操作")
# # 测试
# if __name__ == "__main__":
#     shopping_cart = ShoppingCart()
#     shopping_cart.run()