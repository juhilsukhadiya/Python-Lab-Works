day = int(input("enter the day"))


if (day == 1):
    print("monday")

elif (day == 2):
    print("tuesday")

elif (day == 3):
    print("wednesday")   

elif (day == 4):
    print("thrusday") 

elif (day == 5):
    print("friday")    

elif (day == 6):
    print("saturday")    

elif (day == 7):
    print("thrusday")  

else:
    print("in valid date")     

#q-2
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

#q-3

age = int(input("Enter your age: "))

if age <= 12:
    print("Child")
else:
    if age <= 19:
        print("Teenager")
    else:
        if age <= 59:
            print("Adult")
        else:
            print("Senior")

#q-4  

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


#q-5

num = int(input("Enter a number: "))

if num == 0:
    print("The number is Neutral")
elif num > 0:
    print("The number is Positive")
else:
    print("The number is Negative")