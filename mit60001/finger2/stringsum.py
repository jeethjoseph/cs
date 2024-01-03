s = "1.23,2.4,3.123"
sum = 0
for number in s.split(","):
    sum = sum + float(number)

print(sum)
