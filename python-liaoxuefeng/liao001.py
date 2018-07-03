
#对列表中的每个名字依次打印出:Hello,xxxx!

names = ['James','Marry','Lisa','Steph']

for name in names:
    print('Hello,'+name+'!')


n = 1
list = []
while n <= 100:
    if n > 9:
        break #当if条件满足，break语句将使while循环退出；
    n = n + 1 #开始忘记了，结果运行‘没反应’，强行中断，报‘MemoryError’
    list.append(n)
print(list)
print('END')
