#构造函数

class Student():
    name = ''
    age = 0

    def __init__(self):  #实例化的时候，python自动调用构造函数，不需要显示调用
        print('student')
    
    def do_homework(self):
        print('homework')

student = Student()
a = student.__init__() #可以显示调用构造函数，但是实际编程没有必要
print(a)               #默认返回值为None，构造函数不能指定返回其他值
print(type(a))         #Class'NoneType'