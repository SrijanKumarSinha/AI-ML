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

print("\nex- 7.7 == Infinity Loop")

x = 1
while x <= 5:   
    print(x)
    x += 1   # for infinity loop remove this line and run the code. It will run forever.

print("\nex- 7.8 == Deli")

sandwich_orders = ['veg sandwich', 'non-veg sandwich','tuna sandwich','pastrami','pastrami','pastrami']
finished_sandwiches =[]
while sandwich_orders:
    sandwiches = sandwich_orders.pop()

    print(f"I made your {sandwiches.title()}")
    finished_sandwiches.append(sandwiches)

print("\n---Sandwiches were Made ---")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

print("\nex- 7.9 == No Pastrami")

sandwich_orders = ['veg sandwich', 'non-veg sandwich','tuna sandwich','pastrami','pastrami','pastrami']
finished_sandwiches =[]

print("Sorry, the deli has run out of pastrami today!\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwiches = sandwich_orders.pop()

    print(f"I made your {sandwiches.title()}")
    finished_sandwiches.append(sandwiches)

print("\n---Sandwiches were Made ---")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

print("\nex- 7.10 == Dream Vacation")

responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n ")
print("\t--- Poll Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.\n")

print("\t--- End of the Code ---")



 
 