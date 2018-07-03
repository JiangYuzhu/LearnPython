##global关键字，如何使局部变量变成全局变量，比如使函数内部的定义的变量被模块使用。

def demo():
    global c #先定义
    c = 20
demo()
print(c)

#c14.py演示其他模块使用该变量