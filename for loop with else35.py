

#while loop with else

i = 0
while i<7:
  print(i)
  i = i + 1
  # if i == 4:
  #   break
  #if we break loop before compeletion of code then it will not go to else part 
else:
  print("Sorry no i")



# for loop with else
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")