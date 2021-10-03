# def std_weight(height,gender):
#     if(gender == '남자'):
#         weight = height * height * 22
#         weight = round(weight,2)
#         print('키 {}cm 남자의 표준 체중은 {}kg입니다.'.format(height,weight))
#     else:
#         weight = height * height * 21
#         weight = round(weight,2)
#         print('키 {}cm 여자의 표준 체중은 {}kg입니다.'.format(height,weight))

# std_weight(1.75,'남자')
# std_weight(1.65,'여자')


# def std_weight(height,gender):
#     if(gender == '남자'):
#         return height * height * 22
#     else:
#         return  height * height * 21
  

# height = 175
# gender = '남자'
# weight = std_weight(height/100,gender)
# print('키 {}cm {}의 표준 체중은 {}kg 입니다.'.format(height,gender,round(weight,2)))

def a(a):
    print(a*a)

print(a(3)) # return 값이 없으면 none