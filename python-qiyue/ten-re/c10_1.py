
####
#把一个函数作为另一个函数的参数
###

import re
language = 'PythonC#PHPC#JavaScriptC#'

def convert(value):
    pass

r = re.sub('C#',convert,language,1) 
#执行过程：sub匹配到C#后，将C#作为value的实参传递给convert函数，convert函数返回None给sub
#sub用None替换C
print(r)
