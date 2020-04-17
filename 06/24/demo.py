import random                                  #导入random标准库
randomnumber = (random.randint(10,100) for i in range(10))
randomnumber = tuple(randomnumber)           # 转换为元组
print("转换后：",randomnumber)








































