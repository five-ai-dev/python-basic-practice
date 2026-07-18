# while True:
#     usename = input("请输入正确的用户名")
#     password = input("请输入正确的密码")
#     if usename == "" or password == "":
#         print("输入的用户名或密码不能为空,请重新输入")
#         continue
#     if usename == "zx" and password == "123":
#         print("登陆成功,进入qq")
#         break
#     elif usename == "hym" and password == "456":
#         print("登陆成功,进入qq")
#         break
#     elif usename == "mxy" and password == "789":
#         print("登陆成功,进入qq")
#         break
#     else:
#         print("登陆失败,用户名或密码错误!")

count = 0
while True:
    if count >= 5:
        print("输错五次,禁止操作,程序退出")
        break
    usename = input("请输入正确的用户名")
    password = input("请输入正确的密码")
    if usename == "" or password == "":
        print("输入的用户名或密码不能为空,请重新输入")
        continue
    if usename == "zx" and password == "123":
            print("登陆成功,进入qq")
            break
    elif usename == "hym" and password == "456":
            print("登陆成功,进入qq")
            break
    elif usename == "mxy" and password == "789":
            print("登陆成功,进入qq")
            break
    else:
        count = count + 1
        print(f"登陆失败,用户名或密码错误!,还剩余{5 - count}次机会")



