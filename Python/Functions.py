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

print("\nex- 8.9 == Magicians")