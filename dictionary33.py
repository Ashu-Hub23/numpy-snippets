dic= {"ashu":"legend",
      "vansh":"chudariya",
      "asm":"spak",234:"ashu's roll no. "
     }
print(dic["ashu"])
print(dic["vansh"])

print(dic.get("ashu"))#this will not give error when you give invalid key whereas without "get" if we put invalid key then it show error and does'nt proceed
print(dic) 
print(dic.keys())
print(dic.values())
print(dic.items())

for keys in dic.keys():
    print(f"these are our keys:{keys} with their values {dic[keys]}")

for keys,values in dic.items():
    print(f"these are our keys: {keys} with their values {values}")

# key = input("enter key: ")

# value= dic.get(key)
# if value is not None:
#     print(f"The value for the key '{key}' is: {value}")
# else:
#     print(f"The key '{key}' does not exist in the dictionary.")