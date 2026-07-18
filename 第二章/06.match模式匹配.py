## match  case 模式匹配
"""
day = input("请输入星期几(1-7):")
match day:
    case "1":
        print("星期一: 工作会议日")
    case "2":
        print("星期二: 学习培训日")
    case "3":
        print("星期三: 项目开发日")
    case "4":
        print("星期四: 代码审查日")
    case "5":
        print("星期五: 总结规划日")
    case "6" | "7":
        print("周末: 休息放松日")
    case _:
        print("输入错误")
"""
"""
## 基于 match case 实现一个简易计算器 用户可以输入 + - * / 进行两个数的运算
num1 = float(input("请输入第一个数"))
num2 = float(input("请输入第二个数"))
oper = input("请输入运算符(+ - * /")
match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/" if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("操作不支持!!!")
"""


# 编写游戏角色移动控制系统,根据玩家输入的指令,控制游戏角色完成相应的动作
a = input("请输入指令(上 w  W 下 s S 左 a A 右 d D 跳 ""   攻击 j J 退出 ESC esc)")
match a:
    case "w" | "上" | "W":
        print("角色向上移动")
    case "s" | "下" | "S":
        print("角色向下移动")
    case "a" | "左" | "A":
        print("角色向左移动")
    case "d" | "右" | "D":
        print("角色向右移动")
    case "跳" | " ":
        print("角色跳跃")
    case "j" | "攻击" | "J":
        print("角色发动攻击")
    case "esc" | "退出" | "ESC":
        print("角色退出游戏")
    case _:
        print("操作无效!!!")










