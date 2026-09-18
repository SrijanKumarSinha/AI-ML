print("ex- 8.1 == Message")

def display_message():
    '''Display a sentence.'''
    print("I am learning today Functions.")

display_message()

print("\nex- 8.2 == Favorite Book")

def favorite_book(Bookname):
    print(f"Currently my favorite book is {Bookname.title()}.")
favorite_book('Python Crash Course by Eric Matthes')

print("\nex- 8.3 == T-Shirt")

def make_shirt(size, message):
    print(f"\nThe size of the T-shirt is {size} and the message printed on it is '{message}'.")

make_shirt('Large', 'I love Python')
make_shirt('Medium', 'Python is awesome!')
make_shirt('Small', 'Code with Python')

print("\nex- 8.4 == Large Shirts")

def make_shirt(size='Large', message='I love Python'):
    print(f"\nThe size of the T-shirt is {size} and the message printed on it is '{message}'.")

make_shirt('Medium', 'Python is awesome!')
make_shirt('Double Extra Large', 'I am Iron Man')
make_shirt()  # Using default values

print("\nex- 8.5 == Cities")

def describe_city(city, country='INDIA'):
    print(f"{city.title()} is in {country.title()}.")

describe_city('Delhi')
describe_city('Mumbai')
describe_city('Jharkhand')
describe_city('Bihar')

