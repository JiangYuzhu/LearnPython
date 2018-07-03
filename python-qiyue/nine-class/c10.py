
#类方法
#为什么？有什么作用？操作类相关的变量。

class Student():
    sum1 = 0        
    name = '七月'   
    age = 0

    def __init__(self,name,age):  
        self.name = name    
        self.age = age
             
    def do_homework(self):
        print('do homework')
        # self.__class__.sum1 += 1      
        # print('当前学生数量为：' + str(self.__class__.sum1)) 
    
    @classmethod     #方法前加上该装饰器，表示这是个类方法。python中@表示装饰器。
    def plus_sum(cls):  #cls与self概念类似，分别代表类本身、对象本身
        cls.sum1 += 1   #cls代表类本身，所以等同于：Student.sum1 += 1
        print('当前学生数量为：' + str(cls.sum1))
    
student1 = Student('石敢当',6)
#用类调用类方法
Student.plus_sum()  
student2 = Student('喜小乐',8)
Student.plus_sum()
student3 = Student('小小',7)
#python也可以用对象来调用类方法：
student3.plus_sum()   

