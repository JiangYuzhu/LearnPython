
##__init__.py 的用法
# (1).使用型号导入时，限制包中可以被导出的模块:__all__ = ['c7',"c9"]
# (2).当有多个模块需要导入相同的模块/库时，可以将这些模块/库放在__init__.py中进行导入；
# 简化批量导入

#代码换行
from  t.c9 import a,b,\
c
print(a,b,c)
from t.c9 import (d,e,
f)
print(d,e,f) 

