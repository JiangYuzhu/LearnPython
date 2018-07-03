
#字符集

import re

s = 'abc,acc,aec,afc,adc'

r = re.findall('a[cf]c',s) ###[cf] c或f###
print(r)
r = re.findall('a[c-f]c',s)
print(r)
r = re.findall('a[^bef]c',s)
print(r)
