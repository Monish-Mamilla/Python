import math
initial = float(input("Enter a number: "))
rate = float(input("Enter rate of growth: "))
numGrowths = float(input("Enter the number of growths: "))
total = initial * pow((1 + rate), numGrowths)
total = round(total, 3)
print(total)
print("---------------------------------")
princ = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate per year as a decimal: "))
rate = rate/100
time = int(input("Enter the number of years the amount will compound for: "))
amount = princ * (math.e ** (rate * time))
amount = round(amount, 2)
print(amount)
