char = ['cat','Tom','Angela','pet']
char.sort()                   # 默认区分字母大小写
print("区分字母大小写：",char)
char.sort(key=str.lower)     # 不区分字母大小写
print("不区分字母大小写：",char)






























