a1= {1 : 11,2: 22,3: 33,4: 44}
a2= { 5 : 55,6: 66}
a1.update(a2)
print(a1)

a1.popitem()
print(a1)

a1.pop(2)
print(a1)

del a1[1]
print(a1)

a1.clear()
print(a1)