print("\n","="*20,"Python经典应用","="*20,"\n")
with open('message.txt','r') as file:   # 打开保存Python经典应用信息的文件
    number = 0   # 记录行号
    while True:
        number += 1
        line = file.readline()
        if line =='':
            break    # 跳出循环
        print(number,line,end= "\n")  # 输出一行内容
print("\n","="*20,"over","="*20,"\n")
































































