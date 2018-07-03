
#问题：旅行者从原点出发，每走一段路程，计算与原点的距离。
#比如，先走2步，再走3步，再走6步，每次走完之后与原点的距离。

#用闭包编写(不正确)

origin = 0

def position(pos):
    def travel(step):
        new_pos = pos + step 
        pos = new_pos
        return pos
    return travel

print(position(2))
print(position(3))
print(position(6))
