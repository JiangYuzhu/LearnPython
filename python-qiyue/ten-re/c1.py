
#正则表达式,是一个特殊的字符序列，帮助我们一个字符串是否与我们所设定的字符序列相匹配，实现
#快速检索文本、替换文本的操作。
##正则表达式的灵魂在于“规则”！
#JSON

a = 'C#|C++|Python|Javascript|PHP'
#字符串a是否包含Python?
print(a.index('Python')>-1)
print('Python' in a)
#字符串函数可以解决部分问题，优先使用这些函数。

import re #模块re
#re.findall('正则表达式',a) #re提供了多种方法(函数)，常用的是findall
r = re.findall('Python',a)
if  len(r) > 0:
    print('字符串中包含：'+ str(r)) #如何将列表转换为字符串
    print('字符串中包含：',r)
else:
    print('字符串中不包含:'+str(r))


