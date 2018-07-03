
#问题：旅行者从原点出发，每走一段路程，计算与原点的距离。
#比如，先走2步，再走3步，再走6步，每次走完之后与原点的距离。

#用闭包编写，函数式编程。代码大全2

origin = 0

def position(pos):
    def travel(step):
        nonlocal pos  ##闭包环境变量，具有保存现场的功能，记忆住上次调用的状态
        new_pos = pos + step 
        pos = new_pos
        return pos
    return travel

pos = position(origin)
print(pos(2))
print(pos(3))
print(pos(6))