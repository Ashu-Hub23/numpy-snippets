import time
def safor():
    i=0
    for i in range(41):
     print(i) 
def sawhile():
    i=-1
    while (i<40):
        i=i+1
        print(i)
srtfor = time.time()        
safor()
print(time.time()-srtfor)
srtwhl = time.time()
sawhile()
print(time.time()-srtwhl)


#we can make our result wait by using time.sleep
print(4)
time.sleep(5)
print(2000)


#we can show local time
t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)
