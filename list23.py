#to add element at the end of list
lis= [1, 8, 2, 9, 5, 6,]
lis.append(7)
print(lis)

#to arrange list in assending order
lis.sort()
print(lis)
lis.sort(reverse=True)
print(lis)
lis.sort(reverse=False)
print(lis)

#to  reverse our list order
lis.reverse()
print(lis)

#to  INDEX our list order
print(lis.index(1))

#to  COUNT the no. of element in our list
lis.count(2)

#to EXTEND our list
m = [234, 333, 999]
lis.extend(m)
print(lis)

#we can do it without disturbing lis also
k=lis+m
print(k)
print(lis)
print(m)