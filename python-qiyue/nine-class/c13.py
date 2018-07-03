
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
#这里的__score不是实例变量__score
# 如果想动态尝试添加私有变量是不可以的
print(student1.__score)
print(student1.__dict__)
#从这个输出可以看出，python将私密的实例变量__score改名为_Student__score.
#这是python对私有变量的保护机制。


student2 = Student('小艾',21,60)
#print(student2.__score)  ##报错，说明私有变量不能在类的外部被访问
print(student2.__dict__)