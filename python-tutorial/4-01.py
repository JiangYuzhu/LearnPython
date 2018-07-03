
words = ['calculator','cat','window','defenestrate']

for w in words:
    print(w,len(w))

for w in words[:]:     # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0,w)
print(words)

a = ['Mary','had','a','little','lamp']

for i in range(len(a)):  #迭代序列的索引
    print(i,a[i])
