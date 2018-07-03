
#概括字符集
# (元字符只能匹配单个字符)

# \d 数字字符 [0-9] \D [^0-9]
# \w 单词字符 [A-Za-z0-9_]  \W [^A-Za-z0-9]
# \s 空白字符 \S 非空白字符
# .  除换行符之外其他所有字符

import re

s = 'Python10&C#\r C++___ \n\t98=()~`'

r = re.findall('\d',s)
print('仅数字字符:',r)
r = re.findall('\D',s)
print('非数字字符：',r)

r = re.findall('\w',s)
print('仅单词字符：',r)
r = re.findall('[A-Z0-9a-z_]',s)
print('仅单词字符：',r)
r = re.findall('\W',s)    #概括字符集（元字符）表示
print('非单词字符：',r)
r = re.findall('[^A-Za-z0-9_]',s)  #普通字符集表示
print('非单词字符：',r)

r = re.findall('\s',s)
print('空白字符：',r)
