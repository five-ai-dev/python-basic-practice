# 函数定义
#def out_line():
 #   print(-------------)
# 函数调用
# out_line

# 函数的参数与返回值
# 1. 计算圆的面积
def circle_area(r):
    """
    根据圆的半径，求圆的面积
    :param r: 半径
    :return: 圆的面积
    """
    area = 3.14 * r * r
    return area
area = round(circle_area(6), 1)
print(area)

# 2. 计算长方形的面积
def rectangle_area(l, w):
    """
    根据长方形的长和宽，求长方形的面积
    :param l: 长度
    :param w: 宽度
    :return: 长方形的面积
    """
    area = l * w
    return l * w
area = round(rectangle_area(4, 5))
print(area)
# 3. 计算圆的面积，周长 -- 半径
def circle_area_len(r):
    """
    根据圆的半径，求圆的面积和周长
    :param r: 半径
    :return: 圆的面积，圆的周长
    """
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)
al = circle_area_len(8)
print(al)
print(type(al))

area, len = circle_area_len(8)#解包
print(area)
print(len)