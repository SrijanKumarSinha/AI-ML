print("\nex-4.1 == Pizzas\n")

favourite_food = ['Samosa','Bhujia','Kachodi']
for food in favourite_food:
    print(f"I like {food.title()}")
print(f"I like {favourite_food[0]},{favourite_food[1]},{favourite_food[2]}")
print("I love these foods")

print("\nex-4.2 == Animals\n")

animals = ['Lion','Tiger','Wolf']
for animal in animals:
    print(animal)
print(f"{animals[0]} is the king of the jungle.")
print(f"{animals[1]} is the national animal of india.")
print(f"{animals[2]} is a clever animal.")

print("\nAll the animals are carnivorous\n")

print("\nex-4.3 == Counting To Twenty\n")

for value in range(1,21):
    print(value)

print("\nex-4.4 == One Million , code commeted\n")

#numbers = list(range(1,1000001))
#print(numbers)

print("\nex-4.5 == Summing a Million , code commented\n")

#number = list(range(1,1000001,1))
#print(number)
#max(number)
#min(number)
#sum(number)
 
print("\nex-4.6 == Odd Numbers\n")

odd_numbers = list(range(1,21,2))
print(odd_numbers)

print("\nex-4.7 == Threes\n")

threes = list(range(3,31,3))
print(threes)

print("\nex-4.8 == Cubes\n")

cube = []
for value in range(1,11):
    cube.append(value**3)
print(cube)

print("\nex-4.9 == Cube Comprehension\n")

print("Refer to ex - 4.8")

print("\nex-4.10 == Slices\n")

cars = ['mercedes','rolls royce','bmw','volkswagen','jeep','tata','mahindra','bugati','land rover']
print("The first three item in the list are:")
print(cars[0:3])

print("Three items from the middle of the list are:")
print(cars[3:6])

print("The last three item in the list are:")
print(cars[6:])

print("\nex-4.11 == My Pizzas,Your Pizzas\n")

whole_food = ['Samosa','Bhujia','Kachodi']

favourite_food = ['Samosa','Bhujia','Kachodi']

favourite_food.append("Gup-Chup")

whole_food.append("Samosa chaat")

print(f"My favourite food is :")

for food in favourite_food:
    print(favourite_food[0:4])
 
    

print(f"The whole food list is : {whole_food}")

for food in whole_food:
    print(whole_food[0])
    print(whole_food[1])
    print(whole_food[2])
    print(whole_food[3])
     


 