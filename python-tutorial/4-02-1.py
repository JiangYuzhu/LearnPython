
n = 10000
numbers = list(range(2, n + 1))
i = 2
while i < 10001:
    for m in numbers:
        if i < m and m % i == 0:
            numbers.remove(m)
    i = i + 1
print(numbers)
print("\nThere were", len(numbers), "prime numbers up to", n)


import math    
   
def isPrime(n):    
    if n <= 1:    
        return False   
    for i in range(2, int(math.sqrt(n)) + 1):    
        if n % i == 0:    
            return False   
        return True   
        
print(isPrime(10))
   
#单行程序扫描素数    
   
from math import sqrt    
N = 100   
[ p for p in   range(2, N) if 0 not in [ p% d for d in range(2, int(sqrt(p))+1)] ]    
   
   
#运用python的itertools模块    
   
from itertools import count

def isPrime(n):    
    if n <= 1:    
        return False   
    for i in count(2):    
        if i * i > n:    
            return True   
        if n % i == 0:    
            return False   
print(isPrime(10))