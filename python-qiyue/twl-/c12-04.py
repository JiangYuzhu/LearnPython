
#map与lambda表达式

list_x = [1,2,3,4,5,6,7,8]
r = map(lambda x:2*x*x,list_x)
print(r)
print(type(r))
print(list(r))

list_y = [1,2,3,4,5,6]
r2 = map(lambda x,y:2*x*x+y,list_x,list_y)
print(list(r2))
