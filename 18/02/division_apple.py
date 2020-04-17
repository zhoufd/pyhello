def division():
    num1 = int(input("请输入被除数：")) # 用户输入提示，并记录
    num2 = int(input("请输入除数："))
    result = num1//num2 # 执行除法运算
    print(result)
if __name__ == '__main__':
    try:# 捕获异常
       division()# 调用分苹果的函数
    except ZeroDivisionError:  # 处理异常
       print("输入错误：除数不能为0")# 输出错误原因




