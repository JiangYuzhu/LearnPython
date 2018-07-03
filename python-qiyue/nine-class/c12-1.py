
#成员的可见性:公开、私有
#2.公开的方法变量，类的访问

class Student():

    sum1 = 0
    name = '七月' 
    age = 0
   
    def __init__(self,name,age):  
        self.name = name    
        self.age = age
       
    def marking(self,score):
        self.score = 0
        if score < 0:
            print('学生分数不能小于零！')
            return
        else:
            self.score = score
        print(self.name + '同学本次考试成绩为:' + str(self.score))
               
student1 = Student('石敢当',6)
student1.marking(-1)
student2 = Student('小爱',7)
student2.marking(59)

