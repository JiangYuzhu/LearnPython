#类的定义
#类：抽象的模板，
#对象：由模板实例化得到的具体事物
#实例化：
#函数与方法：
#类最基本的作用：封装
#不能在类的内部调用函数/方法

# class Student(object):  #定义类
#     name = ''     #类属性 
#     age = 0

#     def print_file():     #定义方法，报错：
#         print('name:' + name)
#         print('age:' + str(age))
  
# student = Student()    #类的实例化
# student.print_file()   #类的方法调用

# class Student():  #定义类
#     name = ''     #类属性
#     age = 0

#     def print_file(self):     
#         print('name:' + name)    ##报错：变量name、age没有定义
#         print('age:' + str(age))
  
# student = Student()    #类的实例化
# student.print_file()   #类的方法调用

class Student():  
    name = ''     
    age = 0

    def print_file(self):     #定义方法，类里定义函数必须加上“固定关键字：self”
        print('name:' + self.name)
        print('age:' + str(self.age))

     # print_file 不能在类的内部调用，类只负责定义，不负责执行。 

student = Student()    #类的实例化,形成对象，实例变量
student.print_file()   #类的方法调用

#类的使用（类的实例化、方法调用等）在实际项目应放在其他模块文件中