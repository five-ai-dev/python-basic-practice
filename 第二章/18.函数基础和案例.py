# 函数定义
# def out_line():
#   print(-------------)
# 函数调用
# out_line

# 函数的参数与返回值
# 1. 计算圆的面积
# def circle_area(r):
#     """
#     根据圆的半径，求圆的面积
#     :param r: 半径
#     :return: 圆的面积
#     """
#     area = 3.14 * r * r
#     return area
# area = round(circle_area(6), 1)
# print(area)
#
# # 2. 计算长方形的面积
# def rectangle_area(l, w):
#     """
#     根据长方形的长和宽，求长方形的面积
#     :param l: 长度
#     :param w: 宽度
#     :return: 长方形的面积
#     """
#     area = l * w
#     return l * w
# area = round(rectangle_area(4, 5))
# print(area)
# # 3. 计算圆的面积，周长 -- 半径
# def circle_area_len(r):
#     """
#     根据圆的半径，求圆的面积和周长
#     :param r: 半径
#     :return: 圆的面积，圆的周长
#     """
#     return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)
# al = circle_area_len(8)
# print(al)
# print(type(al))
#
# area, len = circle_area_len(8)#解包
# print(area)
# print(len)


# 1. 定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积 = 底 * 高 / 2）
# def triangle_area(b, h):
#     """
#     根据底和高计算三角形面积
#     :param b: 底
#     :param h: 高
#     :return: 三角形的面积
#     """
#     return b * h / 2
# trinangle_area = triangle_area(2, 3)
# print(trinangle_area)
#
#
#
#
#
# # 2. 定义一个函数：计算传入的字符串中元音字母的个数(元音字母为 aeiouAEIOU)
# def calc_count(s):
#     """
#     计算传入的字符串中元音字母个数
#     :param s: 字符串
#     :return: 元音字母个数
#     """
#     num = 0
#     for i in s:
#         if i in "aeiouAEIOU":
#             num += 1
#     return num
# print(calc_count("Hello World, Hello Python,OK"))
#
#
#
#
# # 3. 定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高法，最低分，平均分（保留一位小数）
# def calc_score(score_list):
#     max_s = max(score_list)
#     min_s = min(score_list)
#     avg_s = sum(score_list) / len(score_list)
#     return max_s, min_s, avg_s
# s_list = [666, 555, 488, 688, 632, 655]
# max_s, min_s, avg_s = calc_score(s_list)
#
# print(f"最大值为{max_s}, 最小值为{min_s}, 平均值为{avg_s}")


# 1. 定义一个函数， 根据传入的分数， 计算对应的分数等级并返回。
# 分数 >= 90: A
# 分数 >= 75: B
# 分数 >= 60: C
# 分数 < 60: D
def score(s):
    """
    根据传入的分数，计算对应的分数等级并返回
    :param s: 分数
    :return: 对应等级
    """
    if s >= 90:
        s = "A"
    elif s >= 75:
        s = "B"
    elif s >= 60:
        s = "C"
    elif s < 60:
        s = "D"
    return s


s_list = [91, 65, 85, 76, 93, 66]
for num in s_list:
    result = score(num)
    print(result)


# 2. 定义一个函数， 用于判断一个字符串是否是回文串， 返回bool值。
# 把字符串反转，如果和原字符串相同， 就是回文串， （如："level", "radar", "黄山落叶松叶落山黄”）
def jud(x):
    """
    判断一个字符串是否是回文串
    :param x: 字符串
    :return: bool值
    """
    if x == x[::-1]:
        return True
    else:
        return False


s_str = "level", "radar"
for s in s_str:
    print(jud(s))


# 3. 定义一个函数 : 完成时间转换功能， 将传入的秒转换为小时、分钟、秒。
def time(s):
    """
    将秒转化为小时，分钟，秒
    :param s:
    :return:
    """
    n = s // 3600
    x = s % 3600
    t = x // 60
    s = x % 60
    return n, t, s


qaq = time(3600)
print(qaq)


# 4. 定义一个函数 : 根据传入的三角形三个边的边长， 判定三角形的类型 （等边、等腰、普通， 或者不能构成三角形）。
def triangle_long(a, b, c):
    s_str = "等边三角形", "等腰三角形", "普通三角形", "不构成三角形"
    if a + b > c and b + c > a and c + a > b:
        if a == b and b == c:
            return "等边三角形"
        elif a == b or a == c or b == c:
            return "等腰三角形"
        elif a != b and b != c:
            return "普通三角形"
    else:
        return "不构成三角形"


tri_long = triangle_long(a=2, b=3, c=3)
print(tri_long)
