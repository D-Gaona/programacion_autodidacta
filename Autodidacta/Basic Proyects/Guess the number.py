        #Number Guesser
import random

top_of_range = input("Type the top number to guess ")

if top_of_range.isdigit():      #.isdigit() ayuda a comprobar que el dato insertado es un numero
    top_of_range = int(top_of_range)

elif top_of_range <= 0:
    print("Please type a number larger than 0 next time.")
    quit()
else:
    print("Please type a number next time.")
    quit()


random_number = random.randint(1, top_of_range)
number_of_tries = 0

while True:
    number_of_tries += 1

    user_guess = input("Make a guess ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("NICE GUESS!!")
        break
    elif user_guess > random_number:
        print("You were above the number, try again")
    else:
        print("You were below the number, try again")


print("You got it in ", number_of_tries, " guesses")
