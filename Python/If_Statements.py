print("ex-5.1 == Condititonal Tests\n")
#1
car = 'bmw'
print("Is car == 'bmw' ? I predict True.")
print(car == 'bmw')

print("Is car == 'mercedes' ? I predict False.")
print(car == 'mercedes')
#2
car = 'audi'
print("\nIs car == 'audi' ? I predict True.")
print(car == 'audi')

print("Is car == 'toyota' ? I predict False")
print(car == 'toyota')
#3
number = 2
print("\nIs number == 2 ? I predict True.")
print(number == 2)

print("Is number == 3 ? I predict False.")
print(number == 3)
#4
strongest_avengers = 'Thor'
print("\nIs strongest_avenger == 'Thor' ? I predict True.")
print(strongest_avengers == 'Thor')

print("Is strongest_avengers == 'Hawkeye' ? I predict False.")
print(strongest_avengers == 'Hawkeye')
#5
number = 7
print("\nIs number == 7 ? I predict True.")
print(number == 7)

print("Is number == 8 ? I predict False.")
print(number == 8)

print("\nex-5.2 == More Conditional Tests")

number = 7

if number == 7:
    print("True")
 

list = ['bmw','toyota','subaru','mercedes']

if 'bmw' in list:
    print("Item is in the list..")
elif 'tata' in list:
    print("Item is not in the list")

print("\nex-5.3 == Alien Colour #1")

alien_colour = 'green'
if alien_colour is 'green':
    print("You earned 5 points")
else:
    print("Earned 0 points")

print("\nex-5.4 == Alien Colour #2")
alien_colour = 'green'
if alien_colour is 'green':
    print("You just earned 5 points for shooting the alien.")
else:
    print("Player just earned 10 points.")

print("\n#2")
alien_colour = 'red'
if alien_colour is 'green':
    print("You just earned 5 points for shooting the alien.")
else:
    print("Player just earned 10 points.")

print("\nex-5.5 == Alien Colors #3") # 3 versions for if, elif and else statements

alien_colour = 'green' # for if statements

if alien_colour is 'green':
    print("Player earned 5 points")
elif alien_colour is 'yellow':
    print("Player earned 10 points")
else:
    print("Player earned 20 points")

alien_colour = 'yellow' # for elif statement

if alien_colour is 'green':
    print("Player earned 5 points")
elif alien_colour is 'yellow':
    print("Player earned 10 points")
else:
    print("Player earned 20 points")

alien_colour = 'red' # for else statement

if alien_colour is 'green':
    print("Player earned 5 points")
elif alien_colour is 'yellow':
    print("Player earned 10 points")
else:
    print("Player earned 20 points")

print("\nex-5.6 == Stages of life")

age = 25

if age < 2 :
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")


print("\nex-5.7 == Favourite foods")

favorite_fruits = ['mango','apple','guava']

if 'mango' in favorite_fruits:
    print(f"I like {favorite_fruits[0]}")
elif 'apple' in favorite_fruits:
    print(f"I like {favorite_fruits[1]}")
elif 'guava' in favorite_fruits:
    print(f"I like {favorite_fruits[2]}")
elif 'pineapple' in favorite_fruits:
    print("Item not found")
elif "orange" in favorite_fruits:
    print("Item is not found")

print("\nex-5.8 == Hello Admin")

usernames = ['admin01','admin02','admin03','admin04','admin05']
for username in usernames:
    print(f"Hello {username.title()} , Thankyou for logging in again")

print("\nex-5.9 == No users")
usernames = []
for username in usernames:
    print(username)
print("We need to find some users")

print("\nex-5.10 == Checking Username")

current_users = ['angela','lena','sunny','jhonny','sarah','ANGELA','LENA','SUNNY','JHONNY','SARAH'] #will be reviewed 
new_users = ['angela','lisa','mike','jhonny','sarah','ANGELA','LISA','MIKE','JHONNY','SARAH']
 
for new_user in new_users:
    if new_user in current_users:
        print(f"Username '{new_user}' is already taken. Please choose a different username.")
    else:
        print(f"Username '{new_user}' is available.")

print("\nex-5.11 == Ordinal Numbers")

numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

print("\n--- End Of The Code ---")