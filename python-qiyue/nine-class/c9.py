
#在实例方法中访问类变量的方式
#在类的内部和外部如何访问类变量和实例变量：
#在类的内部，访问类变量的方法：1）Student.sum1;2)self.__class__.sum1
#在类的内部，访问实例变量的方法：self.name
#在类的外部，访问类变量的方法：类名.类变量；
#在类的外部，访问实例变量的方法：对象名.实例变量

class Student():
    sum1 = 0        
    name = '七月'   
    age = 0

    def __init__(self,name,age):  
        self.name = name    #类的内部使用self.来访问实例变量 
        self.age = age
        #Student.sum1 += 1     #类的内部也可以使用类名加上.号来访问类变量。
        print('当前学生数量为：' + str(Student.sum1)) 
        self.__class__.sum1 += 1 
        print('当前学生数量为：' + str(self.__class__.sum1)) #类的内部访问类变量的第二种方式
      
    def do_homework(self):
        print('do homework')
    
student1 = Student('石敢当',6)
print(student1.name)   #类的外部，使用对象名加上.号来访问实例变量
print(Student.name)   #类的外部，使用类名加上.号来访问类变量
print(student1.do_homework())
student2 = Student('喜小乐',8)
print(student2.name)
print(Student.name)


