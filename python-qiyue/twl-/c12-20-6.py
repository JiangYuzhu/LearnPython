

#方法二：定义一个新函数，调用原来函数，新函数里编写新增功能代码。
#本示例执行报错
import time
def func(a):
    print('hello')
    time.sleep(1)
    print(a)
def deco(func): 
    startTime = time.time()
    func()    ##执行报错 'NoneType'object is not callable.如何给func()调用传递参数
    endTime = time.time()
    usecs = (endTime - startTime)*1000000
    print('Time is %d us'%usecs)

deco(func('Python'))
deco(func('World')) 

##如果func()函数有很多，怎么办？重复执行deco()n遍吗？