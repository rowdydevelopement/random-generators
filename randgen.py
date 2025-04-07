# Import necessary modules
import random  # for generating random choices and numbers
import sys     # for system-related functions like exiting the program

# List of potential fortunes to be randomly selected
fortunes = [
    "you will die at the age of seventy years, five months,3 days,9 hours, 4 minutes, and 2.31 seconds at 8 pm in Houston,Texas 6 hours, 3 minutes, and 8.79 seconds after being hit by a 2050 ford 350 traveling down fondren road at 60.32 mph.",
    "Good things await you within the next 24 hours.",
    "Watch your back...",
    "You will die alone.",
    "You will or have found love.",
    "You will experience burning the next time you pee.",
    "You need to get a new haircut.",
    "You will either be great or fail.",
    "The god of twerking smiles upon you!",
    "You will have good luck today",
    "Something exciting will happen on [Thursday]",
    "You will have a fun adventure",
    "You will make a best friend",
    "Someone will make you smile today",
    "The [8th] of next month is your day",
    "Someone new will come into your life soon",
    "A great fortune is a great servitude",
    "Whatever may happen, every kind of fortune is to be overcome by bearing it"
]

# Generate a random fortune, integer, and decimal
fortune = random.choice(fortunes)
number = random.randint(0, 100)
decimal = random.uniform(0, 100)

# Prompt user to type in lowercase
print("type lowcase pls")
print("HELLO.WHAT IS YOUR NAME?")
name = input()

# Function to greet the user with special behavior if name is "penny"
def greet(name):
    if name == "penny":
        print("I HEAR YOU ARE THE CREATOR OF THE GRAND LEADER.GOOD JOB.")
    else:
        print(f"NICE TO MEET YOU {name}")

# Call the greeting function
greet(name)

# Prompt user to choose one of three "algorithms"
print("I CAN DO ONE OF THREE RANDOM ALGORITHMS.")
print("CHOOSE FROM: NUMBER,DECIMAL, OR FORTUNE")
choice = input()

# Function that performs action based on user's choice
def algorithm(choice):
    if choice == "number":
        print(number)
    elif choice == "fortune":
        print(fortune)
    elif choice == "decimal":
        print(decimal)
    else:
        # Exit if input is invalid
        sys.exit("system error. Does not compute.")

# Run the chosen algorithm
algorithm(choice)

# Payment sequence
print("THANK YOU FOR YOUR PATRONAGE.THAT WILL BE $1.")
print("PLEASE INSERT PEYMENT INTO NEARBY BOX.")
print("HAS PAYMENT BEEN INSERTED?")

# List of fun/silly fake cusses
cusses = [
    "$4!7",
    "@#%%@@@@#&",
    "#$%@",
    "@#!!!$",
    "#^^#@",
    "!#%@$",
    "%^&&*",
    "*&^^*((@#",
]

# Choose a random cuss for use if user doesn't pay
cuss = random.choice(cusses)

# Ask user to confirm payment
answer = input("Tell me here.Say YES or NO:")

# Function to handle user's yes/no answer
def yesorno(answer):
    if answer == "yes":
        print("Thank you for your choice to use the ROWDYBOT SERVICE TERMINAL.")
    elif answer == "no":
        print("Insert money, you little " + cuss)
    else:
        sys.exit("system error")

# Run the yes/no handler
yesorno(answer)

# End the program
sys.exit("GOODBYE.")
