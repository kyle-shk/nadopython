absent = [2,5] #결석
nobook = [7] # 책을 까먹음
for student in range(1,10):
    if student in absent:
        continue
    elif student in nobook:
        print('{}번 뒤질래? '.format(student))
        break
    print('{}, 책을읽으렴'.format(student))

