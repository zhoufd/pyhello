# -*- coding:utf-8 -*-
from multiprocessing import Process

def plus():
    print('-------子进程1开始------')
    global g_num
    g_num += 50
    print('g_num is %d'%g_num)
    print('-------子进程1结束------')

def minus():
    print('-------子进程2开始------')
    global g_num
    g_num -= 50
    print('g_num is %d'%g_num)
    print('-------子进程2结束------')

g_num = 100 # 定义一个全局变量
if __name__ == '__main__':
    print('-------主进程开始------')
    print('g_num is %d'%g_num)
    p1 = Process(target=plus)   # 实例化进程p1
    p2 = Process(target=minus)  # 实例化进程p2
    p1.start()                  # 开启进程p1
    p2.start()                  # 开启进程p2
    p1.join()                   # 等待p1进程结束
    p2.join()                   # 等待p2进程结束
    print('-------主进程结束------')
