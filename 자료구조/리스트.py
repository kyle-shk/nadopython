# 리스트 []

#지하철 칸별로 10,20,30

# subway = [10,20,30]
# print(subway)

# subway = ['유','돈','노']
# print(subway)

# #돈은 몇번쨰 칸?
# print(subway.index('돈'))

# #하 가 다음정류장에 탑승
# subway.append('하')
# print(subway)

# #정을 유 와 돈 사이에 태움
# subway.insert(1,'정')
# print(subway)

# #한명씩 하차
# print(subway.pop())
# print(subway)
# print('')
# print('')
# # print(subway.pop())
# # print(subway)
# # print(subway.pop())
# # print(subway)

# #같은 이름의 사람 몇명인지 확인
# subway.append('유')
# print(subway)
# print(subway.count('유'))
# print('')
# print('')
# print('')
# #정렬도 가능
# list = [5,3,1,2,6]
# list.sort()
# print(list)
# #순서 뒤집기도 가능
# list.reverse()
# print(list)

# #모든값지우기
# list.clear()
# print(list)

# 다양한 자료형과 함께 사용

list = [1,'a',True]
last = [2,'aa',False]

#리스트확장
list.extend(list)
print(list)