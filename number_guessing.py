import random 
number = random.randint(1, 100)
attempts = 0
while True:
    try:
     num1 = int(input("Enter a number between 1 to 100!"))
     attempts += 1
     if num1 == number:
      print("Wohoo! Right guess! You've guessed in",attempts)
     elif num1 > number:
      print("Sorry! too high")
     else:
      print("Sorry! too low")
    except ValueError:
      print("Invalid input! Please enter valid choice")

