
#静态方法
#静态方法与面向对象关联较弱,与类、对象基本没什么关系。

class Student():
    sum1 = 0        
    name = '七月'   
    age = 0

    def __init__(self,name,age):  
        self.name = name    
        self.age = age
             
    def do_homework(self):
        print('do homework')
    
    @classmethod    
    def plus_sum(cls):  
        cls.sum1 += 1  
        print('当前学生数量为：' + str(cls.sum1))


    @staticmethod    #使用该装饰器即可定义一个静态方法，它与面向对象关联性较弱。当与类
                    #和对象没有什么太大关系时，使用静态方法。
    def add(x,y):    #无需像类方法、实例方法中所需要的代表自身的"关键字"
        print('This is a static method')
        print(Student.name)  #静态方法可以访问类变量.
        
    
student1 = Student('石敢当',6)
student1.add(1,2)  #可以使用对象调用静态方法
Student.add(1,2)   #可以使用类调用静态方法
Student.plus_sum()

