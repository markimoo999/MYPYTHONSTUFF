fp = open("players.csv", "r")
lines = fp.readlines()
for line in lines:
    liner = line.strip()
    y = line.split(",")
    print("this person's age is " + y[2] + ", and their name is " + y[1] + " " + y[0] + ", and their favorite color is " + y[3])
#leedleedleedleedleedleedleedleedleedleedleedl
