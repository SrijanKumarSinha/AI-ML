from ast import Return


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

print("\nex- 8.6 == City Names")

def get_city_country(city, country):
    citycountry_name =f"\n{city.title()} , {country.title()}"
    return citycountry_name.title()

while True:
    print("\nEnter your city and country name: ")
    print("(enter 'q' at any time to quit)")

    city_name = input("City Name: ")
    if city_name == 'q':
        break

    country_name = input("Country Name: ")
    if country_name == 'q':
        break

    city_country = get_city_country(city_name, country_name)
    print(f"\n {city_country}")

print("\nex- 8.7 == Album")

def make_album(artist_name, album_title, tracks=None):
    """Build a dictionary of information."""
    album_dict = {
        'artist': artist_name.title(),
        'title': album_title.title()
    }

    if tracks:
        album_dict['tracks'] = tracks

        return album_dict

album1 = make_album('Arijit Singh', 'Tum Hi Ho')
album2 = make_album('Arijit Singh', 'Channa Mereya', 10)
album3 = make_album('Arijit Singh', 'Raabta', 12)
album4 = make_album('Arijit Singh', 'Manwa Laage', 8)
album5 = make_album('Arijit Singh', 'Zaalima', 9)
album6 = make_album('Arijit Singh', 'Mast Magan', 11)

print(album1)
print(album2)
print(album3)
print(album4)
print(album5)
print(album6)

album_with_tracks = make_album('Arijit Singh', 'Tum Hi Ho', 10)
print(album_with_tracks)

print("\nex- 8.8 == User Albums")

def make_album(artist_name, album_title, tracks=None):
    """Build a dictionary of information."""
    album_dict = {
        'artist': artist_name.title(),
        'title': album_title.title()
    }

    if tracks:
        album_dict['tracks'] = tracks

    return album_dict

while True:
    print("\nEnter the artist name and album title: ")
    print("(enter 'q' at any time to quit)")

    artist_name = input("Artist Name: ")
    if artist_name == 'q':
        break

    album_title = input("Album Title: ")
    if album_title == 'q':
        break

    album = make_album(artist_name, album_title)
    print(f"\n {album}")

print("\nThank you for using the album generator!")

print("\nex- 8.9 == Messages")

messages = ["Hello, how are you?", "I'm doing great!", "What's up?"]

def show_messages(msg_list):
    for msg in msg_list:
        print(msg)

show_messages(messages)

print("\nex- 8.10 == Sending Messages")

def send_messages(msg_list):
    sent_messages = []
    while msg_list:
        current_msg = msg_list.pop()
        print(f"Sending message: {current_msg}")
        sent_messages.append(current_msg)
    return sent_messages

sent_messages = send_messages(messages)
print("\nSent messages:")
for msg in sent_messages:
    print(msg)

print("\nex- 8.11 == Archived Messages")

print("\nArchived messages:")
for msg in messages:
    print(msg)

print("\nex- 8.12 == Sandwiches")

def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich("lettuce", "tomato", "chicken")
make_sandwich("bacon", "lettuce", "tomato")
make_sandwich("turkey", "swiss cheese", "lettuce", "tomato")

print("\nex- 8.13 == User Profile")

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value
    return profile

print("\nUser Profile:")
user_profile = build_profile('John', 'Doe', location='New York', field='Software Engineer')
for key, value in user_profile.items(): 
    print(f"{key}: {value}")    

print("\nex- 8.14 == Cars")

def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title()
    }
    for key, value in car_info.items():
        car_dict[key] = value
    return car_dict

car = make_car('tata', 'outback', color='blue', tow_package=True)
print(car)


