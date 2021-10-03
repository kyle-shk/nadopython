# 마린
# name = '마린'
# hp = 40
# damage = 5

# print('{}유닛이 생성되었습니다'.format(name))
# print('체력은 {}, 공격력은 {}입니다'.format(hp,damage))

# tank_name = '탱크'
# tank_hp = 150
# tank_damage = 35
# print('')
# print('{}유닛이 생성되었습니다'.format(tank_name))
# print('체력은 {}, 공격력은 {}입니다'.format(tank_hp,tank_damage))
# print('')
# def attack(name,location,damage):
#     print('{0} : {1}방향으로 적군의 공격합니다 공격력은 {2}입니다'.format(name,location,damage))

# attack(name,'1시',damage)
# attack(tank_name,'1시',tank_damage)

# 문제는 이렇게 새로운 내용이생길때마다 반복적으로 만드는것이 매우 비효율적임 그래서 생긴게 class임

class Unit():
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print('{} 유닛이 생성되었습니다'.format(self.name))
        print('체력은 {}이고 공격력은 {}이다'.format(self.hp,self.damage))

marine1 = Unit('마린',30,150)
tank1 = Unit('탱크',70,110)