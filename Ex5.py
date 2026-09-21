a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a>b :
    if a>c:
        maximum =a
    else:
        maximum = c

else:
    if b>c:
        maximum =b
    else:
        maximum = c  
    print("maxium number =",maximum)      


#q-2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b:
    if a < c:
        minimum = a
    else:
        minimum = c
else:
    if b < c:
        minimum = b
    else:
        minimum = c

print("Minimum number =", minimum)

#q-3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a > b:
    if a > c:
        if a > d:
            maximum = a
        else:
            maximum = d
    else:
        if c > d:
            maximum = c
        else:
            maximum = d
else:
    if b > c:
        if b > d:
            maximum = b
        else:
            maximum = d
    else:
        if c > d:
            maximum = c
        else:
            maximum = d

print("Maximum number =", maximum)


