
#map
#求抛物线y的坐标值
#使用for循环求解：
list_x = [1,2,3,4,5,6,7,8]
def y(x):
    a= 2
    return a*x*x
L = []
for x in list_x:
    # L.append = y(x)
    L.append(y(x))
print(L)

#使用map类求解：
r = map(y,list_x)
print(r)
print(type(r))
print(list(r))

#将数字转换为字符串
print(list(map(str,list_x)))



