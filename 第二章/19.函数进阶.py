################ 函数-变量的作用域 ###################
# 全局变量 ：在函数外部和函数内部都是可以访问的
# num = 100
# #定义函数
# def circle_area(r):
#     # 局部变量 只能在函数内部使用
#     pi = 3.14
#     area = pi * r * r
#     global num
#     num = 10000
#     print("num = ", num)
#     return area
# # 调用函数
# c_area = circle_area(10)
# print(c_area)
# print("num = ", num)

#----------------------函数 - 传参方式------------------
# 定义函数
# def reg_stu(name, age, gender, city):
#     print(f"注册成功， 姓名: {name}, 年龄: {age}, 性别: {gender}, 城市: {city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
#
# # 传参方式一： 位置参数(与定义位置一一对应）
# stu = reg_stu("小智", 18, "男", "马耳他")
# print(stu)
#
#
#
# # 传参方式二 ：关键字参数（顺序无关0
# stu = reg_stu(name = "小智",  age = 18, gender = "男", city = "马耳他" )
# print(stu)
# stu = reg_stu(age = 28, gender = "女", city = "马耳他", name = "小美",   )
# print(stu)
# # 传参方式三 ： 位置参数 + 关键字参数---> 位置参数在前，关键字参数在后
# stu = reg_stu("小智 ", 18, gender = "男", city = "马耳他")



# -----------------函数 - 默认参数------------
# 定义参数
# def reg_stu(name, age, gender = "男", city = "真新镇"):
#     print(f"注册成功， 姓名: {name}, 年龄: {age}, 性别: {gender}, 城市: {city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
#
# # 调用参数
# stu = reg_stu("小茂", 17)
# print(stu)
# stu = reg_stu("小璇", 17, gender = "女")
# print(stu)
# stu = reg_stu("小雅", 17, city = "日落之城", gender = "女")
# print(stu)



#------------------函数--不定长参数（位置参数 *args--> 元组-----------------------
# 需求 ：根据传入的这批数据，计算这批数据的最小值、最大值、平均值
# def calc_data(*args):
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#     return min_data, max_data, round(avg_data, 1)
# print(calc_data(2, 5, 6, 9, 77, 58, 98))
#
#
# #-------------------函数--不定长参数 (关键字参数 **kwagrs -->字典）
def calc_data(*args, **kwargs):
    """根据传入的这批数据，计算这批数据的最小值、最大值、平均值

    :param args: 不定长位置参数
    :param kwargs: 不定长关键字参数
        round : 保留小数位个数
        print : 是否打印输出
    :return:最大值，最小值，平均值
    """

    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    if kwargs.get("round") is not None:
        avg_data = round(avg_data, kwargs.get("round"))
    if kwargs.get("print"):
        print(f"最大值为{max_data}, 最小值为{min_data}， 平均值为{avg_data}")


    return min_data, max_data, round(avg_data, 1)
#调用函数
print(calc_data(2, 5, 6, 9, 77, round = 3, print = True))
print(calc_data(6, 5, 99, 88, 77, 55, 66, 44, 33))











