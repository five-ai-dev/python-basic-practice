# i = 0
# while i < 10:
#     print("船到桥头自然直")
#     i = i + 1
# else:
#     print("循环结束")



# 计算1-100所有偶数的和
total = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1
print(f"1-100之间的偶数和为: {total}")