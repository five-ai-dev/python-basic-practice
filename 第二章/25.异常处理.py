#异常处理
# try:
#     print("============================")
#     # print(my_name)
#     print(1/0)
#     print("============================")
# except NameError as e:
#     print(f"程序运行出错，请联系管理人员，异常信息是{e}")


# try:
#     print("============================")
#     # print(my_name)
#     # print(1/0)
#     # print("ABC"[5])
#     print("ABC".Hello)
#     print("============================")
# except NameError as e:
#     print(f"名字不存在，请检查变量名，异常信息是{e}")
# except ZeroDivisionError as e:
#     print(f"0不能做被除数，异常信息是{e}")
# except IndexError as e:
#     print(f"索引错误，异常信息是{e}")
# except Exception as e:#捕获所有异常
#     print(f"程序运行出错，请联系管理人员~，错误信息:{e}")
# finally:
#     print("资源释放")

# 异常的传递
def fun1():
    print("fun1 ... running...")
    fun2()
def fun2():
    print("fun2 ... running...")
    fun3()
def fun3():
    print("fun3 ... running...")
    print(my_color)
if __name__ == "__main__":
    try:
        fun1()
    except Exception as e:
        print(f"程序出错了，请联系管理人员，错误信息是{e}")
