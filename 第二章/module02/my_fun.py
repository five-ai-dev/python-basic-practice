# __all__指定 from... import *导入哪些功能
__all__ = ["log_separator1", "log_separator3",  "PI"]
# c=常量（数据不会改变，常量的名称为全部大写）
PI = 3.141596
NAME = "智科⨳张翔"

def log_separator1():
    print("- " *30) # "- " ，重复输出30次

def log_separator2():
    print("+ " *30)

def log_separator3():
    print("# " *30)

def lpg_separator4():
    print("* " *30)

# 测试函数
# __name__,python中的内置变量，直接运行时，__name__的值为"__main__",如果作为模块被导入时，__name__的值就是模块名字
# 执行当前文件，则会执行当前代码：如果被当作模块被导入，则不会执行当前代码
if __name__ == "__main__":
    log_separator1()
