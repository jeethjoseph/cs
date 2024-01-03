number = float(input("Enter the Number you want Square Root for :"))
epsilon = float(input("Epsilon for approximation :"))
guess = number/2.0
numguesses = 0
while abs(guess*guess - number) > epsilon:
    guess = guess - ((guess*guess - number)/(2*guess))
    numguesses = numguesses + 1
    print(numguesses)
    print(guess)
print (guess, "is a good approximation for square root of",number)
