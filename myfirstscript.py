# problem #1
# What is mising in the while loop?
# use a breakpoint in line 6 to debug
x = 1
while x < 10:
    print(x)
    x += 1   
#will continually run and show 1 as a loop. We need to close the loop that is showcasing. 
#this is is a continuous loop, we need the close the loop. 
#you put the breakpoint in the problem area line. Before the error shows up. 
#run and debug and press the continue button to test each line.
#change the value of X to get out of the loop
#the while loop will run as long as the condition 'x < 10' is TRUE. 
#the current value of x is printed in the print()
#During the first iteration, "x" is 1, so 1 will be printed. 
#the loop goes through 1 to 9 as X becomes ten the value becomes false. 


# problem #2
# use a breakpoint in line 14 to debug
mylist = list(range(5)) # range 0 through 4 , the list function creates a list out of the number my list = [ 0, 1, 2, 3, 4]
#range(5) is from 0 1 2 3 4. 5 integers starting at 0. 
#list() you converted them to a list format, why ? Because we can access individual items in lists and not ranges. 
#we store these values a variable called my list. 

for x in range(1,5): #picks up at 1 and does not include 5 because it stops at 4. Range goes up unto the last digit. 
    print(f"Run No.:{mylist[x]}") # f function allows us to put everyting together and format the way we what it. 
# the f-string allows us to put special placeholders where we will later put in values. 
#the curly brackets is where you can put in values, we putting the list in their. 
#the list in mylist equals 0 1 2 3 4. 


thelist = list(range(7))
for b in range(1,7): #ask why is it printing 4 over and over. It is because it is in the previous loop. Do i need to close the previous loop somehow. 
    print(f"The answer is:{thelist[b]}") # need it to update to B!
