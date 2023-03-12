num = int(input("Enter a 2-Digit Number that is divisible by 5 or 10: "))
check1 = 9 < num < 100
check2 = num % 5 == 0 or num % 10 == 0
if check1 and check2:
    print("SUCCESS!")
else:
    print("FAILURE")

