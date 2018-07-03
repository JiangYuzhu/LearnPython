
#成员的可见性:公开、私有
#3.私有的实例方法，类的外部无法访问；
#4.私有的变量，类的外部仍然可以访问；

class Student():

    sum1 = 0
    name = '七月' 
    age = 0
   
    def __init__(self,name,age):  
        self.name = name    
        self.age = age
       
    def __marking(self,score): #python用"开头"双下划线表示成员的私密性
        self.__score = 0
        if score < 0:
            print('学生分数不能小于零！')
            return
        else:
            self.__score = score
        print(self.name + '同学本次考试成绩为:' + str(self.__score))
               
# student1 = Student('石敢当',6)
# student1.__marking(-1)             ##报错
# student2 = Student('小爱',7)
# student2.__marking(59)
Student.__score = -20             ##不报错

