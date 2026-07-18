# print(f"10+4 = {10+4}")
# print(f"10-4 = {10-4}")
# print(f"10*4 = {10*4}")
# print(f"10/4 = {10/4}")
# print(f"10//4 = {10//4}")
# print(f"10%4 = {10%4}")

# 输入x,y两个数,计算x+y,x-y
# x = float(input("请输入x的值"))
# y = float(input("请输入y的值"))
#
# print(f"x+y = {x+y}")
# print(f"x-y = {x-y}")

################# 赋值运算符 : = += -= /= *+ %= //= **= ###############
# num = 50
# num += 10 # num = num + 10
# print(f"num += 10后,num = {num}") #60
#
# num -= 10 # num = num - 10
# print(f"num-=10后,num = {num}")# num=50
#
# num *= 10 # num = num * 10
# print(f"num *= 10 = {num}")# num = 500
#
# num /= 10 # num = num / 10
# print(f"num /= 10 = {num}")# num = 50.0
#
# num %= 10 # num = num % 10
# print(f"num %= 10 = {num}")# num = 0.0
#
# num **= 10 # num = num ** 10
# print(f"num **= 10 = {num}")# num = 0
#
# num //= 10 # num = num // 10
# print(f"num //= 10 = {num}")# num = 0


################ 比较运算符 == !+ > >+ < <+ #############
# print(f"100 == 100吗 , {100 == 100}")
# print(f" 100 != 100吗 , {100 != 100}")
# print(f" '100' == '100' 吗 , {'100' == '100'}) ")
# print(f" 100 > 100吗 , {100 > 100} ")
# print(f" 100 >= 100吗 , {100 >= 100} ")
# print(f" 100< 100吗, {100 < 100} ")
# print(f" 100 <= 100吗 , {100<= 100}")


# n = int(input("请输入一个整数:"))
# print(f"{n}在10-20之间:", n>=10 and n <= 20)

n = int(input("请输入一个整数:"))
print(f"{n}不在10-20之间吗: {n<10 or n > 20}")
