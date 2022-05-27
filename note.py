first_age = int(input("What is the age of the first rider? "))
first_height = float(input("What is the height of the first rider? "))
second_rider = input("Is there a second rider (yes/no)? ")
if second_rider.lower() == "yes":
    second_age = int(input("What is the age of the second rider? "))
    second_height = float(input("What is the height of the second rider? "))
    if first_age >= 18 or second_age >= 18:
        if first_height < 36 or second_height < 36:
            should_ride = False
        else:
            should_ride = True
    elif first_age >= 12 or second_age >=12:
        if first_height >= 52 or second_height >=52:
            golden_pass = input("Do you have Golden passport (yes/no)? ")
            if golden_pass.lower() == "yes":
                should_ride = True
            elif golden_pass.lower() == "no":
                # should_ride = False   
                if first_age >= 16 or second_age >=16:
                    if first_age >= 14 or second_age >= 14:
                        should_ride = True
                    else:
                        should_ride = False
                else:
                    should_ride = False
        else:
            should_ride = False       
    else:
        should_ride = False                             
elif second_rider.lower() == "no":
    if first_age >= 18 and first_height >= 62:
        should_ride = True
    elif first_age >= 12 and first_height >= 52:
        golden_pass = input("Do you have Golden passport (yes/no)? ")
        if golden_pass.lower() == "yes":
            should_ride = True
        elif golden_pass.lower() == "no":
            should_ride = False   
    else:
        should_ride = False
else:
    print("YES or NO.")       
#BOOLEAN
if should_ride:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")