
#系统随机产生n个整数（n可以由键盘输入确定），然后由小到大排列输出。

import random
import time

l = []
n = int(input('please input the numbers of interger:'))
print('start random:' + str(time.time()))
for i in range(n):
    x = random.randrange(0,100000000,30)
    l.append(x)
print('stop  random:' + str(time.time()))
print('start sort:' + str(time.time()))
l.sort()
print('stop  sort:' + str(time.time()))
#print(l)


