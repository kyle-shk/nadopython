python = 'python is very good!'
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python[0].islower())
print(len(python))
print(python.replace('python','Java'))


index = python.index('i')
print(index)
index = python.index('d',index+1)
print(index)

print(python.find('g'))
print(python.find('java')) #없으면 -1
# print(python.index('java')) # 실행이안됨
print(python.count('o'))