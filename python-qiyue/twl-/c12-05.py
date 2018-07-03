
#reduce

from functools import reduce 
# reduce(function,sequence[,initial]) --> value

list_x = [1,2,3,4,5,6,7,8,9]
r1 = reduce(lambda x,y:x+y,list_x)
print(r1)
r2 = reduce(lambda x,y:10*x+y,list_x)
print(r2)
list_y = ['1','2','3','4','5','6']
r3 = reduce(lambda x,y:x+y,list_y,'aaaa')
# r3 = reduce(lambda x,y:x+y,list_y,initial='aaaa') 错误写法
print(r3)

