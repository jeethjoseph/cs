checkInt = int(input("Enter an Integer: "))
pwr = 2
while pwr < 6:
    root = 2
    while root**pwr < abs(checkInt):
        root = root + 1
    if root**pwr == abs(checkInt):
        if checkInt >0:
            print("For Integer",checkInt,". Root =",root,"and Power =",pwr)
            break
        else:
            if pwr % 2 != 0:
                print("For Integer",checkInt,". Root =","-"+str(root),"and Power =",pwr)
                break

    pwr = pwr + 1
if root**pwr != abs(checkInt):
    print("Couldn't find any such sets")

