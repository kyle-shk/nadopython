class Unit():
    def __init__(self,name,hp,damage): # __init__은 생성자
        self.name = name
        self.hp = hp
        self.damage = damage
        print('{} 유닛이 생성되었습니다'.format(self.name))
        print('체력은 {}이고 공격력은 {}이다'.format(self.hp,self.damage))

marine1 = Unit('마린',30,150)
tank1 = Unit('탱크',70,110)

#__init__에 해당된 파라미터를 전부보내야 객체를만들수있음!!!