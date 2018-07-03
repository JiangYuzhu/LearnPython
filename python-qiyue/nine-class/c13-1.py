
#没有什么是不可访问的


class Student():

    sum1 = 0
    name = '七月' 
    age = 0
    score = 0

    def __init__(self,name,age,score):  
        self.name = name    
        self.age = age
        self.__score = score
        print(self.name +'同学本次考试成绩为：' + str(self.__score))
             
    def do_homework(self):
        print('do homework')
        self.__class__.sum1 += 1      
        print('当前学生数量为：' + str(self.__class__.sum1)) 
    
                
student1 = Student('石敢当',6,59)
student1.__score = -1 
#不是因为实例变量的私密性没有生效，而是因为python的动态特性，这里给实例新添加了一个变量__score

student1.__age = 18
print(student1.name + '同学今年' +str(student1.__age) + '岁了,本次考试成绩为：'
 + str(student1.__score))
student2 = Student('李诺',9,98)
print(student1.__dict__) 
print(student2.__dict__)
###系统把私有变量改为_Student__score###
print(student1.__score)
