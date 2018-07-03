#实例化及实例化的意义

class Student():  
    name = ''     
    age = 0

    def print_file(self):     
        print('name:' + self.name)
        print('age:' + str(self.age))

     
student1 = Student()  #这三个对象相等(人的世界)，因为表示对象特征的name、age值相同；
student2 = Student()  #计算机认为是三个不相等的对象
student3 = Student()     

print(id(student1))   #这三个对象在计算机里是三个不同的对象，它们在内存里的地址完全不同；
print(id(student2))
print(id(student3))

#可以用is、==来比较(is 表示两个对象完全相同，不仅特征相同而且ID(内存地址)也相同)，
#==表示两个对象的内容相同
print(student1 == student2)  #结果为False
print(student2 == student3)
print(student1 is student2)  #结果为False
print(student2 is student3)