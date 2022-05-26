grade = float(input("Insert your grade: "))

last_digit = grade%10

if last_digit >= 7 :
    sign = "+"
elif last_digit < 3 :
    sign = "-"
else :
    sign = ""
    
if grade >= 93 :
    letter = "A"
elif grade >= 90 :
     letter = "A" + sign
elif grade >= 80 :
    letter = "B" + sign
elif grade >= 70 :
    letter = "C" + sign
elif grade >= 60 :
    letter = "D" + sign
else :
    letter = "F"

if grade >= 70 :
    message = "Congratulations! You have pass this course!"
else :
    message = "Your grade hasn't meet the requirements to pass this course! Don't give up, keep studying, and try again!"

print (f"Your grade is: {letter}. {message}")