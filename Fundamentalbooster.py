print("Welcome to the Interactive Personal Data Collector!")



name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favorite_number = int(input("Please enter your favourite number: "))


print("Thank you! Here is the information we collected:")



print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favourite Number: {favorite_number} (Type: {type(favorite_number)}, Memory Address: {id(favorite_number)})")


birth_year = 2026

print(birth_year - age)
print("Thank you for using the Personal Data Collector. Goodbye!")