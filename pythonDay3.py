import time
a = input("first name here\n")
b = input("middle name here\n")
c = input("last name here\n")
abc = a + " " + b + " " + c
length = len(abc)
lastLocation = abc.index(c)
countingE = abc.count("e")
countingA = abc.count("a")
print( "your full name is " + abc +", and the length of your name is", length,"letters long, and the letter in the middle is "+ abc[length/2]+ ", and your last name is placed here in the code: " + str(lastLocation) + ", and your name has this many e's: " + str(countingE) + ", and this many a's: " + str(countingA) + ".")
time.sleep(3)
for x in range(0 , length):
    print (abc[x] + "\n")
