from random import *

# 승객이용시간 = randint(5,50)
# 소요시간 = randint(5,15)

print('출력문예제')
i = 1
count = 0
while i <= 50:
    if randint(5,51) <= randint(5,15):
        print('[o] {}번째 손님 (소요시간 : {}분)'.format(i,randint(5,15)))
        i += 1
        count += 1
    elif randint(5,51) > randint(5,15):
          print('[] {}번째 손님 (소요시간 : {}분)'.format(i,randint(5,51)))
          i += 1
print('')
print('총 탑승 승객 : {}'.format(count))