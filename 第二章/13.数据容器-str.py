# s = "Hello- World- Hello-Python"
# # find()查找指定字符串第一次出现的索引位置
# index = s.find("l")
# print(index)


#count() 统计子字符串在指定字符中出现的次数
# sc = s.count("o")
# print(sc)
#
# # #upper() 转为大写
# su = s.upper()
# print(su)
#
# # lower() 转为小写
# sl = s.lower()
# print(sl)
# #strip() 去除字符串两端的空格
# ss = s.strip()
# print(ss)
#
# # replace() 将字符串中的指定子串替换出新的内容
# sr = s.replace("-", "_")
# print(sr)
# # startswith() / endswith() 判断字符串是否以指定的字符串开头 是 True, 否则 False
# print(s.startswith("Hello"))
# print(s.endswith("Python"))


# 案例一 邮箱格式验证:用户输入一个邮箱,验证邮箱格式是否正确(包含一个@和至少一个.)如果输入正确,输出"邮箱格式正确",否则输出"邮箱格式错误"
#方式一
# mail = input("请输入邮箱")
# if mail.count("@") ==1 and mail.count(".") >=1:
#     print(f"{mail}邮箱格式正确")
# else:
#     print(f"{mail}邮箱格式错误")

#方式二
# mail = input("请输入邮箱")
# if mail.count("@") ==1 and "." in mail:
#     print(f"{mail}邮箱格式正确")
# else:
#     print(f"{mail}邮箱格式错误")


#practice_1

# a = input("请输入第一个字符串")
# b = input("请输入第二个字符串")
# if a == a[::-1]:
#     print(f"{a}是回文")
# else:
#     print(f"{a}不是回文")
# if b == b[::-1]:
#     print(f"{b}是回文")
# else:
#     print(f"{b}不是回文")
#
# practice_2
str_list = []
for i in range(10):
    str_list1 = input(f"请输入第{i+1}个字符串")
    str_list2 = str_list1 [::-1]
    str_list3 = str_list2.upper()
    str_list.append(str_list3)
for item in str_list:
    print(item)








