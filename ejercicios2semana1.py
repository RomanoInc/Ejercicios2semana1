#Menor de tres numeros
a = int(input("Join 1 number: "))
b = int(input("Join 2 number: "))
c = int(input("Join 3 number: "))

if a < b and b < c:
    print("minor number is: ", a)
elif b < c:
    print("minor numer is: ", b)
else:
    print("minor number is:", c)
