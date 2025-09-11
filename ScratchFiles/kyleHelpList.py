#User will enter any integer save it in a variable x
#Print out all numbers from 1- 1000
#But make a new line if x number of integers have been printed out
#use only one loop

x = int(input("Enter an Integer: "))
if x < 10 or x > 30:
    x = int(input("Enter an Integer: "))
lineLength = 0
num = 1
line = ""
while num <= 1000:
    if lineLength == 0:
        print(line)
        line = ""
        line += str(num) + " "
        lineLength += 1
        num += 1
    elif lineLength < x and lineLength != 0:
        line += str(num) + " "
        lineLength += 1
        num += 1
    elif lineLength >= x:
        lineLength = 0
print(line)
    
