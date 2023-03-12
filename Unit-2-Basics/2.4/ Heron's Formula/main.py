import math
print ("note: a+b>c and a+c>b")
a = int (input("Enter A: "))
b = int (input("Enter B: "))
c = int (input("Enter C: "))
s = (a + b + c) / 2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
area = round (area, 3)
print ("a = " + str(a) + "\n" + "b = " + str(b) + "\n" + "c = " + str(c) + "\n" + "area = " + str(area))
s = round (s,2)
print (s)
