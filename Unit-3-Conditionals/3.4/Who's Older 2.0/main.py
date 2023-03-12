import datetime
myBD = input("Enter your birth month, date: ")
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))
userBD = month,day
diff = myBD - userBD
if diff == 0:
    print("We have the same age!")
if diff < 0:
    print("I am older than you.")
if diff > 0:
    print("You are older than me.")
