NumberOfInputs = 10
largestOddNumber = ''
while NumberOfInputs > 0:
    checkInt = abs(int(input("Enter a Positive Integer: ")))
    if checkInt % 2 == 0:
        print("Number is Even")
    else:
        if largestOddNumber == '':
            largestOddNumber = checkInt
        else:
            if checkInt > largestOddNumber:
                largestOddNumber = checkInt
    NumberOfInputs =  NumberOfInputs - 1

if largestOddNumber == '':
    print("No odd numbers")
else:
    print("Largest odd number is",largestOddNumber)
                    
