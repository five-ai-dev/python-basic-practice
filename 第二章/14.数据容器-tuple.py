# 元组基本操作 --tuple
# 定义
# t1 = (50, 60, 80, 90, 70, 99, 60, 80)
# print(t1)
# print(type(t1))
#
# print(t1[0])
# print(t1[-1])
#
# print(t1.count(60))
# print(t1.index(80))
#
# t2 = (80)
# print(t2)
# print(type(t2))
# t3 = (80,)
# print(t3)
# print(type(t3))




######## 元组tupe组包与解包######
#组包操作
# t1 = (2, 3, 4, 5, 6, 7, 8)
# t2 = 2, 3, 4, 5, 6, 7, 8
# print(t1)
# print(t2)
#
# a, b, c, d, e, f, g = t1
# print(a, b, c, d, e, f, g)
#
# first,second,*other,last = t1
# print(first, second)
# print(*other)
# print(last)


# ##案例1##
# a = 10
# b = 20
# b,a = a,b
# print(a)
# print(b)
#
# ###案例二###
# a = 100
# b = 200
# c = 300
# b, c, a = a, b, c
# print(a)
# print(b)
# print(c)


"""
  根据如下提供的学生成绩单,完成如下需求:
  1. 计算每个学生的总分,各科平均分,然后一并输出-->{avg:.1f}-->保留一位小数
  2. 统计各科成绩的最低分、最高分、平均分,并输出
  3. 查找成绩优秀(平均分大于90)的学生,并输出
"""
#1.
students = (
    ("01", "卡比兽", 85, 94, 86),
    ("02", "皮卡丘", 96, 87, 78),
    ("03","小智", 89, 91, 96),
    ("04", "莉莉艾", 98, 97, 95),
    ("05", "喷火龙", 81, 83, 84),
    ("06", "裂空座", 83, 86, 77)
)
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    print(f"{s[0]}\t\t{s[1]}\t\t{s[2]}\t\t{s[3]}\t\t{s[4]}\t\t{total}\t\t{avg:.1f}")
#2.统计各科成绩的最低分、最高分、平均分,并输出
chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]
print(f"语文最低分为{min(chinese_scores)},最高分为{max(chinese_scores)},平均分为{sum(chinese_scores)/len(chinese_scores):.1f}")
print(f"数学最低分为{min(math_scores)},最高分为{max(math_scores)},平均分为{sum(math_scores)/len(math_scores):.1f}")
print(f"英语最低分为{min(english_scores)},最高分为{max(english_scores)},平均分为{sum(english_scores)/len(english_scores):.1f}")
#3. 查找成绩优秀(平均分大于90)的学生,并输出
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    if avg > 90:
       print(f"成绩优秀的学生学号是{s[0]},姓名是{s[1]}")