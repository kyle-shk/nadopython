# # 일반 유닛
# class Unit():
#     def __init__(self,name,hp,damage): # __init__은 생성자
#         self.name = name # self.?? 가 맴버변수
#         self.hp = hp
#         # self.damage = damage
#         # print('{} 유닛이 생성되었습니다'.format(self.name))
#         # print('체력은 {}이고 공격력은 {}이다'.format(self.hp,self.damage))
# # 공격유닛
# class AttackUnit(Unit):
#     def __init__(self,name,hp,damage):
#         self.name = name # self.?? 가 맴버변수
#         self.hp = hp
#         self.damage = damage
#     def attack(self,location):
#         print('{} : {}방향으로 공격을 합니다'.format(self.name,location,self.damage))
#     def damaged(self,damage):
#         print('{} " {}데미지를 얻었습니다.'.format(self.name,damage))
#         self.hp -= damage
#         print('{} : 현재체력은 {}입니다.'.format(self.name,self.hp))
#         if self.hp <= 0:
#             print('{} 유닛이 파괴되었습니다.'.format(self.name))

# 공격유닛을 만들때 일반유닛과 겹치는부분은 상속받아서 없애자

# 일반 유닛
class Unit():
    def __init__(self,name,hp): # __init__은 생성자
        self.name = name # self.?? 가 맴버변수
        self.hp = hp
# 공격유닛
class AttackUnit(Unit):
    def __init__(self,name,hp,damage):
        Unit.__init__(self,name,hp)
        # self.name = name # self.?? 가 맴버변수
        # self.hp = hp
        self.damage = damage
    def attack(self,location):
        print('{} : {}방향으로 공격을 합니다'.format(self.name,location,self.damage))
    def damaged(self,damage):
        print('{} " {}데미지를 얻었습니다.'.format(self.name,damage))
        self.hp -= damage
        print('{} : 현재체력은 {}입니다.'.format(self.name,self.hp))
        if self.hp <= 0:
            print('{} 유닛이 파괴되었습니다.'.format(self.name))


firebat = AttackUnit('파이어뱃',50,20)
firebat.attack('5시')

# 공격 2번 받는다고 가정
firebat.damaged(20)
firebat.damaged(30)