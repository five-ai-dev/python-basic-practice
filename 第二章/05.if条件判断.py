# score = 800
# if score > 500:
#     print("欢迎你通过了考试")
#     print("祝你好运")
# print("------------------------")
# ok_account = "1738541211"
# ok_password = "123456"
#
# account = input("请输入您的账号")
# password = input("请输入您的密码")
#
# if account == ok_account and password == ok_password:
#     print("登陆成功")
#     print("进入qq页面")
#
#
# if account != ok_account or password != ok_password:
#     print("登陆失败")
#     print("账号或密码错误")





# year = int(input("请输入年份"))
#
# if (year %100 !=0 and year %4 == 0) or (year % 400 ==0):
#     print(f"输入年份{year}是闰年")
# else:
#     print(f"输入年份{year}为平年")


#####案例一####
# num = int(input("请输入您的数"))
# if num % 2 ==0:
#     print(f"您输入的数字{num}为偶数")
# else:
#     print(f"您输入的数字{num}为奇数")

######案例二#######
# age = int(input("请输入您的年龄"))
# if year >= 18:
#     print(f"您的年龄{age}成年")
# else:
#     print(f"您的年龄{age}未成年")



########案例三########
# num = int(input("请输入数字"))
# if num > 0:
#     print(f"{num}为正数")
# elif num < 0:
#     print(f"{num}为负数")
# else:
#     print(f"{num}是0")




# #####案例四########
# score = int(input("请输入分数"))
# if score >= 60:
#     print("成绩及格")
# else:
#     print("成绩不及格")




# 案例-->根据输入的用户名和密码进行系统登陆-->  zx/123   hym/456 mxy/789
# username = input("请输入用户名")
# password = input("请输入密码")
# if username == "zx" and password == "123":
#     print("登陆成功")
# elif username == "hym" and password == "456":
#     print("登录成功")
# elif username == "mxy" and password == "789":
#     print("登陆成功")
# else:
#     print("登陆失败,用户名或密码错误")


    #案例1#
# score = int(input("请输入分数"))
# if score >= 85:
#     print(f"输入的{score}为优秀")
# elif score >=60 and score < 85:
#     print(f"输入的{score}为及格")
# else:
#     print(f"输入的分数{score}不及格")




"""
amount = float(input("请输入购物车的商品总额:"))
if amount >= 500:
    print(f"您实际应付金额为您的购物车商品总额的{amount * 0.8}")
elif amount >=300 and amount < 500:
    print(f"您实际应付金额为您购物车总额的{amount * 0.9}")
elif amount >=100 and amount < 300:
    print(f"您的应付金额为您购物车总金额的{amount * 0.95}")
elif amount < 100:
    print(f"您的应付金额为您的购物车总额")
"""


"""
a = int(input("请输入第一个边长"))
b = int(input("请输入第二个边长"))
c = int(input("请输入第三个边长"))

if a + b > c and b + c > a and a + c > b:
    if a == b and b == c:
        print(f"{a}{b}{c} 这三个边构成等边三角形")
    elif a ==b or b == c or a == c:
        print(f"{a}{b}{c} 这三个边构成等腰三角形")
    else:
        print(f"{a}{b}{c} 这三个边构成普通三角形")
else:
    print(f"{a}{b}{c} 这三个边不能构成一个三角形")
"""



a = float(input("请输入用户消费的电量"))
if a < 2880:
    print(f"所交电费为{a * 0.4883}")
elif 2880 <= a <= 4800:
    print(f"所交电费为{(a - 2880) * 0.5383 + 2880 * 0.4883}")
elif a > 4800:
    print(f"所交电费为{(a - 4880) * 0.7883 + (4800 - 2880) * 0.5383 + 2880 * 0.4883}")








