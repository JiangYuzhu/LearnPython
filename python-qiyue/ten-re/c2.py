
import re 

a = 'C#0C++7Python9Javascript5PHP'
#把字符串中所有的数字提取出来
r = re.findall('[0-9]',a)
print(r)

# for i in a:    #如何用for循环来提取   
#     if i in [0-9]:
#         print(str(i))
       
    