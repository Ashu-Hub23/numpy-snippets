#factoial


x = int(input("enter your no. to find factorial: "))
def factorial(x):
 if (x==0 or x==1):
  return 1
 else :
   return x * factorial(x-1)
print(factorial(x))

#fabonacci

f = int(input("enter your no. to find fibonacci series: "))
def fibo(f):
 if (f==0):
  return 0
 elif (f==1):
  return 1
 else :
  return fibo(f-1)+fibo(f-2)

for f in range(0,f+1):
 print(fibo(f))