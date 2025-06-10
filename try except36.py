#in try except we run a right code then it will run but if our code in wrong then it will not crash it will run except code

def asuu():
  
  x=input("enter the no.")
  try:
   print(f"this is your lucky no.{int(x)}")
   print("square of  your entered no.")
  


   for i in range(int(x)):
    print ((i+1)*(i+1))
    return 1
  except:
   print("invalid input")
   print("Ashu")
   return 0
 #final will always run
  finally:
  #  print("this will always execute")
   print("this will always execute")

x = asuu()
print(x)