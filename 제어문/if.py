# weather = input('날씨어떄? ') #string형태로 나옴

# if 조건:
#     실행명령문

# if weather=='비' or weather =='눈':
#     print('우산챙겨요')
# elif weather=='미세먼지':
#     print('마스크챙겨')
# else:
#     print('걍 ㄱ')


temp = int(input('날씨 어때 ? '))

if 30 <= temp:
    print('나가지마')
elif 10 <= temp and temp < 30:
    print('좋음')
elif 0 <= temp and temp < 10:
    print('추움')
else:
    print('패딩 ㄱ')