import random

COLOURS = ['blue','green','yellow','red','purple','orange','teal']
CARS = ['mclaren','ferrari','lamborghini','bugatti','porsche']
TYPES = ['coupe','convertible','manual','automatic']

def generate_password():
    # Choose three random words from the lists
    return random.choice(COLOURS) + random.choice(CARS) + random.choice(TYPES)


# Ask user to input number of passwords needed
num_passwords = input("Password Generator\n==================\n\nHow many passwords are needed?: ")

# Validate the input
try:
    num_passwords = int(num_passwords)
except ValueError:
    print("Please enter a number.")
    exit()

# Check if the user input is between 1 and 24
if num_passwords < 1 or num_passwords > 24:
    print("Please enter a value between 1 and 24.")
    exit()

# Generate and print the passwords
for n in range(num_passwords):
    print(f"{n+1} --> {generate_password()}")
    
  