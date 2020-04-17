#coding=utf-8
from multiprocessing import Queue

if __name__ == '__main__':
    q=Queue(3) # 初始化一个Queue对象，最多可接收三条put消息
    q.put("消息1")
    q.put("消息2")
    print(q.full())  # 返回False
    q.put("消息3")
    print(q.full()) # 返回True

    # 因为消息列队已满，下面的try都会抛出异常，
    # 第一个try会等待2秒后再抛出异常，第二个try会立刻抛出异常
    try:
        q.put("消息4",True,2)
    except:
        print("消息列队已满，现有消息数量:%s"%q.qsize())

    try:
        q.put_nowait("消息4")
    except:
        print("消息列队已满，现有消息数量:%s"%q.qsize())

    # 读取消息时，先判断消息列队是否为空，再读取
    if not q.empty():
        print('----从队列中获取消息---')
        for i in range(q.qsize()):
            print(q.get_nowait())
    # 先判断消息列队是否已满，再写入
    if not q.full():
        q.put_nowait("消息4")

