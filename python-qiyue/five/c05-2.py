
#值类型与引用类型
# int、str、tuple： 值类型(不可变数据类型)；list、set、dict 引用类型(可变数据类型)
#值类型（不可变数据类型），不支持item、append方式修改元素值：
a = 1
b = a
a = 3
print(b,a)

str1 = 'Hello Python'
str2 = str1 
str1 = 'Hello word'
print(str2,str1)

t1 = (1,2,3)
t2 = t1
t1 = (4,5,6)
print(t2,t1)

#引用类型（可变数据类型），可以append、item修改值：
la = [1,2,3]
lb = la
la[0] = '1'
print(la,lb)

#看一个现象：

# >>>
# >>> a = 'Hello'
# >>> a = a + 'python'
# >>> print(a)
# Hellopython

# >>> b = 'Hello'
# >>> id(b)
# 82449024
# >>> b = b + 'Python'
# >>> id(b)
# 82448240
# >>>
# 82448240

# >>> 'python'[0] = w
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'w' is not defined
# >>> 'python'[0]
# 'p'
# >>>