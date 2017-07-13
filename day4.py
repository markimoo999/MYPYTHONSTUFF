fp = open("usdeclar.txt", "r")
lines = fp.readlines()
for line in lines:
    print (line.strip())
    length = len(line)
    print("this line is " + str(length) + " character(S) long.")