name = input("Type your name: ")
print("Welcome ", name, " to whis adventure")

answer = input(
    "You are on the road, driving alone, suddenly you see a new driveway you didn't knew, do you take it? ").lower()
if answer == "yes":
    print("Well, now you'r going nowhere, that sound like a big adventure. ")

    answer == input("Are you scared? ").lower()
    if answer == "yes":
        print("It´s normal to feel scared, it always happens when we are exploring new paths of our lives. ")

        answer == input("Do you want to turn arround? ").lower()
        if answer == "yes":
            print("C´mon lets turn around, we can think better when we are in peace ")

        elif answer == "no":
            print("Nice, lets see what we found at the end of the road, ")


    elif answer == "no":
        print("Wow, so you are brave. ")
        answer == input(
            "While you are on the path, suddenly it comes to an end, you have to choose, Left or Right ").lower()


elif answer == "no":
    print("Well, at least you know where are you going. ")
    answer = input("Are you feeling ok? ")


else:
    print("That's not a valid answer, you have to choose")
    quit()
