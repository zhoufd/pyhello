import datetime                                      # 调用日期模块datetime
print('当前年份：'+str(datetime.datetime.now().year))   # 输出当前年份，当年是2018年，输出2018
print('当前日期时间：'+datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))
# #输出当前日期和时间，如：18-11-20 15:30:23,注意代码中的单引号，大小写，不能写错



