# 1 - Use a while loop to ask the user for a positive number (>= 0). 
#Continue asking as long as the number is negative, then display the number.

#number = float(input("Please, type a positive number: "))

#while number <= 0 :
#    print("Sorry, that is a negative number. Try again.")
#    number = float(input("Please, type a positive number: "))


#print("Ended the loop")

# 2 - Use a while loop, to simulate a child asking their parent for a piece of candy.
#Have the program keep looping until the user answers "yes", then have the program output "Thank you." 

candy = ""

#while candy.lower() == "no" :
#    candy = input("May I have a piece of candy? ")

#print("Thank you!")

#another way to do number 2:

while candy.lower() != "yes" :
    candy = input("May I have a piece of candy? ")
    
print("Thank you!")