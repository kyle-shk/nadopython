class Unit():
    def __init__(self,name,hp,damage): # __init__은 생성자
        self.name = name # self.?? 가 맴버변수
        self.hp = hp
        self.damage = damage
        print('{} 유닛이 생성되었습니다'.format(self.name))
        print('체력은 {}이고 공격력은 {}이다'.format(self.hp,self.damage))

# marine1 = Unit('마린',30,150)
# tank1 = Unit('탱크',70,110)

wraith1 = Unit('레이스',80,5)
print('유닛이름은 {}이고 공격력은 {}이다.'.format(wraith1.name,wraith1.damage))

# 마인드컨트롤된 레이스
wraith2 = Unit('레이스',80,5)
wraith2.clocking = True #객체에 추가로 속성할당, class할당!!!
print('')
print(wraith2.name,wraith2.damage,wraith2.clocking)
if wraith2.clocking == True:
    print('{}는 현재 클로킹된 상태입니다.'.format(wraith2.name))

    