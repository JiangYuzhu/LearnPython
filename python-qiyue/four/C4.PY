
#集合set
#{}定义，各元素用逗号分隔
#如何定义空的集合？
print(type({})) #{}这是空的字典
print(type(set())) #set()才是空的集合定义方法
#特性：
#1.无序，不支持索引(序号)indexing、切片subscriptable操作；
#2.不重复
#支持哪些操作：
#len()、in、max()、min()
#特殊操作
#1.求两个集合的差集
a = {1,2,3,4,5,6}
b = {3,4,7}
print(a-b)
#2.求两个集合的交集
print(a&b)
#3.求连个集合的并集
print(a | b)

