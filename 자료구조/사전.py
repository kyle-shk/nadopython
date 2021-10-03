cabinet = {3:'유',100:'조'}

print(cabinet[3])
print(cabinet[100])
print(cabinet.get(100))
print(cabinet.get(5),'값이없음')


print(3 in cabinet)
print(5 in cabinet)

cabinet = {'a-1':'유','b-1':'조'}
print(cabinet['a-1'])
print(cabinet['b-1'])
#새손님
cabinet['a-1']='김'
print(cabinet['a-1'])
#간손님
del cabinet['a-1']
print(cabinet)

#keys 들만 출력
print(cabinet.keys())
#value 만출력
print(cabinet.values())
#key,value 쌍으로 출력
print(cabinet.items())
#목욕탕 폐점
cabinet.clear()
print(cabinet)