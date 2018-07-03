
#生成器，generator
#列表生成式一次性生成列表的所有元素，如果仅使用列表少部分（比如前面几个）元素，后面的所有元素
#占用的存储空间就浪费了。
#（列表）生成器采用推算的方法一个接一个生成列表的元素。
# 如果列表元素可以按照某种算法推算出来，那我们可以在循环的过程中不断推算出后续的元素，
# 这样就不必创建完整的list列表，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器

#（一）。创建生成器最简单的方法是将列表生成式的[]改为():
g = (x*x for x in range(100))
print(type(g))
#通过next()函数获得generator下一个返回值：
print(next(g))
print(next(g))
#generator是可迭代对象，使用for循环取得需要的元素
#比如：使用该生成器，取得列表的前6个元素：(代码未写成功)

# for n in g:
#     if  n == 6:
#         break
#     print(n)

#（二）.斐波那契数列：
print('~~~~~~~~~以下为使用函数生成斐波那契数列~~~~~~~~~~~')
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n += 1
    return 'Done!'
fib(10)

print('~~~~~~~~~以下为Fibonacci函数另一种写法~~~~~~~~~~~')

def fib1(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        t = (b,a+b)
        a = t[0]
        b = t[1]
        n += 1
    return 'Done!'
fib1(15)

##（三）。使用生成器生成斐波那契数列：
##如果一个函数定义中包含了yield关键字，这个函数就不是普通函数，而是一个生成器。
##在执行过程中，遇到yield就中断，下次继续执行。
print('~~~~~~~~~以下为生成器生成斐波那契数列~~~~~~~~~')
def fib2(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n += 1
    return 'Done!'
fib(10)