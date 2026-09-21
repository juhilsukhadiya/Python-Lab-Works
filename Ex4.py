year = 1900

if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("true")
        else:
            print("false")
    else:
        print("true")
else:
     print("false")


#case:-1 4 divide but not devide 100
# case:-2 4,100,400 three are to devide     


#q-2

S = 15
x = int(input("Enter x: "))

if (x % 2 == 0):
    x = x + 1

elif (x < 2):
    x = x + 2

elif (x % 2 != 0):
    x = x + 2

else:

    x = x + 2

if x < S:
    S = S - x

elif x >= S:
    S = S - 1

else:
    S = S - 1

if S == 0:
    print("Output x =", x)

else:
    x = x + 2
    print("Output x =", x)