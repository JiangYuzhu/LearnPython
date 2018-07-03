
#子类构造函数如何继承父类构造函数

#子类变量不可能完全继承自父类。
#

from c14 import Human   

class Student(Human):

    school = ''

    def __init__(self,school,name,age):
        self.school = school
        Human.__init__(name,age) #调用父类的构造函数，子类能否正确得到name和age？
        
    def do_homework(self):
        print('english homework')

student1 = Student("人民路小学",'石敢当',10)
print(student1.sum)
print(Student.sum)
print(student1.name) 
print(student1.age)

 