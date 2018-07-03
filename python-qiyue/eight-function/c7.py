
#可变参数,参数的实际个数是可变的，参数前加*来表示，如*param
#典型的内置函数print()可以接收多个参数，print('a','b','c','d')

def demo(*param):
    print(type(param))
    print(param)
demo(1,2,3,4,5,6)
demo()
a = (7,8,9)
demo(a)  #变量a是元组，直接传递，变成二维元组
demo(*a)  ####3

def demo2(param):
    print(type(param))
    print(param)
demo2((1,2,3,4,5,6))
demo2(())


#可变参数的一个实际应用例子:求多个数字的平方和
def squsum(*param):
    sum = 0
    for i in param:
        sum += i * i
    print(sum)
squsum(1,2,3,4,5,6)
squsum(*[1,2,3,4,5,6])

def demo3(param1,*param,param2=2):
    print(param1,end=' ')
    print(*param,end=' ')
    print(param2)
demo3('a',1,2,3,'param')
demo3('a',1,2,3,param2='param')
