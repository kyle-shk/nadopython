gun = 30

def checkpoint(soldiers):
#     gun = 20
    global gun # 전역공간에 있는 gun 사용
    gun -= soldiers
    print('[함수내] 남은총 갯수 : {}'.format(gun))

    
def checkpoint_ret(gun,soldiers):
    gun -= soldiers
    print('[함수내] 남은총수 {}'.format(gun))
    return gun



print('전체총수 : {}'.format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun,2)
print('남은총수 : {}'.format(gun))