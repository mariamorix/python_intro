#word = "commitment"
#fav_letter = input("What is your favorite letter? ")

#for letter in word :
#    if letter.lower() == fav_letter.lower() :
#        print("_", end = "")
#   else :
#        print(letter.lower(), end = "")
#print()

quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

keep_running = "yes"

while keep_running.lower() == "yes" :
    number = int(input("Give us a number: "))

    for i, letter in enumerate(quote) :
        if i % number == 0 :
            print(letter.upper(), end = "")
        else :
            print(letter.lower(), end = "")
    print()
    keep_running = input("Would like to try again (yes/no)? ")
print("Thanks for playing!")