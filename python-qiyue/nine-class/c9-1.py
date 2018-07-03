
class Student():
    sum1 = 0        
    name = '七月'   
    age = 0

    def __init__(self,name,age):  
        self.name = name    
        self.age = age
       
      
    def do_homework(self):
        print('do homework')
        self.__class__.sum1 += 1      
        print('当前学生数量为：' + str(self.__class__.sum1)) 
    
student1 = Student('石敢当',6)
print(student1.do_homework())
student2 = Student('喜小乐',8)
print(student2.do_homework())
   