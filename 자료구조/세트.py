#중복안되고 , 순서가없음!

my_set = {1,2,3,3,3,3}
print(my_set)

java = {'유','김','양'}
python = set(['유','박'])

#교집합
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합 자바는할수있지만 파이썬은 못하는개발자
print(java-python)
print(java.difference(python))

#python 할줄아는사람늘어남
python.add('태호')
print(python)

#java 까먹음
java.remove('김')
print(java)