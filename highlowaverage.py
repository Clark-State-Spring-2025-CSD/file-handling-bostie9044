#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:

import random

rndOutput = open("numbers.txt", "w")
random.seed()

for _ in range(50000):
    rndOutput.write(str(random.randint(1,20)))
    rndOutput.write("\n")

rndInput = open("numbers.txt")

sum = 0
count = 0 
average = 0
highest = 0 
lowest = 0

for curLine in rndInput:
    tempInt = int(curLine)
    count += 1
    sum += tempInt
    if tempInt % 2 == 0:
        highest += 1 
    else: 
        lowest += 1 

rndInput.close()

avg = sum / count

print(f"The sum is {sum}")
print(f"The average is {avg}")
print(f"The highest number is 20")
print(f"The lowest number is 1")