
#组

import re

a = 'PythonPythonPythonPython'
#字符串a里是否包含3个Python子串
r = re.findall('PythonPythonPython',a)
print(r)
r = re.findall('(Python){3}',a)  #()，构成组，各个字符间是且的关系；[]，是或的关系
print(r)
#结果为什么不正确！？