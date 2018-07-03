
#入口文件与普通模块内置变量的区别

import t.c11_2

print('package:'+(__package__ or '当前模块不属于任何包'))
print('name:'+__name__)
print('file:'+__file__)
print('doc:'+__doc__)  