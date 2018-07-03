
#类属性变量和实例属性变量
#类变量是什么，有什么作用？和类相关联在一起的，
#实例变量是什么，有什么作用？和对象相关联在一起的；使用self.name来保存对象的特征值；
#

class Student():
    name = ''   #类变量，这里的类变量name和age对于抽象的类来说没有意义。
    age = 0

    def __init__(self,name,age):  
        self.name = name   
        #实例属性变量，使用self关键字（其实是可以随意起个名字，并不是关键字）来定义实例变量，
        # 与其他语言有所不同
        #self表示实例对象本身，定义时需要，调用时不需要传递实参。
        self.age = age 
        print('student')
    
    def do_homework(self):
        print('homework')

student1 = Student('石敢当',6) #实例化时，将实参传递给构造函数的形参。
print( student1.name + '同学今年' + str(student1.age) + '岁')   
  #正确打印出‘石敢当’                    