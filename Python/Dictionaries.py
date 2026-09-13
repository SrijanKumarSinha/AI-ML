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


