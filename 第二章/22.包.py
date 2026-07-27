# 1. 导入模块
# import utils.my_fun
# utils.my_fun.log_separator1()
#
# from utils import my_fun
# my_fun.log_separator2()

#注意：如果要通过 from utils import * 导入包下的所有模块，需要__init__.py文件中添加__all__ = []，填模块文件名
from utils import *
my_fun.log_separator3()
print(my_var.NAME)


# 2. 导入模块中的功能
# 相对路径:从当前文件所在目录开始查找
from utils.my_fun import log_separator3,log_separator2
# 绝对路径：从项目的根目录开始查找
from 第二章.utils.my_fun import log_separator3,log_separator2
log_separator3()
log_separator2()