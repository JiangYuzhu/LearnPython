#变量的作用域

c = 50
def add(x,y):
    c = x + y #变量c仅作用与函数内部，与外部c没有关系
    print(c)
print(c)

# #下面的例子更能说明：
# def  demo():
#   a = 10
# print(a) #将会报错:a没有定义 

#函数外部的变量覆盖整个模块
d = 20
def demo2():
    print(d)
demo2()

#变量作用域的相对性
def demo3():
    e = 50
    #a = '' 不需要，其他语言如果要实现引用for循环内部的变量，可以在for循环外部先定义并赋空值
    for i in range(0,9):
        a = 'a'
        e += 1
    print(a) 
    #pythonfor循环的外部可以直接引用for循环内部定义的变量，因为python没有
    #块级作用域的概念
    print(e)
demo3()