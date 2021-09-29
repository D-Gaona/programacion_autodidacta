        #Presentation to the program
print("Welcome to my computer quiz! ")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Bye")
    quit()

print("Okay let's play :)")

        #Score method

score = 0           #Add to every if statement += 1

        #Quiz structure

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("25 + 70 =  ")
if answer.lower() == str(95):
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("28 * 5 = ")
if answer.lower() == str(140):
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("Capital of Russia ")
if answer.lower() == "moscu":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("Amazonas is a lake or a river? ")
if answer.lower() == "river":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("Cobras are venomous? ")
if answer.lower() == "yes":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("what tipe of venom does cobras have? ")
if answer.lower() == "neurotoxic":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("That is " + str((score / 10) * 100) + "% of the questions")


