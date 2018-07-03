##匿名函数lambda

f = lambda x,y,z:x*x+y*y+z*z

print(f(3,4,5))


L = list(filter(lambda n:n%2==1,range(1,20)))
print(L)