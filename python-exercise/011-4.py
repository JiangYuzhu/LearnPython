
###网上关于Fibo数列的Python代码：
#1:
def Fibo(num):
    a = 0
    b = 1
    i = 0

    while i < num:
        print(a)
        a,b = b, a+b #逻辑没看明白
        i += 1

print(Fibo(30))

#2:
def fibo1(num):
    numList = [0,1]
    for i in range(2,num):
        numList.append(numList[i-2] + numList[i-1])
    return numList
print(fibo1(30))

#3:
def fibo2(n):
    x, y = 0, 1
    while(n):
        x,y = y, x+y
        n = n-1
    return x   #函数返回一项
print(fibo2(30))

#4.
def fibo3(n):
    def fib_iter(n,x,y):
        if n == 0:
            return x
        else:
            return fib_iter(n-1, y, x+y)
    return fib_iter(n, 0, 1)
print(fibo3(30))
