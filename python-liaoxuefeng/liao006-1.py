##使用filter()生成指定范围内的质数。
#下面代码摘自百度百科：埃氏筛选法

def _int_iter():#定义生成器，生成从3开始的无限奇数序列
    n = 1
    while True:
        n = n + 2
        yield n
 
def  _not_divisible(n):#定义筛选函数
    return lambda x:x % n > 0
 
def primes(): #定义删选质数的函数
    it = _int_iter()#初始序列
    while True:
        n = next(it)#返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)#构造新序列
numbers = 0
for n in primes():#构造循环条件，使之可以输出任何范围的素数序列
    if n < 10000:
        print(n)
        numbers += 1
    else:
        break
print(numbers)

