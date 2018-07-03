
# 输入三个整数，然后从小到大排序后输出。

l = []

for i in range(3):
    x = input('please input interger:\n')
    l.append(x)

l.sort()
print(l)