

#问题：旅行者从原点出发，每走一段路程，计算与原点的距离。
#比如，先走2步，再走3步，再走6步，每次走完之后与原点的距离。

#用闭包编写(我写的，好像是假的闭包)

origin = 0

def position():
    def travel(step):
        global origin
        pos = origin + step 
        origin = pos
        return pos
    return travel

pos1 = position()
print(pos1(2))
pos2 = position()
print(pos2(3))
pos3 = position()
print(pos3(6))
