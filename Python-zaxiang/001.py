#range()
for i in range(10):
    print(i)
    i = 20 #这里虽然给i赋值，但是不会影响，因为下次循环时，再次被赋给新的循环值

a,b = 0,1
while b < 1000:
    print(b)
    a,b = b,a+b

for n in range(2,10):
    for x in range(2,n):
        if n%x == 0:
            print(n,'=',x,'*',n//x)
            break
    else:
        print(n,'is a prime number')


L = []
for n in range(2,100):
    for x in range(2,n):
        if n%x == 0:
            break
    else:    ##不太理解！
        L.append(n)
print(L)


             
