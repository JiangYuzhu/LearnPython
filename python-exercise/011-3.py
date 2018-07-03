
def Fibo(x):
    L = [1,1] #如果初始L为空列表，append错误：‘read only’ ？？？
    for n in range(2,x):
        # if n == 1:
        #     L.append = 1
        #     break
        # elif n == 2：
        #     L.append = 1
        #     break
        # else:
        L.append(L[n-2]+L[n-1])
    return L
    # print(L)      ###如何格式化打印，比如每行打印10个，并且右对齐；
print("请输入一个正数:")
num = int(input())
print('斐波那契数列:')
fibo = Fibo(num)
print(fibo)
huangjin =fibo[num-2]/fibo[num-1]
print('黄金分割数值：',huangjin)