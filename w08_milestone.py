import random


print("Welcome to the word guessing game!")
keep_playing = "yes"

while keep_playing.lower() == "yes" :

    word_list = ["dog", "cat", "violin", "answer", "water", "window"]
    target_word = random.choice(word_list)
    count = 1
    print(target_word)
    hint = len(target_word) * "_"
    print(f"Your hint is: {hint} ")
    guess = input("What is your guess? ")

    while guess.lower() != target_word :

        for i, letter in enumerate(guess):
            if letter in target_word:
                if letter == target_word[i]:
                    print(f"{letter.upper()}", end = "")
                else:
                    print(f"{letter.lower()}", end = "")
            else:
                print(f"_", end = "")
        count = count + 1
        guess = input("\nWhat is your guess? ")
    print(f"Congratulations, you guessed it! It took you {count} guesses!")
    keep_playing = input("Would you like to play again (yes/no)? ")

print("Thanks for playing with us!")