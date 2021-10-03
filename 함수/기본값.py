# def profile(name,age,maing_lang):
#     print('이름 : {}\n나이: {}\n사용언어:{}'.format(name,age,maing_lang))

# profile('유',22,'파이썬')
# print('')
# profile('김',21,'자바')

#같은학교 같은학년 같은 반 같은수업 -> 기본값이용

def profile(name,age=15,maing_lang='자바'):
    print('이름 : {}\n나이: {}\n사용언어:{}'.format(name,age,maing_lang))

profile('김')
print('')
profile('박')