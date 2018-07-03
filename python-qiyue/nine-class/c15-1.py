
#子类方法调用父类方法：
#（一）：

from c14 import Human   

class Student(Human):

    school = ''

    def __init__(self,school,name,age):
        self.school = school
        Human.__init__(self,name,age) #通过类调用，因为是普通调用，必须传入self
        
    def do_homework(self):
        print('english homework')

student1 = Student("人民路小学",'石敢当',10)
print(student1.name) 
print(student1.age)
student1.do_homework()
Student.do_homework(student1) #类调用实例方法，这种调用很可笑
Student.do_homework('')
 