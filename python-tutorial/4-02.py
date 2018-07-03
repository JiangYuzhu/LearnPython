
#寻找质数/素数。
#下面是教程中的代码，做了修改，结果不对。教程的也不对
#break语句该放在那里？

# a = [2]
# integer = int(input('请输入一个较大的整数：'))

# for n in range(3,integer):  
#     for x in range(2,n):
#         if n % x == 0:
#             print(n,'equals',x,'*',n//x)
#             #break
#         else:
#             a.append(n)
#             break
#             # print(n,'is a prime number')
       
# print('从2到',integer,'中，共有质数：',len(a),'个')
# print(a)

#下面来自网络，正确。
# n = 10000
# numbers = list(range(2, n + 1))
# i = 2
# while i < 10001:
#     for m in numbers:
#         if i < m and m % i == 0:
#             numbers.remove(m)
#     i = i + 1
# print(numbers)
# print("\nThere were", len(numbers), "prime numbers up to", n)

#根据上面代码修改：
import time
n = int(input('请输入一个较大的正整数：'))
numbers = list(range(2,n+1))
i = 2
print(time.time)
while i < n+1:
    for m in numbers:
        if i < m and m % i == 0:
            numbers.remove(m)
    i = i + 1
#print(numbers)
print("\n小于",n,"的质数共有：",len(numbers),"个")
print(time.time)


