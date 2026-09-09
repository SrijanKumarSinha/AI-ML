print("ex-3.1 == Names:" )

names = ['Tony Stark','Natasha Romanoff','Steve Rogers','Bruce Banner','Thor','Clint Barton']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])

print("\nex-3.2 == Greetings:")

message = "Well Done Avenger,"

print(f"{message}{names[0]} !")
print(f"{message}{names[1]} !")
print(f"{message}{names[2]} !")
print(f"{message}{names[3]} !")
print(f"{message}{names[4]} !")
print(f"{message}{names[5]} !")

print("\nex-3.3 == Your Own List:")

Vehicles = ['Rolls Royce Phantom','Mercedes G-wagon','Jeep Wrangler','Harley Davidson Fatbob','Yamaha RX 100','Royal Enfield Himalayan','Hero Honda Splender','Land Rover Defender']
message = "I will own a "
print(f"{message}{Vehicles}")

print("\nex-3.4 == Guest List")

Guests = ['Shree Narendra Modi','Robert Downey Jr.','Mahendra Singh Dhoni','Akshay Kumar','Scarlett Johansson']
print(f"You are doing so much of hardwork for our country let's have a talk on more technology developmment , Please Come to Dinner Tonight , {Guests[0]}")
print(f"You are my favourite Hollywood Actor and favourite avenger please join me at dinner tonight, Mr. {Guests[1]}")
print(f"You are my favourite Cricketer lets talk more on cricket at dinner time, Mr. {Guests[2]}")
print(f"You are my favourite bollywood actor , an action super star come tonight to have a dinner, Mr. {Guests[3]}")
print(f"You are my favourite actress in hollywood ,come let's have a dinner tonight with me , My Favourite {Guests[4]}")

print("\nex-3.5 == Changing Guest List")

print(f"Unfortunately {Guests[3]} is unavailable because of his busy schedule")

Guests[3] = 'Elon Musk'

for Guest in Guests:
    print(f"Dear {Guest}, you are cordially invited to dinner.")

print("\nex-3.6 == More Guests")

print("Great news! I found a bigger dinner table, so more guests can join us. \n")

Guests.insert(0, 'Shree Atal Bihari Vajpaye')

middle_index = len(Guests)//2

Guests.insert(middle_index, 'Shree Yogi Aditya Nath ')

Guests.append('Monica Belluci')

for Guest in Guests:
    print(f"Dear {Guest}, please join us for dinner tonight.")
 

print("\nex-3.7 == Shrinkking Guest List")

print("Sorry everyone, the new table won't arrive in time , so I can only invite two people for dinner.\n")

while len(Guests) > 2:
    removed_Guest = Guests.pop()
    print(f"Dear {removed_Guest}, I am really sorry, but I can't invite you to dinner.")

print("\n--- Remaining Guests ---")
for Guest in Guests:
    print(f"Dear {Guest}, you are still invited to dinner!")

del Guests[1]
del Guests[0]

print(f"\nFinal Guests list: {Guests}")

print("\nex-3.8 == Seeing the world")

location = ['Puri' , 'Nainital','Ayodhya','Kashi','Vrindavan']

print("Here is the original list:")
print(location)

print("\nHere is the sorted list:")
print(sorted(location))

print("\nHere is the original list again:")
print(location)

print("\nHere is the reverse-alphabatical list:")
print(sorted(location,reverse=True))

print("\nMy list is still in orginal form:")
print(location)

print("\nReversed order:")
location.reverse()
print(location)

print("\nBack to original order:")
location.reverse()
print(location)

print("\nPermanently sorted in alphabetical order:")
location.sort()
print(location)

print("\nPermanently sorted in reverse-alphabetical order:")
location.sort(reverse=True)
print(location)

print("\nex-3.9 == Dinner Guests")
 
print(f"I am inviting {len(Guests)} people to dinner")

print("\nex-3.10 == Every Function")

languages = ['Python','Rust','C','C++','JavaScript']
print("Initial list:",languages)

#1 Accessing elements by index
print(f"First element: {languages[0]}")
print(f"Last element: {languages[-1]}")

#2 Modifying an element
languages[1]='Java'
print("After modifying index 2:", languages)

#3 Adding elements
languages.append('Kotlin')
print("After append ('Kotlin):",languages)

languages.insert(1,'TypeScript')
print("After insert(1, 'TypeScript):", languages)

#4 Removing elements
del languages[4]
print("After del languages[4]:", languages)

popped_items = languages.pop()
print(f"Popped index 4 ('{popped_items}')", languages)

popped_last = languages.pop(4)
print(f"Popped index 4 ('{popped_last}'):", languages)

languages.remove("C")
print("After remove('C'):",languages)

#5 Finding list length 
print(f"Number of languages remaining : {len(languages)}")

#6 Temporary sorting :
print("Temporarily sorted:", sorted(languages))
print("Temporarily reverse-sorted:", sorted(languages))
print("List is unchanged:", languages)

#7 Reversing the order:
languages.reverse()
print("After reverse():",languages)

#8 Permanent sorting
languages.sort()
print("Permanently sorted:",languages)

languages.sort(reverse=True)
print("Permanently reverse-sorted:", languages)

print("\n--- End Of The Code ---")