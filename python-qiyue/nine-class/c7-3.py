

class Student():
    sum = 0 #班级学生总人数，这个类变量有意义。 
    name = '七月'   #站在面向对象的角度来考虑，这里定义的类变量name、age没有意义!
    age = 0         #name和age是具体的，和抽象的Student类关联没有意义，应和具体的对象关联。

    def __init__(self,name,age):  
        self.name = name   #实例变量
        self.age = age 
        print('student')
    
    def do_homework(self):
        print('homework')

student1 = Student('石敢当',6)
student2 = Student('喜小乐',7)
print(student1.name + '同学今年' + str(student1.age) + '岁')   
print(student2.name + '同学几年' + str(student2.age) + '岁')
print(Student.name)