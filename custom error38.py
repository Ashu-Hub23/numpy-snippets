d=int(input("enter any integer between 5 and 9: "))
if (d<5 or d>9):
    raise ValueError("your input is not between 5 and 9")

d=input("write anything in string datatype: ")
if (d=="quit"):
    print("no error")
else:
    raise ValueError("wrong input")    