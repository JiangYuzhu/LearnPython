

# 由键盘输入n个整数，然后由小到大输出。

l = []

n = int(input('input the numbers of interger:'))

for i in range(n):
    x = int(input('please input interger:'))
    l.append(x)

l.sort()
print(l) 
