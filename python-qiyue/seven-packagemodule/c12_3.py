
#入口文件与普通模内置变量的区别
#区分入口文件和普通模块

import t.c12_2

print('~~~~~~~~~~~~~~~~C12_3~~~~~~~~~~~~~~~~~~')
print('package: '+(__package__ or '当前模块不属于任何包'))
print('name: '+__name__)
print('file: '+__file__)
print('doc: '+(__doc__ or '当前模块没有注释信息')) 

print('~~~~~~~~查看本入口文件有哪些内置变量~~~~~~~~~')
print(dir())