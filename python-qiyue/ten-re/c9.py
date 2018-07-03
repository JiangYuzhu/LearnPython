
# re.sub

import re
language = 'PythonC#PHPC#JavaScriptC#'
r = re.sub('C#','GO',language)
print(r)
r = re.sub('C#','GO',language,count=1)
print(r)

#字符串替换函数
language.replace('C#','GO')
print(language)   #language字符串为什么没有被替换？
language = language.replace('C#','GO')
print(language)


