
#方法二：定义一个新函数，调用原来函数，新函数里编写新增功能代码。
#正确
import time
def func(a):
    print('hello')
    time.sleep(1)
    print(a)
def deco(f,x): 
    startTime = time.time()
    f(x)   
    endTime = time.time()
    usecs = (endTime - startTime)*1000000
    print('Time is %d us'%usecs)

deco(func,'Python')
deco(func,"World") 
