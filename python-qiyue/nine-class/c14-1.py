
#子类可继承父类变量和方法

from c14 import Human   #如果是c14-*会报语法错误

class Student(Human):

    def do_homework(self):
        print('english homework')

student1 = Student('石敢当',9)
print(student1.sum)    #变量可继承
print(Student.sum)
print(student1.name)
print(student1.age)
student1.get_name() #方法可继承