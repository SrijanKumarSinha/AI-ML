# %% [markdown]
# Ex - 7.1 == Rental Car

# %%
Car_name = input("Enter your car name: ")  # input method, for taking user's input 
print(f"\nLet me see if i can find you a {Car_name}.") 



# %% [markdown]
# Ex - 7.2 == Restaurant Seating

# %%
people_number = int(20)

people = input("How many people are there: ")
if people_number < 8:
    print("\nThey'll have to wait for a table")
else:
    print("\nThe table is ready")

# %% [markdown]
# Ex - 7.3 == Multiples of Ten

# %%
number = input("Enter a number, and I'll tell you if it is multiple of 10 or not: ")
number = int(number)

if number % 10 == 0:
    print(f"The number {number} is multiple of 10")
else:
    print(f"The number {number} is not the multiple of 10")

# %% [markdown]
# Ex - 7.4 == Pizza Toppings

# %%
prompt = "\nEnter your toppings for your pizza:"
prompt += "\nEnter 'quit' to end your program."

toppings = " "
while toppings != 'quit':
    toppings = input(prompt)
    print(toppings)

# %% [markdown]
# Ex - 7.5 == Movie Tickets

# %%
age = input("Enter your age to know the price of your movie ticket: ")
age = int(age)
if age < 3 :
    print("The ticket is free")
elif age >= 3 and age <=12 :
    print("The ticket price is 10 rupees only")
else:
    print("The ticket price is 15 rupees only")

# %% [markdown]
# Ex - 7.6 == Three Exists

# %% [markdown]
# Using conditional test in a while loop to stop the loop

# %%
prompt = "\nEnter your toppings for your pizza:"
prompt += "\nEnter 'quit' to end your program."

toppings = " "
while toppings != 'quit':
    toppings = input(prompt)
    print(toppings)


