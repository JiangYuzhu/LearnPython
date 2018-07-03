#python三大特性:继承性、封装性、多态性
#Python继承性，父类、子类
#意义或作用：避免定义重复的方法和变量
#python可以单继承、多继承（多个父类）

class Human():

    sum = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)

    def do_homework(self):
        print('This is parent method')
