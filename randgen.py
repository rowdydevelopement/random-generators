import random
import sys
fortunes=[
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
    "Whatever may happen, every kind of fortune is to be overcome by bearing it"]
fortune=random.choice(fortunes)
number=random.randint(0,100)
decimal=random.uniform(0,100)
print("type lowcase pls")
print("HELLO.WHAT IS YOUR NAME?")
name=input()
def greet(name):
	if name=="penny":
		print("I HEAR YOU ARE THE CREATOR OF THE GRAND LEADER.GOOD JOB.")
	else:
		print(f"NICE TO MEET YOU {name}")
greet(name)

		
print("I CAN DO ONE OF THREE RANDOM ALGORITHMS.")
print("CHOOSE FROM: NUMBER,DECIMAL, OR FORTUNE")

choice=input()
def algorithm(choice):
  if choice=="number":
    print(number)
  elif choice=="fortune":
    print(fortune)
  elif choice=="decimal":
    print(decimal)
  else:
    sys.exit("system error. Does not compute.")
 
algorithm(choice)

print("THANK YOU FOR YOUR PATRONAGE.THAT WILL BE $1.")
print("PLEASE INSERT PEYMENT INTO NEARBY BOX.")
print("HAS PAYMENT BEEN INSERTED?")
cusses = [
  "$4!7",
"@#%%@@@@#&",
"#$%@",
"@#!!!$",
"#^^#@",
"!#%@$",
"%^&&*",
"*&^^*((@#",]
cuss=random.choice(cusses)
answer = input("Tell me here.Say YES or NO:")
def yesorno(answer):
    if answer == "yes": 
        print("Thank you for your choice to use the ROWDYBOT SERVICE TERMINAL.")
    elif answer == "no":
      print("Insert money, you little " + cuss)   
    else:
      sys.exit("system error")
yesorno(answer) 

sys.exit("GOODBYE.")
