
##filter函数
#filter()函数接受两个参数：一个是函数，一个是序列；filter()把传入的函数依次作用于序列的
#每个元素，根据函数返回值结果是True还是False来决定保留还是丢弃该元素。
list_A = [1,1,0,1,0,2,0,0,3,1,0]
list_AA = filter(lambda x:x,list_A)
print(list_AA) #fileter()返回一个iterator，是一个惰性序列。
print(list(list_AA))

odd = filter(lambda x:True if x%2 ==1 else False,list(range(1,20)))
print(list(odd))

##关键在于设计“筛选函数”

#将序列中的小写字母元素删掉
list_str = ['a','B','E','A','d','b','F']
list_upp = filter(lambda x:True if upper(x)==x else False,list_str)
print(list(list_upp))

##用filter求素数！！！
