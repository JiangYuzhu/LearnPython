#枚举其实是一个类

from enum import Enum

class Demo(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

print(Demo.YELLOW)