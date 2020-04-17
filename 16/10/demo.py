# -*- coding:utf-8 -*-
from threading import Thread
import time

def plus():
    print('-------子线程1开始------')
    global g_num
    g_num += 50
    print('g_num is %d'%g_num)
    print('-------子线程1结束------')

def minus():
    time.sleep(1)
    print('-------子线程2开始------')
    global g_num
    g_num -= 50
    print('g_num is %d'%g_num)
    print('-------子线程2结束------')

g_num = 100 # 定义一个全局变量
if __name__ == '__main__':
    print('-------主线程开始------')
    print('g_num is %d'%g_num)
    t1 = Thread(target=plus)   # 实例化线程p1
    t2 = Thread(target=minus)  # 实例化线程p2
    t1.start()                  # 开启线程p1         
    t2.start()                  # 开启线程p2
    t1.join()                   # 等待p1线程结束
    t2.join()                   # 等待p2线程结束
    print('-------主线程结束------')
