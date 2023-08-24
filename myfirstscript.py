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
    # chgange the value of X to get out of the loop


# problem #2
# use a breakpoint in line 14 to debug
mylist = list(range(5)) # range 0 through 4 , the list function creates a list out of the number my list = [ 0, 1,2 ,3 4]

for x in range(1,5):
    print(f"Run No.:{mylist[x]}") # f function allows us to put everyting together and format the way we what it. 

