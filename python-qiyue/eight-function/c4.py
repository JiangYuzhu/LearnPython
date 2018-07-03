#序列解包与链式赋值 
a = 1
b = 2
c = 3

a,b,c = 1,2,3 #使得代码简洁，而不失易读性
print(a,b,c)

d = 1,2,3
# print(type(d)) # class 'tuple'
# print(d)   #结果:(1,2,3)
a,b,c = d   #序列解包
print(a,b,c) #结果：1,2,3

a,b,c = [1,2,3]
print(a,b,c) #结果：1,2,3


d = 1,2,3
a,b,c = d
print(d)
print(a,b,c)
#序列解包，个数要相等

#链式赋值
a = 1
b = 1
c = 1
a,b,c = 1,1,1
a = b = c = 1 #链式赋值
print(a,b,c)
