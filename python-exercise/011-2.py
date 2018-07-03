
def Fibo(x):
    a = [0,1]
    #while i < x:
    for n in range(2,x):
        # if n == 0:
        #     #print('%d' %(1),)
        #     quit
        # elif n == 1:
        #     #print('%d' %(1))
        #     quit
        # else:
        # a.append(a[n-2]+a[n-1])
        a.append(a[n-2] + a[n-1])
    return a
    # print(a)      ###如何格式化打印，比如每行打印10个，并且右对齐；
print("请输入一个正数:")
num = int(input())
print('斐波那契数列:')
f = Fibo(num)
print(f)
huangjin =f[num-2]/f[num-1]
print('黄金分割数值：',huangjin)