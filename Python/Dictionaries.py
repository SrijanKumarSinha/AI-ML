from psutil import users


print("\nex-6.1 == Persons")

user_information = { 
    'first_name': 'Tony',
    'last_name': 'Stark',
    'age': 48,
    'city': 'New York'
    }
print(user_information)
print(user_information['first_name'])
print(user_information['last_name'])
print(user_information['age'])
print(user_information['city'])

print("\nex-6.2 == Favorite Numbers")

favorite_numbers = {
    'Tony stark' : '7',
    'Steve rogers' : '2',
    'Thor' : '5',
    'Clint barton' : '3',
    'Bruce banner' : '4',
    'Natasha romanoff' : '8'
    }

print(favorite_numbers)
print(f"Tony Stark's favorite number is {favorite_numbers['Tony stark']}.")
print(f"Steve Rogers' favorite number is {favorite_numbers['Steve rogers']}.")
print(f"Thor's favorite number is {favorite_numbers['Thor']}.")
print(f"Clint Barton's favorite number is {favorite_numbers['Clint barton']}.")
print(f"Bruce Banner's favorite number is {favorite_numbers['Bruce banner']}.")
print(f"Natasha Romanoff's favorite number is {favorite_numbers['Natasha romanoff']}.")

print("\nex-6.3 == Glossary")

glossary = {
    'list' : 'A collection of items in a particular order.',
    'tuple' : 'A collection of items that is ordered and unchangeable.',
    'dictionary' : 'A collection of key-value pairs.',
    'set' : 'A collection of unique items.',
    'string' : 'A sequence of characters.'
    }

print(f"List : {glossary['list']}")
print(f"\nTuple : {glossary['tuple']}")
print(f"\nDictionary : {glossary['dictionary']}")
print(f"\nSet : {glossary['set']}")
print(f"\nString : {glossary['string']}")

print("\nIN-TEXT PRACTICE")

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python',
    }
 
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): # using set for not repeating the same value
    print(language.title())

print("\nex-6.4 == Glossary 2")

glossary = {
    'list' : 'A collection of items in a particular order.',
    'tuple' : 'A collection of items that is ordered and unchangeable.',
    'dictionary' : 'A collection of key-value pairs.',
    'set' : 'A collection of unique items.',
    'string' : 'A sequence of characters.',
    'functions' : 'A reusable blovk of organized code desgined to perform a specific, single action',
    'class' : 'A blueprint or code template used to create objects that bundle data and functions together into songle unit',
    'OOP' : 'A style of coding that builds programs using interacting "objects that combine data and actions,making large projects easier to organize and reuse',
    }

for glossary in glossary.values():
    print(glossary.title())

print("\nex-6.5 == Rivers")

rivers = {
    'ganga' : 'india',
    'nile' : 'egypt',
    'amazon' : 'south america',
    }

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for key in rivers:  # for printing key values of the dictionary [rivers] through loop
    print(key)

for value in rivers.values():  # for printing value of the dictionary [rivers] through loop
    print(value)

for key, value in rivers.items(): # for printing the key and value side by side through loop
    print(key, ":", value)


print("\nex-.6.6 == Polling")

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python',
    'chris' : 'c++',
    'bruce' : 'java',
    'clint' : 'javascript'
    }
for name in sorted(favorite_languages.keys()): # using sorted, for arranging names in alphabetical order
    print(f"{name.title()}, thankyou for voting on poll.")

print("\nex-6.7 == People")


avenger_1 = { 
    'first_name': 'Tony',
    'last_name': 'Stark',
    'age': '48',
    'city': 'New York'
}

avenger_2 = {
    'first_name' : 'Bruce',
    'last_name' : 'Banner',
    'age' : '50',
    'city' : 'Ohio'
}

avenger_3 = {
    'first_name' : 'Natasha',
    'last_name' : 'Romanoff',
    'age' : '34',
    'city' : 'Russia'
}
    
people = [avenger_1, avenger_2, avenger_3]
for avenger in people:
    full_name = f"{avenger['first_name'].title()} {avenger['last_name'].title()}"
    print(f"Name : {full_name}")
    print(f"Age : {avenger['age']}")
    print(f"Location : {avenger['city'].title()}\n")

print("\nex-6.8 == Pets")

pet_1 = {
    'breed' : 'Golden Retriever',
    'owner name' : 'Prapti'
    }

pet_2 = {
    'breed' : 'German Shepherd',
    'owner name' : 'Arvind'
    }

pet_3 = {
    'breed' : 'German Shepherd',
    'owner name' : 'Rahul'
    }

pets = [pet_1, pet_2, pet_3]
for pet in pets:
    print(f" Breed : {pet['breed']}")
    print(f"Owner Name : {pet['owner name']}\n")

print("\nex-6.9 == Favorite Places")

favorite_places = {
    'Tony Stark' : ['Titan'],
    'Steve Rogers' : ['Wakanda'],
    'Thor' : ['Nedaviller']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favourite place is:")
    for place in places:
        print(f"- {place.title()}")

print("\nex-6.10 == Favorite Numbers")

favorite_numbers = {
    'Tony stark' : ['7','8','9'],
    'Steve rogers' : ['2','3','5'],
    'Thor' : ['5','4','6'],
    'Clint barton' : ['3','10'],
    'Bruce banner' : ['4','2','7','1'],
    'Natasha romanoff' : ['8','2','7']
}

for name, numbers in favorite_numbers.items():
    num_strings = [str(number) for number in numbers]
    horizontal_numbers = " , ".join(num_strings)
    
    print(f"\n{name.title()}'s favourite numbers are : {horizontal_numbers}")

print("\nex-6.11 == Cities")

cities = {
    'deoghar' : {
        'country' : 'india',
        'state' : 'jharkhand',
        'population' : 300000,
        'fact' : 'One jyotirling of Mahadev is in deoghar'
        },

    'nainital' : {
        'country' : 'india',
        'state' : 'uttarakhand',
        'population' : 954605,
        'fact' : 'Kaichi dham of neeb karori baba is in the hills of nainital'
        },

    'ayodhya' : {
        'country' : 'india',
        'state' : 'uttar pradesh',
        'population' : 248000000,
        'fact' : 'Shree ram janm bhoomi , Ram mandir  in ayodhya'
        }
    }

for city, city_info in cities.items():
    print(f"\nCity : {city.title()}")
    print(f"Country : {city_info['country'].title()}")
    print(f"State : {city_info['state'].title()}")
    print(f"Population : {city_info['population'] :,}")
    print(f"Fact : {city_info['fact'].capitalize()}")

print("\nex-6.12 == Extensions")

cities = {
    'deoghar' : {
        'country' : 'india',
        'state' : 'jharkhand',
        'population' : 300000,
        'fact' : 'One jyotirling of Mahadev is in deoghar',
        'language' : 'hindi' # Added a new key
        },

    'nainital' : {
        'country' : 'india',
        'state' : 'uttarakhand',
        'population' : 954605,
        'fact' : 'Kaichi dham of neeb karori baba is in the hills of nainital',
        'language' : 'kumaoni' # Added a new key
        },

    'ayodhya' : {
        'country' : 'india',
        'state' : 'uttar pradesh',
        'population' : 248000000,
        'fact' : 'Shree ram janm bhoomi , Ram mandir  in ayodhya',
        'language' : 'awadhi' # Added a new key
        }
    }

print("\n--- City Profiles ---")
for city, city_info in cities.items():
    print(f"\nWelcome to {city.title()}!")
    print(f"Located in : {city_info['state'].title()} , {city_info['country'].title()}")
    print(f"Regional Language is : {city_info['language'].title()}")
    print(f"Total Population : {city_info['population']:,}")
    print(f"Fact : {city_info['fact'].capitalize()}")

print("\n--- End Of The Code ---")