
#类属性变量和实例属性变量的查找顺序：
#先找实例变量，如果没有，再找类变量


class Student():
    sum = 0         #学生总人数
    name = '七月'   #类变量
    age = 0       
    def __init__(self,name,age):  
        name = name   #不正确的实例变量表示方式，正确的应该是：self.name,self.age
        age = age 
    
student1 = Student('石敢当',6)
print(student1.name)  
#不存在的实例变量，为什么不是None，而是把类变量的值打印出来了？ 
print(Student.name)

#用一个方法来验证student1到底有没有name这个实例变量
print(student1.__dict__) 
#内置变量（__dict__）保留着对象下所有的变量。结果为空，说明对象student1没有变量
