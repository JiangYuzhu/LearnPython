
#字符串，str
#用单引号、双引号、三引号来表示或定义字符串

print('1111')
print("1111")
print('''1111''')
print('"abc"+"1111"')
print("abc"+"1111")
print("Let's go")
print('Let\' go')
print('Let" Go')
#字符串换行方式一:三个单引号。输入可以换行，输出也是换行的。
print('''
hello python
hello python
hello python
''')
#字符串换行方式二:三个双引号。输入可以换行，输出也是换行的。
print("""
hello python
hello python
hello python
""")
#字符串换行方式三:单引号或双引号+\n。输出是换行的。
print('\nhello python\nhello python\nhello python\n')
#字符串换行方式四:\,实现输入换行，输出不换行。
print('hello python\
hello python\
hello python')

#字符ASCII值
print(ord('w'))
print(ord('W'))
#print(ord(''))
