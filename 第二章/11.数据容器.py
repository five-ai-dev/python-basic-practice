#定义列表
# s = ["A", "B", "C", "D", "E", "F", "G", "H"]
# print(s)
# print(type(s))
# print(s[0:5:1])
# print(s[0:5:2])
# print(s[0:-1:1])

# 列表定义
# s = [90, 50, 30, 95, 90, 55, 80, 60]
# print(s)
#
# s.append(40)
# print(s)
#
# s.insert(2, 99)
# print(s)
#
# s.remove(90)
# print(s)
#
# s.pop()
# print(s)
#
# s.pop(1)
# print(s)
#
# s.reverse()
# print(s)
#
# s.sort()
# print(s)
#
# a = s.pop(1)
# print(a)
#
# a = s.pop()
# print(a)






###--列表 list 案例--###
# 案例一.将用户输入的10个数字,存储到一个列表中,并将列表中的数字进行排序,输出其最小值,最大值,平均值

# 1.定义列表
# num_list = []
#
# #2.将用户输入的10个数字存入列表
# for i in range(10):
#     num = int(input("请输入一个有效数字"))
#     num_list.append(num)
# print("数字列表", num_list)
#
# #3.排序
# num_list.sort()
# print("排序后的列表", num_list)
#
# #4.输出其最小值,最大值,平均值.
# print(f"最小值为{num_list[0]}")
# print(f"最大值为{num_list[9]}")
# print(f"平均值为{(sum(num_list)/len(num_list))}")



# 案例二(方法一) 合并两个列表中元素,并对合并的结果进行去重处理(去除列表重复元素)
# num_list1 = [10, 15, 20, 25, 30, 35, 40, 45, 50]
# num_list2 = [20, 30, 40, 50, 60, 70, 80, 90, 100]
# #合并列表
# num_list = num_list1 + num_list2
# #    方法二  num_list = [*num_list1, *num_list2]
# #    方法三  for num in num_list2:
#    # num_list.append(num)
# print("合并后的原始列表为:", num_list)
# #去重处理
# new_list = []
# for num in num_list:
#     if num not in new_list:#判断元素是否在列表,在True,不在False
#         new_list.append(num)
# print("去重后的列表:", new_list)


#案例三 生成1-20的平方列表
#方式一
# num_list = []
# for i in range(1,21):
#     num_list.append(i ** 2)
# print(f"1-20的平方列表为{num_list}")

#方式二
# num_list = [i ** 2 for i in range(1, 21)]
# print(f"1-20的平方列表为{num_list}")





#案例四 从一个数字列表中提取所有偶数,并计算其平方,组成一个新的列表
# num_list = [55, 46, 35, 66, 85, 98, 75, 15, 25, 12, ]
# new_list = [i ** 2 for i in num_list  if i % 2 == 0]
# print(f"新列表为{new_list}")



