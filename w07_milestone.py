keep_playing = "yes"

while keep_playing.lower() == "yes" :

    target_word = "answer"
    count = 0
    hint = len(target_word) * "_"
    print(f"Your hint is: {hint} ")
    guess = input("What is your guess? ")

    while guess.lower() != target_word :
        count = count + 1
        print("That is not correct, try again!")
        guess = input("What is your guess? ")
    print(f"Congratulations, you guessed it! It took you {count} guesses!")
    keep_playing = input("Would you like to play again (yes/no)? ")

print("Thanks for playing with us!")

#continues on week 08