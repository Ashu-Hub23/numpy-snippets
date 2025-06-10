i= [1,2,3, "harry","Ashu",True ]
print (i)
print (type(i))
print (i[0])
print (i[1])
print (i[2])
print (i[3])
print (i[4])
print (i[5])

print("negative indexing")
i= [1, 2, 3 , "harry","Ashu",True,"asd","esdf", "afbf" ]

print (i[-1])
print (i[-2])
print (i[-3])
print (i[-4])
print (i[-5])
print (i[-6])
print (i[len(i)-3])

if 2 in i :
  print ("2 is in i")
else:
  print("2 is not in i")
#print(list[start:end:jump index])
print (i[1:5])
print (i[1:5:2])

i= [1,2,3, "harry","Ashu",True ]
print (i)
print (type(i))
print (i[0])
print (i[1])
print (i[2])
print (i[3])
print (i[4])
print (i[5])

print("negative indexing")
i= [1, 2, 3 , "harry","Ashu",True,"asd","esdf", "afbf" ]

print (i[-1])
print (i[-2])
print (i[-3])
print (i[-4])
print (i[-5])
print (i[-6])
print (i[len(i)-3])

if 2 in i :
  print ("2 is in i")
else:
  print("2 is not in i")
#print(list[start:end:jump index])
print (i[1:5])
print (i[1:5:2])

#list comprehension

lst=[i*i for i in range(11)]
print(lst)
lst=[i*i for i in range(11) if i%2==0]
print(lst)



