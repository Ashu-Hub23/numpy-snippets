# #set they are unchangeable, no fixed order and its elements does not repeats

# s ={"ashu", 12 ,False,35, 23.5}
# print(s)

# temp = list(s)
# lst=[ 1,2,3,4]
# temp.extend(lst)
# s = set(temp)
# print(s)

# ##this will give you dict not an empty set
# ashu={}
# print(type(ashu))

# #this will give you an empty set
# ashu=set()
# print(type(ashu))

s = {1, 2, 3 ,34.6}
a = {1 ,2, 341}
#print (a.union(s))

s.update(a)
print (s)

p=a.intersection(s)
print(p)



#III. symmetric_difference and symmetric_difference_update():
#The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets.

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)

# #  The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.
 
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.symmetric_difference_update(cities2)
# print(cities)

#disjoint
#The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(cities.isdisjoint(cities2))

#issuperset
a={1,2,3,4,5}
b={1,2,3,4,5}
c={3,4,5}
print(a.issuperset(b))
# a.issuperset(c)
print(a.issuperset(c))