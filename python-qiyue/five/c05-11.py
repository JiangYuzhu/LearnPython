
#成员运算符：is，not is

# >>> a = 1
# >>> b = 1.0  #比较运算符是对“值”进行比较
# >>> a == b
# True
# >>> a is b  #比较的是两个变量/对象的身份是否相等,身份、对象、内存地址
# False       

# >>> a = 1
# >>> b =1
# >>> a == b
# True
# >>> a is b
# True
# >>> id(a)    #
# 1370149936
# >>> id(b)
# 1370149936 #两个内存地址是否相等，
# >>>
# >>> id(1)
# 1370149936

a = 1
b = 1
print(id(a),id(b),id(1))
print(a is b)
print(a == b)

a = 2
b = 2
print(id(a),id(b),id(2))
print( a is b )
print( a == b )

# 上段代码块运行结果：
# 1370149936 1370149936 1370149936
# True
# True
# 1370149952 1370149952 1370149952
# True
# True

