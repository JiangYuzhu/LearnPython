#自定义函数
#def funname(parameter_list):
#    pass #空语句/占位符，表示函数体，即代码块
#1.参数列表可以没有
#2.使用return value返回函数值，如果没有return语句，函数返回空值；或不使用return；

# 本节学习：
# 1）如何定义函数、调用函数；
# 2）如何设置系统递归深度；
# 3）如何查看系统内置函数；
# 4）如何查看内置函数的代码；
# 5）如何判断自定义的变量函数的名称与系统内置的变量函数的名称同名；

#例一：加法函数
def add(x,y):
    result = x + y
    print(result)
    return result
    #print(result)
print(add(1,2))

#例二：自定义print函数，调用系统的print函数实现打印
#def print(code):
#    print(code)
#print('python')
#执行发生错误
#[Previous line repeated 995 more times]
#RecursionError: maximum recursion depth exceeded

# import sys
# sys.setrecursionlimit(2000)
# def print(code):
#    print(code)
# print('python')
#最大递归深度996次,与计算机硬件、python版本有关

def print_code(code):
    print(code)
    #return none，没有return同于return none
print_code('python')

a = add(1,2)
b = print_code('Python')  #函数调用打印出python，函数返回值为None，b为None
print(a,b)  #执行结果：3 None


#如何判断定义的变量、函数与系统内置变量、函数同名？