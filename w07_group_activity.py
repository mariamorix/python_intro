import random

keep_playing = "yes"

while keep_playing.lower() == "yes" :

    number = random.randint(1,100)

    guess = int(input("What is your guess? "))
    count = 0

    while guess != number:
        count = count + 1
        if guess < number :
            print("Higher")
            guess = int(input("What is your guess? ")) 
        elif guess > number :
            print("Lower")
            guess = int(input("What is your guess? ")) 

    print("You gessed it!")
    keep_playing = input("Would you like to play again (yes/no)? ")

print("Thank you for playing! Good-bye!")

