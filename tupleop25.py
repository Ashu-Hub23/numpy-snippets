#cant change anything directly but we can do operations in a tuple by converting it into a list and again change it into a tuple. 
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[1] = "Finland"
countries = tuple(temp)
print(countries)


tup = (1 ,2 ,3, 4,3,2,3 ,233,42,24,232)
lis = list(tup)
lis2=[23, 14 ,11,2 ]
lis.extend(lis2)
tup=tuple(lis)
print (tup)

any=tup.count(4)
print(any)
any=tup.index(3)
print(any)
#index(element,start,end)
any=tup.index(3,3,8)
print(any)
print(len(tup))