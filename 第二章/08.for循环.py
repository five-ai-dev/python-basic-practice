# for循环,遍历输入的字符串
# a = input("请输入需要遍历的字符串")
# for s in a:
#     print(f"元素: {s}")
# else:
#     print("遍历结束")


# 用for循环 计算1-100的之间的奇数之和
# total = 0
# for i in range(1,101,2):
#     total += i
# print("1-100之间的奇数累加之和:", total)
#
#
#
#
# total = 0
# for i in range(100,501):
#     if i % 3 == 0:
#         total += i
# print(f"100-500之间所有3的倍数的数字之和: {total}")
#
#
# m = int(input("请输入长方形的长度"))
# n = int(input("请输入长方形的宽度"))
#
#
# for j in range(n):
#       for i in range(m):
#          print("*", end = " ")
#
#       print()






# 嵌套循环案例 打印99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{i} * {j} = {i * j}", end = "\t")
#     print()




# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end = "  ")
#
#     print()


# for i in range(1,7):
#     for j in range(1,i+1):
#         print(f"{j}", end="\t")
#     print()


for i in range(1,9):
    for j in range(1,9):
        if (i + j) % 2 != 0:
            print("□", end="  ")
        else:
            print("■", end="  ")

    print()





