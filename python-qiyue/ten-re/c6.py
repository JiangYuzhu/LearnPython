
# 边界匹配符(完整地匹配字符串)
# ^ 开始
# $ 末尾  

import re
qq = '1000001' #7位
r = re.findall('\d{4,8}',qq)   #易犯错误：{4,8}写成{4-8}、[4,8]、[4-8]
print(r)
r = re.findall('^\d{4,8}$',qq) #开始到结束至少4个数字最多8个数字
print(r)

qq = '101'
r = re.findall('\d{4,8}',qq)
print(r)
r = re.findall('^\d{4,8}$',qq)
print(r)

qq = '100000001'  #9位
r = re.findall('\d{4,8}',qq)
print(r)
r = re.findall('^\d{4,8}$',qq)
print(r)

r = re.findall('000',qq)
print(r)
r = re.findall('^000',qq)
print(r)
r = re.findall('000$',qq)
print(r)