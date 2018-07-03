
#成员的可见性:公开的public、私有的private
#成员：变量、方法；
#可见性：公开的、私有的，默认是公开的，

# 1.如何定义私有的变量、方法；
#前面加双下划线认为是私有的。

#1.类的内部调用成员、类的外部调用成员

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
        print(self.name + 'do homework')
        self.do_english_homework() ##类的内部调用成员(实例方法)
       
    def do_english_homework(self):
        print(self.name + 'do english homework')
    
    @classmethod
    def plus_sum(cls): 
        cls.sum1 += 1
        print('班级学生总数为：'+ str(cls.sum1))
        #print(self.name + '班级学生总数为：'+ str(cls.sum1))
        #如何在类方法中调用实例变量？


    @staticmethod
    def add(x,y):   
        print('This is a static method')
        print(Student.name)  
            
student1 = Student('石敢当',6,59)
student1.do_homework()   ##类的外部调用成员(实例方法)
Student.plus_sum()

