
#问题：旅行者从原点出发，每走一段路程，计算与原点的距离。
#比如，先走2步，再走3步，再走6步，每次走完之后与原点的距离。

#用非闭包编写(正确代码)

origin = 0

def travel(step):
    global origin
    pos = origin + step 
    origin = pos
    return pos

print(travel(2))
print(travel(3))
print(travel(6))
