

# 输入三个整数，然后从小到大排序后输出。

l = []

for i in range(3):
    x = input('please input interger:\n')
    l.append(x)

if l[0] > l[1]:
    l[0],l[1] = l[1],l[0]
if l[1] > l[2]:
    l[1],l[2] = l[2],l[1]
if l[0] > l[1]:
    l[0],l[1] = l[1],l[0]

print(l)