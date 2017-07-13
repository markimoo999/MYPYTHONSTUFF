fp =  open("myfile.txt", "r")
lines = fp.readlines()
addingThings = 0
for line in lines:
    addingThings = addingThings + int(line)
print (addingThings)