#python对于函数返回结果的类型没有要求(动态)

#如何让函数返回多个结果
# R Skill1,Skill2
def damage(skill1,skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 3 + 10
    return damage1,damage2
damages = damage(3,6)

print(type(damages)) #函数返回多个值，python自动组成Tuple
print(damages)
print(damages[0],damages[1]) #使用序号将导致代码不易于阅读，不明白damage[0]代表什么
#序列解包
skill1_damage,skill2_damage = damage(3,6) #使用具有实际意义的变量来接收函数返回的多个值
print(skill1_damage,skill2_damage)

