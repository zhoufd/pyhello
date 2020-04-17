str1 = '明 日 学 院 官 网  >>>  www.mingrisoft.com'
print('原字符串：',str1)
list1 = str1.split()             # 采用默认分隔符进行分割
list2 = str1.split('>>>')        # 采用多个字符进行分割
list3 = str1.split('.')          # 采用.号进行分割
list4 = str1.split(' ',4)        # 采用空格进行分割，并且只分割前4个
print(str(list1) + '\n' + str(list2) + '\n' + str(list3) + '\n' + str(list4))
list5 = str1.split('>')             # 采用>进行分割
print(list5)

















































