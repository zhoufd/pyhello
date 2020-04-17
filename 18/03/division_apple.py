def division():
    num1 = int(input("请输入被除数：")) # 用户输入提示，并记录
    num2 = int(input("请输入除数："))
    result = num1//num2 # 执行除法运算
    print(result)
if __name__ == '__main__':
    try:  # 捕获异常
        division()  # 调用函数
    except ZeroDivisionError:  # 处理异常
        print("\n出错了：除数不能为0！")
    except ValueError as e:  # 处理ValueError异常
        print("输入错误：", e)  # 输出错误原因
    else:  # 没有抛出异常时执行
        print("程序执行完成……")





