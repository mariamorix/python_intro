#For this assignment, you'll work as a team to write a program for a fictitious amusement park ride.
#RULES: No one under 36 inches may ever ride, either by themselves or with another rider.
#Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.
#If there are two riders and one of them is at least 18 years old, they may ride together.

first_rider_age = int(input("What is the age of the first rider? "))
first_rider_height = int(input("What is the height of the first rider? "))
second_rider = input("Is there a second rider (yes/no)? ")

    

if first_rider_height < 36 :
    ride_acceptance = False
else:
    if second_rider.lower() == "no" and first_rider_age >= 18 and first_rider_height >= 62 :
        ride_acceptance = True
    elif second_rider.lower() == "no" :
        if first_rider_age >= 12 and first_rider_age <= 17 :
            golden_pass = input("Do you have a golden passport?(yes/no) ")
            if golden_pass.lower() == "yes" :
                ride_acceptance = True
            else:
                ride_acceptance = False
    elif second_rider.lower() == "yes":
        second_rider_age = int(input("What is the age of the second rider? "))
        second_rider_height = int(input("What is the height of the second rider? "))
        if second_rider_height >= 36 and first_rider_age >= 18 or second_rider_age >= 18 :
             ride_acceptance = True
        elif (first_rider_age >= 12 and second_rider_age >=12) and (first_rider_height >=52 and second_rider_height >= 52) :
            ride_acceptance = True
        elif second_rider_age >= 12 and second_rider_age <= 17 :
            golden_pass = input("Do you have a golden passport?(yes/no) ")
            if golden_pass.lower() == "yes" :
                ride_acceptance = True
            else:
                if(first_rider_age >=14 and second_rider_age >= 16) or (first_rider_age >=16 and second_rider_age >=14) :
                    ride_acceptance = True
                else:
                    ride_acceptance = False
        else:
            ride_acceptance = False
    else:
        ride_acceptance = False

if ride_acceptance :
    print("Yeah, you may ride!")
else :
    print("Sorry, you may not ride!")