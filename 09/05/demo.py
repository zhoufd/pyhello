password = 0
i = 1
while i < 7:
    num = input("请输入一位数字密码！")
    num =int(num)
    if  num == password  :
        print("密码正确，正进入系统！"  )
        i =7
    else:
        print("密码错误，已经输错" , i ,"次")
    i+=1
if i== 7:
    print("密码错误6次，请与发卡行联系！！")








