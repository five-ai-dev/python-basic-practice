# 函数类型注解
def circle_area_len(r : float ) -> touple[float, float]:
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)
al = circle_area_len(10)
print(al)




def calc_order_cost(*args : touple[str, float, int], coupon : int = 0, score : int = 0, express : float = 0.0) -> touple[float]:
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠(优惠券、积分抵扣）、运费信息计算订单的总金额
    :param args:商品信息（商品名、价格、数量) --->如：("耳机", 288, 3) ("鼠标", 177, 2)
    :param coupon:优惠券
    :param score:积分抵扣
    :param express:运费信息
    :return:订单总金额
    """
    # 订单总金额 = 商品总金额 - 优惠券 - 积分抵扣 + 运费
    # 1. 计算商品总金额
    calc_cost = [goods[1] * goods[2] for goods in args]  # arg是一个大元组，goods是每个商品信息，小元组
    calc_total = sum(calc_cost)

    # 2. 扣减优惠券
    if calc_total >= 5000 and coupon <= calc_total:
        calc_total -= coupon

    # 3. 扣减积分抵扣
    if calc_total >= 5000 and score // 100 <= calc_total:
        calc_total -= score // 100

    # 4. 添加运费
    calc_total += express
    return calc_total

#测试
result = calc_order_cost(("耳机", 288, 3), ("鼠标", 177, 2), coupon=20, score=5000, express=9.9)
print(result)
result = calc_order_cost(("手机", 8999, 2),("鼠标", 177, 2),  coupon=20, score=5000, express=9.9)
print(result)