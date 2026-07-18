# 常见数据类型 -->type() 获取指定字面量或者变量的类型
# print("Hello World")
# print(type("Hello World"))
# print(type(100)) # int
# print(type(3.14)) # float
# print(type(True)) # bool
# print(type(False)) # bool
# print(type(None))# NoneType
#
# num=-200
# print(type(num)) # int
# # 常见数据类型 -->isinstance(数据, 类型) -->bool值 -->判断数据是否是指定类型 如果是: True. 否则 : False
# print(isinstance(num, int)) # True
# print(isinstance(num, float)) #False
# print(isinstance(num, bool)) # False

# 字符串
# 定义字符串的三种方式
# s1 = "Hello World" # 双引号定义
# s2 = 'Hello Python' # 单引号定义
# s3 = """
# Hello
#      My name is Zhang Xiang
#      Thank you
#     """ # 三引号定义 (多行字符串)
# print(s1)
# print(s2)
# print(s3)
#
# print(type(s1))
# print(type(s2))
# print(type(s3))
#
# # 定义字符串 ---> It 's very good
# # 转义字符 \' \" \n \t
# msg = 'It \'s very good'
# print(msg)
#
# msg2 = "It 's very good"
# print(msg2)
#
#
# msg3 = "Hello World的意思是\"你好世界\""
# print(msg3)
#
# msg4 = 'Hello World的意思是"你好世界'
# print(msg4)
#
# print("\t Hello \n\t My name is Zhang Xiang Thank you ")
#

# 字符串拼接
# s1 = "无欲无求" "笑口常开"
# print(s1)
#
# msg1 = "无欲无求"
# msg2 = "笑口常开"
# print("元歌说:"+msg1 + "," + msg2)



#  案例 ---> str(int数字)  --->将int 类型数字转为字符串
# name = "张翔"
# age = 21
# pro = "智能科学与技术"
# hobby = "python、java"
# print ("大家好,我是" + name + ",今年" + str(age) + "岁,学习的专业是" + pro + ",爱好是" + hobby )

# 字符串格式化 --> 方式一 : %s 占位符
# name = "张翔"
# age = 21
# pro = "智能科学与技术"
# hobby = "python、java"
# print ("大家好,我是 %s ,今年 %s 岁,学习的专业是 %s ,爱好是 %s " %(name,age,pro,hobby))

# 字符串格式化 --> 方式二 : f"..{变量名/表达式}.."--->推荐
name = "张翔"
age = 21
pro = "智能科学与技术"
hobby = "python、java"
print (f"大家好,我是 {name} ,今年 {age} 岁,学习的专业是 {pro} ,爱好是 {hobby}" )