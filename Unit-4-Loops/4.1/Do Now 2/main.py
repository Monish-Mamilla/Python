numIterations = int(input("How many times do you want to run the loop? "))
sum = difference = 0
product = quotient = 1
for x in range(1, numIterations + 1):
    sum += x
    product *= x
    difference -= x
    quotient /= (x+1)
    if sum > 100 or product > 100 or difference > 100 or quotient > 100:
        break
print("Sum: {}"
      "\nProduct: {}"
      "\n Difference: {}"
      "\nQuotient: {}".format(sum, product, difference, quotient))
