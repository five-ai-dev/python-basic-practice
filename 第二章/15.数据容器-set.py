# 集合-->无序,不可重复,可修改
# 定义
# set = {5, 6, 9, 15, 74, 99, 66}
# print(set)
# print(type(set))
# #定义空集合
# set2 = ()
# print(set2)
# print(type(set2))
# #常见方法
# # add() : 添加元素到集合
# s1 = {100, 200, 300, 400, 500, 600, 700, 800}
# print(s1)
# s1.add(5000)
# print(s1)
#
#
# #remove() : 移除集合中的指定元素(指定元素不存在 报错)
# s1.remove(200)
# print(s1)
#
#
# #pop() : 随机删除集合中的元素并返回
# a = s1.pop()
# print(a)
# print(s1)
#
# # clear() : 清空集合
# s1.clear()
# print(s1)
#
#
#
# s2 = {"A", "B", "C", "D", "E", "F", "G"}
# s3 = {"A","B","X", "Y", "Z"}
# # difference() : 求两个集合的差集(存在第一个集合,但不存在于第二个集合)
# print(s2.difference(s3))
# print(s3.difference(s2))
#
#
# #union() : 求两个集合的并集
# print(s2.union(s3))
#
#
#
# #intersection() : 求两个集合的交集
# print(s2.intersection(s3))



#选修足球学生名单
football_set ={"王林", "曾牛", "徐立国", "适天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set ={"张铁","墨居仁","王林","姜老道", "曾牛","王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set ={"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set ={"适天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}
# 1. 找出同时选修了法语和艺术的学生
# 方法一
fa_set = french_set & art_set
print(fa_set)
# 方法二
fa_set = french_set.intersection(art_set)
print(fa_set)
# 2. 找出同时选修了所有四门课的学生
# 方法一
all_set = football_set & basketball_set & french_set & art_set
print(all_set)
# 方法二
all_set = football_set.intersection(basketball_set) . intersection(french_set) . intersection(art_set)
print(all_set)


# 3. 找出选修了足球,但没有选修篮球的学生
# 方法一
fo_set = football_set.difference(basketball_set)
print(fo_set)
# 方法二
fo_set = set()
for s in football_set:
    if s not in basketball_set:
     fo_set.add(s)
print(fo_set)
# 方法三---> 差集
fo_set = football_set - basketball_set
print(fo_set)
# 4. 统计每一个学生选修的课程数量
all_set = football_set | basketball_set | french_set | art_set
all_list = [*football_set, *basketball_set, *french_set, *art_set]
print(all_set)
print(all_list)
for s in all_set:
  print(f"学生: {s}选修了: {all_list.count(s)}门课程")

