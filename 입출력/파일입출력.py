# score_file = open('score.txt','w',encoding='utf8')
# print('수학 : 0',file=score_file)
# print('영어 : 100',file=score_file)
# score_file.close()

# score_file = open('score.txt','a',encoding='utf8') #append 이어쓰기
# score_file.write('과학은 80')
# score_file.write('\n영어는 : 10')
# score_file.close()

def a(b):
    for i in b:
        print(i)

a([1,2,3,4,5])