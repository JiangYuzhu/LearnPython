
####
#把一个函数作为另一个函数的参数
###

import re
language = 'PythonC#PHPC#JavaScriptC#'

def convert(value):
    print(value)
    #value不是简单的字符串，而是对象
    # return '!!' + value + '!!'

r = re.sub('C#',convert,language) 
print(r)