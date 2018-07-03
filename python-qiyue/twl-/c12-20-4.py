#方法二：定义一个新函数，调用原来函数，新函数里编写新增功能代码。
#正确
import time
def func():
    print('hello')
    time.sleep(1)
    print('Python')
def deco(): 
    startTime = time.time()
    func()
    endTime = time.time()
    usecs = (endTime - startTime)*1000000
    print('Time is %d us'%usecs)

deco()

##如果func()函数有很多，怎么办？重复执行deco()n遍吗？