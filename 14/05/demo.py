print("\n","="*20,"Python经典应用","="*20,"\n")
with open('message.txt','r') as file:         # 打开保存Python经典应用信息的文件
    messageall = file.readlines()              # 读取全部信息
    for message in messageall:
        print(message)                          # 输出一条信息
print("\n","="*25,"over","="*25,"\n")


































































