import random

def some_facts(user_input, number):
  swimming_fact = [
    "Most competitive swimmers swim 6-12 miles a day",
    "An Olympic pool can hold up to 850,000 gallons of water",
    "Gertrude Ederle was the first woman to swim the English Channel, in 1926",
    "The first swimming goggles were made from tortoise shells",
    "The first known record of people swimming dates back to Egyptian drawings from 2500BC"
  ]

  running_fact = [
    "Instead of 'running', the activity was known as 'pedestrianism' during the late 19th century",
    "Each step you run involves movement from 200 muscles",
    "Cheetah, the fastest animal on earth, could run at 110-120 km/h, while the rest of its feline kind could reach up to 30mph",
    "1 billion pairs of running shoes are sold around the world annually",
    "If you want to run the whole planet, you have to run 12 miles every day for 2,075 days"
  ]

  football_fact = [
    "The first World Cup was held in Uruguay in 1930, only 13 teams played",
    "The first official Women's football tournament took place in 1991",
    "By 1998, the number of men's teams competing in the World Cup was 32",
    "Brazil is the only team to have played in every single World Cup tournament",
    "In 2022, England's women's team won the European Championship for the first time in over 50 years!"
  ]
  if user_input == "swimming":
    for i in range(0, number):
      print("Swimming fact " + str(i+1) +": " + str(swimming_fact[i]))
  elif user_input == "running":
    for i in range(0, number):
      print("Running fact " + str(i+1) +": " + str(running_fact[i]))
  elif user_input == "football":
    for i in range(0, number):
      print("Football fact " + str(i+1) +": " + str(football_fact[i]))
  else:
    print("Sorry but I dont know any facts on that one!")
  
def main_function():
  user_play = input("Would you like to know some sports facts? y/n ")
  if user_play == "y":
    user_sport = input("Would you like to know some facts about swimming, running or football? ")
    user_fact_number = input("How many facts would you like to know? Pick a number 1-5 or random (I choose!) ")
    if user_fact_number == "random":
      user_fact_number = random.randint(1,5)
      print("Your number is: " + str(user_fact_number))
    some_facts(user_sport, int(user_fact_number))
    play_again = input("Would you like to learn some more? y/n ")
    if play_again == "y":
      main_function()
    elif play_again == "n":
      print("Hope you learnt something and see you soon!")
    else:
      print("I'm sorry I did not understand that response please type y (for yes) or n (for no) ")
      while play_again != "n" and play_again != "y":
        main_function()
  elif user_play == "n":
    print("Maybe another time!")
  else:
    print("I'm sorry I did not understand that response please type y (for yes) or n (for no) ")
    while user_play != "n" and user_play != "y":
      main_function()
    

main_function()