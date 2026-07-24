"""
   案例：
   开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询和统计功能。 系统使用嵌套字典结构存储商品数据，通过控制台菜单与用户交互。
   具体功能如下：
       1. 添加购物车： 用户根据提示录入商品名称、以及该商品的价格、数量、保存该商品信息到购物车。
       2. 修改购物车: 要求用户输入要修改的购物车商品名称， 然后再提示输入该商品的价格、数量、输入完成后修改该商品信息。
       3. 删除购物车：要求用户输入要删除的购物车名称， 根据名称删除购物车中的商品。
       4. 查询购物车： 将购物车中的商品信息展示出来， 格式为: " 商品名称： xxx， 商品价格： xxx， 商品数量：xxx”。
       5. 退出购物车
    结构： shopping_cart = {"vivox90": {"price": 4999, "num": 2}, "鼠标“： {...}
"""
from unittest import case

"""
shopping_cart = {}
# 1. 制作菜单
menu = """
##########购物车系统#############
#           1. 添加购物车              #
#           2. 修改购物车              #
#           3. 删除购物车              #
#           4. 查询购物车              #
#           5. 退出购物车              #                  
"""
print("请输入商品名称")
print(menu)
# 2. 执行操作
while True:
    choice = input("请输入选择的操作(1-5)")
    match choice:
        case "1": #添加购物车
            goods_name = input("请输入商品名称")
            goods_price = float(input("请输入商品价格"))
            goods_num = int(input("请输入商品数量"))
            if goods_name in shopping_cart:
                print("商品已存在，请重新选择")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}

                print(f"添加的商品名称为{goods_name},添加完毕")
        case "2": #修改购物车
            goods_name = input("请输入商品名称")
            if goods_name not in shopping_cart:
                print("该商品不存在，请重新选择")
                continue
            goods_price = float(input("请输入商品最新价格"))
            goods_num = int(input("请输入商品最终数量"))
            shopping_cart[goods_name] = {"price" : goods_price, "num" : goods_num}
            print("修改完毕")

        case "3": #删除购物车
            goods_name = input("请输入商品名称")
            if goods_name not in shopping_cart:
                print("该商品不存在，请重新选择")
            else:
                del shopping_cart[goods_name]
                print("商品删除完毕")
        case "4": #查询购物车
            for goods_name in shopping_cart.keys():
                goods_info = shopping_cart[goods_name]
                print(f"商品名称为{goods_name},商品价格为{goods_info["price"]},商品数量为{goods_info["num"]}")


        case "5": #退出购物车
            print("bye~")
            break
        case _:
            print("非法操作，不支持")
"""

"""
开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
1. 添加学生信息 : 根据提示录入学生姓名、语文、数学、英语成绩， 录入完成保存到系统中。
2. 修改学生信息 : 要求输入要修改的学生姓名， 然后再提示输入语文、数学、英语成绩， 输入完成后修改学员信息。
3. 删除学生信息 : 要求输入要删除的学生姓名， 根据姓名删除学生信息。
4. 查询学生信息 : 要求输入要查询的学生姓名， 根据姓名查询学生信息并输出。
5. 列出所有学生 : 遍历所有学生信息并输出。
6. 统计班级成绩 : 统计班级语文、数学、英语成绩的最高分、最低分、平均分， 以及语文、 数学、 英语最高分和最低分的学员姓名。
7. 退出系统。

"""
edu_sys = {}
# 1.构建系统
sys = """
#           1.添加学生信息         #
#           2.修改学生信息         #
#           3.删除学生信息         #
#           4.查询学生信息         #
#           5.列出所有学生         #
#           6.统计班级成绩         #
#           7.退出系统            #             
"""
print("请输入学生姓名")
print(sys)

while True:
    choice = input("请输入选择的操作(1-7)")
    match choice:
        case "1":
            students_name = input("请输入学生名字")
            if students_name in edu_sys:
                print("该学生已存在，请重新选择操作")
                continue
            chinese_scores = int(input("请输入语文成绩"))
            math_scores = int(input("请输入数学成绩"))
            english_scores = int(input("请输入英语成绩"))
            edu_sys[students_name] = {"chinese": chinese_scores, "math": math_scores, "english": english_scores}
            print("学生信息添加完成")

        case "2":
            students_name = input("请输入学生名字")
            if students_name not in edu_sys:
                print("该学生不存在，请重新选择操作")
                continue
            chinese_scores = int(input("请输入语文成绩"))
            math_scores = int(input("请输入数学成绩"))
            english_scores = int(input("请输入英语成绩"))
            edu_sys[students_name] = {"chinese": chinese_scores, "math": math_scores, "english": english_scores}
            print("修改完成")
        case "3":
            students_name = input("请输入学生名字")
            if students_name not in edu_sys:
                print("该学生不存在，请重新输入")
                continue
            del edu_sys[students_name]
            print("删除完毕")

        case "4":
            students_name = input("请输入学生名字")
            if students_name not in edu_sys:
                print("该学生不存在，请重新输入")
                continue
            students_info = edu_sys[students_name]
            print(f"学生姓名为{students_name}，语文成绩为{students_info["chinese"]}, 数学成绩为{students_info["math"]}, 英语成绩为{students_info["english"]}")
        case "5":
            #方法一
            if len(edu_sys) == 0:
           #方法二 if not edu_sys:
                print("系统暂无任何学生数据")
            for students_name in edu_sys.keys():
                students_info = edu_sys[students_name]
                print("""
                    f"学生姓名为{students_name}，
                     语文成绩为{students_info["chinese"]},
                     数学成绩为{students_info["math"]}, 
                     英语成绩为{students_info["english"]}"
                     """)
                input("\n按下回车键,再返回主菜单...")

        case "6":
            if len(edu_sys) == 0:
                print("系统暂无学生，无法统计成绩")
                continue
            chinese_list = []
            math_list = []
            english_list = []
            name_list = []
            for name, score_dict in edu_sys.items():
                name_list.append(name)
                chinese_list.append(score_dict["chinese"])
                math_list.append(score_dict["math"])
                english_list.append(score_dict["english"])
                #语文统计
                max_ch = max(chinese_list)
                min_ch = min(chinese_list)
                avg_ch = sum(chinese_list)/len(chinese_list)
                name_max_ch = name_list[chinese_list.index(max_ch)]
                name_min_ch = name_list[chinese_list.index(min_ch)]
                #数学统计
                max_ma = max(math_list)
                min_ma = min(math_list)
                avg_ma = sum(math_list)/len(math_list)
                name_max_ma = name_list[math_list.index(max_ma)]
                name_min_ma = name_list[math_list.index(min_ma)]
                #英语统计
                max_en = max(english_list)
                min_en = min(english_list)
                avg_en = sum(english_list)/len(english_list)
                name_max_en = name_list[english_list.index(max_en)]
                name_min_en = name_list[english_list.index(min_en)]
            print(f"""
                语文最高分是{max_ch}, 对应的学生为{name_max_ch} 
                语文最低分是{min_ch}, 对应的学生为{name_min_ch} 
                平均分是{avg_ch:.1f}
                数学最高分是{max_ma}, 对应的学生为{name_max_ma}
                数学最低分是{min_ma}, 对应的学生为{name_min_ma} 
                平均分是{avg_ma:.1f}
                英语最高分是{max_en}, 对应的学生为{name_max_en} 
                英语最低分是{min_en}, 对应的学生为{name_min_en} 
                平均分是{avg_en:.1f}
                      """)

        case "7":
            print("bye bye ~")
            break
        case _:
            print("非法操作，不支持")
