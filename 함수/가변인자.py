# def profile(name,age,lang1,lang2,lang3,lang4):
#     print('이름 : {}\t나이: {}\t'.format(name,age), end=" ") #줄바꿈안함
#     print(lang1,lang2,lang3,lang4)
def profile(name,age,*lang):
    print('이름 : {}\t나이: {}\t'.format(name,age), end=" ") #줄바꿈안함
    for a in lang: 
        print(a,end=' ')
    print()


profile('김',22,'a','b','c','d',1,2,3,4,5,'aa')
profile('김태호',22,'aa','bb')