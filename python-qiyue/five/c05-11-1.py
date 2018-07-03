
a = [1,2,3]
b = a
print(id(a),id(b),id([1,2,3]))
print(a is b)
print(a == b)

[1,2,3].append(4)
print(id(a),id(b),id([1,2,3,4]))
print(a is b)
print(a == b)

[1,2,3].insert(0,0)
print(id(a),id(b),id([0,1,2,3,4]))
print(a is b)
print(a == b)

a.append(5)
print(id(a),id(b),id([1,2,3,4,5]))
print(a is b)
print(a == b)

# 上段代码块执行结果（分步执行）：
# PS C:\python-files\five> python c05-11.py
# 1370149936 1370149936 1370149936
# True
# True
# 1370149952 1370149952 1370149952
# True
# True
# PS C:\python-files\five> python c05-11.py
# 1370149936 1370149936 1370149936
# True
# True
# 1370149952 1370149952 1370149952
# True
# True
# 79891472 79891472 79891512
# True
# True
# 79891472 79891472 79891512
# True
# True
# PS C:\python-files\five> python c05-11.py
# 1370149936 1370149936 1370149936
# True
# True
# 1370149952 1370149952 1370149952
# True
# True
# 86772752 86772752 86772792
# True
# True
# 86772752 86772752 86772792
# True
# True
# 86772752 86772752 86772792
# True
# True
# PS C:\python-files\five> python c05-11.py
# 1370149936 1370149936 1370149936
# True
# True
# 1370149952 1370149952 1370149952
# True
# True
# 93522960 93522960 93523000
# True
# True
# 93522960 93522960 93523000
# True
# True
# 93522960 93522960 93523000
# True
# True
# 93522960 93522960 93523000
# True
# True
# PS C:\python-files\five>