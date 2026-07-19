#系统随机生成一个随机数
#用户根据提示猜数字,并将所猜数字输入系统
#如果猜错,系统给出提示是猜大了,还是猜小了,然后继续输入猜的数字
#如果猜对,系统自动退出,游戏介绍
# import random
# random_num = random.randint(1,100)
# while True:
#     num = int(input("请输入一个数字"))
#     if num > random_num:
#         print(f"输入的数字太大了!")
#     elif num < random_num:
#         print(f"输入的数字太小了!")
#     else:
#         print("恭喜你,猜对了,真厉害!!!")
#         break
# print(f"随机生成的数字是{random_num}")



#practice
# total = 0
# for i in range(1,1001):
#     if i % 5 == 0:
#         total += i
# print(f"1-1000之间所有的5的倍数的数字累加起来是{total}")




#practice
msg = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
count_a = 0
count_k = 0
for char in msg:
    if char == "a":
        count_a += 1
    elif char == "k":
        count_k += 1
print(f"字母a共有{count_a}个")
print(f"字母k共有{count_k}个")


