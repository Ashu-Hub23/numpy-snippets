#string formatting which was used in old python
letter="hey my name is {} and I am from {}"
country = "India"
name = "Assu"

print (letter.format(country,name))
#here problem is that if we make more string we will get confuse while checking which no. refers to which string for such problem new f-string is introduced
letter=f"hey my name is {name} and I am from {country}"
country = "India"
name = "Assu"

print (letter.format())


#to get calulation answer in string 
print(type(f"{3*4}"))