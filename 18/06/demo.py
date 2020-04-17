def division():
    num1 = int(input("请输入被除数：")) # 用户输入提示，并记录
    num2 = int(input("请输入除数："))
    assert num2 != 0, "除数不能为0"  # 应用断言调试
    result = num1//num2 # 执行除法运算
    print(result)
if __name__ == '__main__':
        division()  # 调用函数








