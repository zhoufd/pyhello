number = (i for i in range(3))
print(number.__next__())      # 输出第1个元素
print(number.__next__())      # 输出第2个元素
print(number.__next__())      # 输出第3个元素
number = tuple(number)  # 转换为元组
print("转换后：",number)









































