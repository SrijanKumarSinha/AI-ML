print("ex- 7.1 == Rental Car")

car_name = input("Enter your car name: ")
print(f"\nLet me see if i can find you a {car_name}.")

print("\nex- 7.2 == Restaurant Setting")
people_number = input("How many people are there in their dinner group: ")
people_number = int(people_number)

if people_number > 8:
    print("\nWait for your table")
else:
    print("\nYour table is ready")

print("\nex- 7.3 == Multiples of ten")

print("\tEnter your number to know if it is a multiple of 10 or not\n")
number = input("Enter your number: ")
number = int(number)

if number % 10 == 0:
    print(f"\tThe number {number} is multiple of 10.")
else:
    print(f"\tThe number {number} is not a multiple of 10")

print("\nex- 7.4 == Pizza Toppings")

toppings = "\nEnter your toppings name for your pizza: "
toppings += "\nEnter 'quit' to end the program."

message = " "
while message != 'quit':
    message = input(toppings)
    print(message)

print("\nex- 7.5 == Movie Tickets")

age = input("Enter your age to know your movie ticket price: ")
age = int(age)

if age < 3:
    print("The movie ticket is free")
elif age >= 3 and age <= 12:
    print("The movie ticket price is 10 ruppes only")
else:
    print("The movie ticket price is 15 ruppes only")

print("\nex- 7.6 == Three Exits")

toppings = "\nEnter your toppings name for your pizza: "
toppings += "\n(Enter 'quit' when you are finished.)"

while True:
    toppings_are = input(toppings)

    if toppings_are == 'quit' :
        break
    else:
        print(f"Give more you required.")
    