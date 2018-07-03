for x in range(20,0,-2):
    print(x,end=' | ')
print('\n')
a = []
b = []
for y in range(1,101):
    if y%2 == 0:
        a.append(y)
    else:
        b.append(y)
print(a,'\n')
print(b)
