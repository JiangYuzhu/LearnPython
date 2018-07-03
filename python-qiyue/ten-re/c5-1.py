
#数量词

import re

s = 'python10&C#\rjava C++___ \n php \t98=()~`'

r = re.findall('[a-z]{3,6}',s)
print(r)

s = 'Python10&C#\rJava C++___ \nPHP\t98=()~`'

r = re.findall('[A-Z]{1,3}[a-z]{2,6}',s)  #结果不正确
print(r)


