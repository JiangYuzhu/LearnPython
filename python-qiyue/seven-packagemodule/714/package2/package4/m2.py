
m2 = 2
print('~~~~~~~This is m2\'s __package__~~~~~~~')
print(__package__)


from .m3 import m3  #相对（路径）导入

from ..m4 import m

from ...m5 import m5 
##上面相对导入会报错误：
##Attempted relative import beyond top-level package.