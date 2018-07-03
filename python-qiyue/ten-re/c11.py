
#re.match
#re.search

import re
s = 'P67PHP23JavaScript85'
r1 = re.match('\d', s)
print(r1)
r2 = re.search('\d', s)
print(r2)

s = '67PHP23JavaScript85'
r1 = re.match('\d', s)
print(r1)
r2 = re.search('\d', s)
print(r2)
print(r2.group())
