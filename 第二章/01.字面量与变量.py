#字面量的写法
# print(200) #整数(int)
# print(3.14) #小数(float)
# print(True) #布尔(bool)
# print(False) #布尔(bool)
# print("Hello Python") #字符串(str)
# print("--------------") #字符串(STR)
# print(None) #空值(None Type)
#
# print(True + 1) #2
# print(False -1) #-1

# 变量
# num = 1114.1
# print(num)
# num = num + 1
# print(num)
# num = "ok"
# print(num)

# 案例
# base = 20.7 #基础播放量
# incr = 50 #每个月新增播放量
# print("未来第一个月的播放总量:", base + incr)
# print("未来第二个月的播放总量:", base + incr + incr)

# 案例 - 升级 : 一次性定义多个变量
# base,incr = 20.7,50
# print("未来第一个月的播放总量:", base + incr)
# print("未来第二个月的播放总量:", base + incr + incr)

a = 100
b = 200
c = 300

d = a # d = 100
e = b # e = 200
a = e # a = 200
b = c # b = 300
c = d # c = 100
print(a,b,c)

