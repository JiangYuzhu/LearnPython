
#1.self与实例方法
#2.在实例方法中访问实例变量和类变量
#3.构造函数和实例方法的区别：
# 3.1构造函数是一种特殊的实例方法，两者主要区别在于调用方式不一样。
# 构造函数是通过类加上括号来调用的（类实例化时自动调用），
# 普通的实例方法是通过对象加上.来调用的。
# 3.2另一个区别在于意义不同，构造函数的目的在于初始化类的各个特征/属性，实例方法的主要作用是
# 描述类的行为

class Student():
    sum1 = 0         #学生总人数，方法里如何使用类变量？
    name = '七月'   #类变量
    age = 0

    def __init__(self,name,age):  
        self.name = name   #实例变量
        self.age = age 
        print(name)  #结果是什么？
        print(age)

    def do_homework(self): ##定义时需要显示指定self，调用时不需要
        print('do homework')
        # print(sum1)
    
student1 = Student('石敢当',6)
print(student1.do_homework)
print(student1.name)  
print(Student.name)
