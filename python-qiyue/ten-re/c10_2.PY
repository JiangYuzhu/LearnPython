####
#把一个函数作为另一个函数的参数
###

import re
language = 'PythonC#PHPC#JavaScriptC#'

def convert(value):
    return '!!' + value + '!!'

r = re.sub('C#',convert,language,1) 
print(r)
