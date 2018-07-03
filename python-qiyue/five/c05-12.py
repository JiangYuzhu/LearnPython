
#变量的值、身份、类型
#对象的三个基本特征：值（value）、身份（id）、类型（type）

# 如何比较两个变量/对象的类型？
# >>> a = 1
# >>> type(a) == int
# True
# >>> type(a) == str
# False
# >>>
# >>> isinstance(a,int)
# True
# >>> isinstance(a,str)
# False
# >>>
# >>> isinstance(a,(str,tuple))
# False
# >>> isinstance(a,(str,int))
# True
# >>>