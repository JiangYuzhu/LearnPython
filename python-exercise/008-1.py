
#9*9乘法表
print('~~~~~~~~完整矩形格式~~~~~~~~~')
for i in range(1,10):
    for j in range(1,10):
        print('%d*%d=%2d\t' %(i,j,i*j),end='') #end=''使print()不换行；
    print('') #换行
    
#'%d*%d=%2d\t' %(i,j,i*j) 格式化
print('~~~~~~~~~~左上三角形~~~~~~~~~~')
for i in range(1,10):
    for j in range(i,10):
        print('%d*%d=%2d\t'%(i,j,i*j),end='')
    print('')



