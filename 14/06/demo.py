import os
path = "C:\\demo"              # 指定要创建的目录
if not os.path.exists(path):  # 判断目录是否存在
    os.makedirs(path)           # 创建目录
    print("目录创建成功！")
else:
    print("该目录已经存在！")














































































