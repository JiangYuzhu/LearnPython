#Number子类型：bool类型和复数（complex,表示：22j）

print(type(True))

#布尔类型是数字类型的子类型
#非零都表示True(真)，零表示False(假)
#其他类型非空表示True，空表示False
print(int(True))
print(int(False))
print(bool(1))
print(bool(0))
print(bool(2))
print(bool(-1))
print(bool(1.1))
print(bool(-1.1))
print(bool(0.01))
print(bool(0o7))
##其他类型的数据与bool类型之间的关系
print(bool('abc'))
print(bool(''))
print(bool([1,2,3]))
print(bool([]))