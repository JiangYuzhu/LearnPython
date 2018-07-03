
#列表的可变与元组的不可变

# #####列表的可变
# >>> a = [1,2,3]
# >>> hex(id(a))
# '0x4ea0e40'
# >>> hex(id([1,2,3]))
# '0x4ea0b70'
# >>> a.append(4)
# >>> hex(id(a))
# '0x4ea0e40'
# >>> hex(id([1,2,3,4]))
# '0x4ea0b70'
# >>> a[0] = '1'
# >>> hex(id(a))
# '0x4ea0e40'
# >>> hex(id(['1',2,3,4]))
# '0x4ea0b70'
# >>>
# ######元组的不可变
# >>> a = (1,2,3)
# >>> a.append(4)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'tuple' object has no attribute 'append'
# >>> a[0] = '1'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# >>> hex(id(a))
# '0x4e06030'
# >>> hex(id(1,2,3))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: id() takes exactly one argument (3 given)
# >>> hex(id((1,2,3)))
# '0x4e060d0'
# >>>

####
# >>> a = (1,2,3,['a','b','c'])
# >>> a[1]
# 2
# >>> a[3][1]
# 'b'
# >>> a[3][1] = 'd'
# >>> a[3][1]
# 'd'
# >>> a
# (1, 2, 3, ['a', 'd', 'c'])
# >>> hex(id(a))
# '0x4f3d2a0'
# >>> hex(id(a[0]))
# '0x5825d430'
# >>> hex(id(a[1]))
# '0x5825d440'
# >>> hex(id((1,2,3,['a','d','c'])[0]))
# '0x5825d430'
# >>> hex(id((1,2,3,['a','d','c'])))
# '0x4fa91e0'
# >>> hex(id(a[3][1]))
# '0x4e5c980'
# >>> hex(id(a[3][2]))
# '0x4e5c660'