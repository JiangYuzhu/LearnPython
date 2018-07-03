
#子类方法调用父类方法：
# （二）：super关键字

from c14 import Human   

class Student(Human):

    school = ''

    def __init__(self,school,name,age):
        self.school = school
        super(Student,self).__init__(name,age) #子类方法调用父类方法
        
    def do_homework(self):
        print('english homework')
        super(Student,self).do_homework()   #子类方法调用父类方法

student1 = Student("人民路小学",'石敢当',10)
print(student1.name) 
print(student1.age)
student1.do_homework()

  