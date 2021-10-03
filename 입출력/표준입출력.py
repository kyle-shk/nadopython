# print('python','java',sep=',',end=' ') # sep 는 , 뭘넣을지 정하고 end 는 문장마지막에 어떻게할지 정함
# print('뭐가더 재밌음?')

# import sys
# print('python','java',file=sys.stdout) #표준출력
# print('python','java',file=sys.stderr) #표준에러


#시험성적
# score = {'수학':0,'영어':90,'코딩':100}
# for subject,score in score.items():
#     print(subject.ljust(8),str(score).rjust(4), sep=':') #왼쪽으로 정렬하는데 8칸이 확보된 상태로 정렬해라



# 대기 순번표
#001, 002, 003 ................
# for num in range(1,21):
#     print('대기번호 : {}'.format(str(num).zfill(3))) #크기3 만큼확보하고 값이 없는공간은 0으로 채움


#표준입력
# answer = input('아무값이나 입력하시오: ') # 출력타입은 string
# print(answer)

for i in range(1):
    print(i)