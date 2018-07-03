
#方法一：直接修改原来函数

#侵入函数内部，直接修改函数代码
import time
def func(a):
    startTime = time.time()
    print('Hello')
    time.sleep(1)
    print(a)
    endTime = time.time()
    usecs = (endTime - startTime)*1000000
    print('Time is %d us'%usecs)
func('Python')