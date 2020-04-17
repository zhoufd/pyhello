str1 = ' http://www.mingrisoft.com  \t\n\r'
print('原字符串str1：' + str1 + '。')
print('字符串：' + str1.strip() + '。')       # 去除字符串首尾的空格和特殊字符
str2 = '@明日科技.@.'
print('原字符串str2：' + str2 + '。')
print('字符串：' + str2.strip('@.') + '。')  # 去除字符串首尾的@或者.



print('字符串：' + str2.strip('技@.') + '。')  # 去除字符串首尾的@或者.




















































