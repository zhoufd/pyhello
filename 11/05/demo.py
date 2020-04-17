def printsign(**sign):                              # 定义输出姓名和绰号的函数
    print()                                          # 输出一个空行
    for key, value in sign.items():                # 遍历字典
        print("[" + key + "] 的绰号是：" + value)  # 输出组合后的信息

printsign(邓肯='石佛', 罗宾逊='海军上将')
printsign(吉诺比利='妖刀', 帕克='跑车', 鲍文='鲍三叔')








































