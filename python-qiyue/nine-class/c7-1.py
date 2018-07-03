
#类变量和实例变量的查找顺序

class Student():
    sum = 0         #学生总人数
    name = '七月'   #类变量
    age = 0       
    def __init__(self,name,age):  
        self.name = name   #正确的实例变量表示方式,实例变量名仍然为name、age。
        self.age = age    #self代表的就是实例对象本身；
    
student1 = Student('石敢当',6)
print(student1.name)  
print(Student.name)

#用一个方法来验证student1到底有没有name这个实例变量
print(student1.__dict__) 
#__dict__保留着对象下所有的变量。对象student1有变量
print(Student.__dict__) 
#类的__dict__里保存的各种类变量。
