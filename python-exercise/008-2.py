
# 9*9乘法表

i = 1
while i<=9:
    n = 1
    while n<=i:
        print('%d*%d=%2d\t'%(n,i,i*n),end='')
        n += 1
    print('')
    i += 1
