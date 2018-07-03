#默认参数，函数定义时设计的形参较多，调用函数时部分参数有默认值，不需要调用时都传递实参值
#简化调用

def print_student_files(name,gender,age,school):
    print('我叫' + name)
    print('我今年' + age + '岁')
    print('我是' + gender + '生')
    print('我在' + school + '读书')
print_student_files('蒋东锦','男','4','半山园幼儿园') #逗号为半角时报错：invalid character
print('~~~~~~~~~~~~~~~~~~~~~~~~~~')

def print_student_files2(name,gender='男',age='4',school='半山园幼儿园'): 
    #定义时，给出形式参数默认值
    print('我叫' + name)
    print('我是' + gender + '生')
    print('我今年' + age + '岁')
    print('我在' + school + '读书')

print_student_files2('蒋东锦')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
print_student_files2('鸡小萌','女','5') 
print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
print_student_files2('石敢当',age='6') 
#实参与默认参数不同时，可以通过必须参数顺序传递值或关键字参数来传递值

#定义时，非默认参数不能放在默认参数后面，两者不能混杂
#调用时，默认参数和必须参数不能混合


