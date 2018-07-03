
c = 1

def func1():
    #c = 2
    def func2():
        #c = 3
        print(c)
    func2()
#作用域链，作用域具有链式特性（就近取值）
func1()

#结果为3，注释掉c=3，结果为2，再注释掉c=2，结果为1.