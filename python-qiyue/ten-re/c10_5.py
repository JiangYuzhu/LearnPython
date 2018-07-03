
####
#把一个函数作为另一个函数的参数
###

import re
s = 'Python67PHP23JavaScript85'

def convert(value):
    matched = value.group() #group方法拿到具体的数字
    if int(matched) >= 6:
        return '9'
    else:
        return '0'

r = re.sub('\d',convert,s) 
print(r)
