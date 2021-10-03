ex = 'http://naver.com'

#내답
# ex=ex[7:]
# ex=ex[0:5]
# ex=ex[0:3] + str(len(ex)) + str(ex.count('e')) + '!'
# print(ex)

#나도코딩답
my_str = ex.replace('http://','')
# print(my_str)
my_str = my_str[0:my_str.find('.')] #index도가능
# print(my_str)
password = my_str[0:3] + str(len(ex)) + str(ex.count('e'))
# print(password)
print('%s의 비밀번호는 %s입니다!'%(ex,password))