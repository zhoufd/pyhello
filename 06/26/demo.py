number = (i for i in range(4))     # 生成生成器对象
for i in number:                    # 遍历生成器对象
    print(i,end=" ")                # 输出每个元素的值
print(tuple(number))                # 转换为元组输出









































