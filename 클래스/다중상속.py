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
        print('{} : {}방향으로 공격{}을 합니다'.format(self.name,location,self.damage))
    def damaged(self,damage):
        print('{} " {}데미지를 얻었습니다.'.format(self.name,damage))
        self.hp -= damage
        print('{} : 현재체력은 {}입니다.'.format(self.name,self.hp))
        if self.hp <= 0:
            print('{} 유닛이 파괴되었습니다.'.format(self.name))


#  날수있는 기능을 가진 클래스
class Flyalble:
    def __init__(self, flying_speed):
        self.flying_speed =flying_speed

    def fly(self,name,location):
        print('{} : {}방향으로 날아갑니다 속도는 {}'.format(name,location,self.flying_speed))


#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyalble):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,damage)
        Flyalble.__init__(self,flying_speed)


#발키리
valkyrie = FlyableAttackUnit('발키리',200,6,5)
valkyrie.fly(valkyrie.name,'3시')
valkyrie.attack('11시')