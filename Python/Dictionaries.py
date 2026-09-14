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
for language in set(favorite_languages.values()): # set for not repeating the same value
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
    'OOP' : 'A style of coding that builds programs using interacting "objects that combine data and actions, making large projects easier to organize and reuse',
    }

for glossary in glossary.values():
    print(glossary.title())