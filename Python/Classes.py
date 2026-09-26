print("9.1 == Restaurant")

def describe_restaurant(restaurant_name, cuisine_type):
    print(f"{restaurant_name.title()} serves {cuisine_type.title()} cuisine.")
 
describe_restaurant("sushi bar", "Japanese")
describe_restaurant("burger joint", "American")
describe_restaurant("dal - chawal", "Indian")

print("\n9.2 == Three Restaurants")     
 
restaurant1 = {"name": "Sushi Bar", "cuisine": "Japanese"}
restaurant2 = {"name": "Burger Joint", "cuisine": "American"}
restaurant3 = {"name": "Dal - Chawal", "cuisine": "Indian"}

def describe_restaurant(restaurant):
    print(f"{restaurant['name'].title()} serves {restaurant['cuisine'].title()} cuisine.")

describe_restaurant(restaurant1)
describe_restaurant(restaurant2)
describe_restaurant(restaurant3)
 
print("\n9.3 == Users")

user1 = {"first_name": "Tony", "last_name": "Stark", "age": 45, "city": "New York"}
user2 = {"first_name": "Steve", "last_name": "Rogers", "age": 100, "city": "Brooklyn"}
user3 = {"first_name": "Natasha", "last_name": "Romanoff", "age": 35, "city": "Stalingrad"}
user4 = {"first_name": "Bruce", "last_name": "Banner", "age": 40, "city": "Dayton"}
user5 = {"first_name": "Thor", "last_name": "Odinson", "age": 1500, "city": "Asgard"}
user6 = {"first_name": "Clint", "last_name": "Barton", "age": 38, "city": "Waverly"}

def describe_user(user):
    print(f"Name: {user['first_name']} {user['last_name']}")
    print(f"Age: {user['age']}")
    print(f"City: {user['city']}\n")

describe_user(user1)
describe_user(user2)
describe_user(user3)
describe_user(user4)
describe_user(user5)
describe_user(user6)

def greet_user(user):
    print(f"Hello, {user['first_name']}! Welcome back.\n")
greet_user(user1)
greet_user(user2)
greet_user(user3)
greet_user(user4)
greet_user(user5)
greet_user(user6)

print("ex- 9.4 == Number Served")

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves delicious {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, additional_customers):
        self.number_served += additional_customers

restaurant = Restaurant('The Dal-Chawal', 'Indian')
print(f"Initial customers served: {restaurant.number_served}")

restaurant.number_served = 15

print(f"Customers served (after direct modification): {restaurant.number_served}")
restaurant.set_number_served(35)

print(f"Customers served (after calling set_number_served): {restaurant.number_served}")

restaurant.increment_number_served(25)
print(f"Customers served (after calling increment_number_served): {restaurant.number_served}")