#用1,2,3,4四个数字，组成位数不重复的三位数。

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j!=k and k!=i:
                print(i,j,k)
                # print(i*100+j*10+k)
                # print(str(i)+str(j)+str(k))

for i in [1,2,3,4]:
    for j in [1,2,3,4]:
        for k in [1,2,3,4]:
            if i!=j and j!=k and k!=i:
                print(i,j,k)
                # print(i*100+j*10+k)
                # print(str(i)+str(j)+str(k))

import this
