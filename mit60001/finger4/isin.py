def isin(stringA, stringB):
    if stringA in stringB or stringB in stringA:
        return True
    else:
        return False


print(isin("Hello", "Hello World"))
print(isin("Burger King","Burger"))
print(isin("jack","Jack Fruit"))
print(isin("Dollars","Rupees"))
