
#关键字可变参数,任意个数的关键字参数

#打印任意城市的温度
def city_temp(**param):  #在参数前加两个*
    print(type(param)) #结果显示是字典类型
    print(param)
city_temp(bj='32c',sh='31c',xm='23c')

print('~~~~~~~~~~~~~~~')
def city_temp2(**param):
    for c in param:   #一个变量只能打印出字典的健
        print(c)
city_temp2(bj='32c',sh='31c',xm='23c')

print('~~~~~~~~~~~~~~~')
def city_temp3(**param):
    for key,value in param: #用两个变量来遍历字典的key和value
        print(key,':',value)
city_temp3(bj='32c',sh='31c',xm='23c')

print('~~~~~~~~~~~~~~~')
def city_temp4(**param):
    for key,value in param.items(): #需使用字典的items方法
        print(key,':',value)
city_temp4(bj='32c',sh='31c',xm='23c')

print('~~~~~~~~~~~~~~~')
def city_temp5(**param):
    for key,value in param.items(): 
        print(key,':',value)
a = {'bj':'32c','sh':'31c','xm':'23c'}
city_temp5(**a)  #使用字典传递参数