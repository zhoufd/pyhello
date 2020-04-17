message = '唯有在被追赶的时候，你才能真正地奔跑。'        # 全局变量
print('函数体外：message =',message)                     # 在函数体外输出全局变量的值
def f_demo():
    message = '命运给予我们的不是失望之酒，而是机会之杯。'  # 局部变量
    print('函数体内：message =',message)                 # 在函数体内输出局部变量的值
f_demo()   # 调用函数
print('函数体外：message =',message)                      # 在函数体外输出全局变量的值











































