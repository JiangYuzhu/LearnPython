
#返回函数

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
print(calc_sum(1,3,5,7,9))

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

print(lazy_sum(1,3,5,7,9,11,13)())
f = lazy_sum(2,4,6,8,10)
print(f())

#一个错误的例子：(没有文中所说的问题,未能重现)
#文中强调：返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f()) #文中为fs.append(f)
    return fs
print(count())

f1 = count()
f2 = count()
f3 = count()
print(f1)
print(f2)
print(f3)

##练习：
