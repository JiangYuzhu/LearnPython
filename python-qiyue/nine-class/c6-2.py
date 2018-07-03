
class Student():
    name = ''
    age = 0

    def __init__(self,name,age):  #初始化对象的属性
        name = name   #python知道赋值左边是变量，右边是参数
        age = age 
        print('student')
    
    def do_homework(self):
        print('homework')

student1 = Student('石敢当',6)
print(student1.name)   #访问类/对象某个变量或方法，都是通过.号来操作
                       #没有打印预期的‘石敢当’，而是初始的空字符串