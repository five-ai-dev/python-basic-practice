# 字典-->key不能重复,如果重复,后面的值会覆盖前面的值.-->key必须德是不可变类型(int, float, tuple, str),不能是(list, set, dict)类型
# 定义字典
# dict1 = {"柯南":580, "小兰":640, "琴酒":660, "基德":690}
# print(dict1)
# print(type(dict1))
#
# dict2 = {2:580, (2,3):640, 1.5:660, "K":690}
# print(dict2)
# # 访问
# print(dict1["小兰"])
# dict1["小兰"] = 666
# print(dict1)


########### 字典常用操作 ##########
dict1 = {"柯南":580, "小兰":640, "琴酒":660, "基德":690}
print(dict1)

# 添加 key不存在就是添加
dict1 ["灰原"] = 600
print(dict1)

# 修改 key存在就是修改
dict1 ["基德"] = 800
print(dict1)
# 查询
print(dict1["灰原"]) #根据key 获取 value
print(dict1.get("灰原")) #根据key 获取 value

print(dict1.keys())
print(dict1.values())
print(dict1.items())
# 删除
score = dict1.pop("琴酒")
print(score)
print(dict1)

del dict1["柯南"]
print(dict1)
# 遍历
for k in dict1.keys():
    print(f"{k} : {dict1[k]}")

for item in dict1.items():
    print(f"{item[0]} : {item[1]}")

for k,v in dict1.items():
    print(f"{k} : {v}")