# customer = '토르'
# index =5

# while index >= 1:
#     print('{}님 커피가 준비되었습니다. {}번남았습니다'.format(customer,index))
#     index -=1
#     if index ==0:
#         print('커피는 폐기처분됐습니다')

customer = '토르'
person = 'Unknown'

while person != customer:
    print('{}님 커피가 나왔습니다'.format(customer))
    person = input('성함이 어떻게되십니까? ')