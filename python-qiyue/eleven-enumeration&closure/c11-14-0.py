
#问题：旅行者从原点出发，每走一段路程，计算与原点的距离。
#比如，先走2步，再走3步，再走6步，每次走完之后与原点的距离。
##逐步演示正确闭包代码

#用非闭包编写（错误代码）

origin = 0

def travel(step):
    pos = origin + step #试图引用全局变量origin，但是报错：局部变量origin没有赋值就引用
    origin = pos
    return pos

pos = travel(2)
pos = travel(3)
pos = travel(6)



