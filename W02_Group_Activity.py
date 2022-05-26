print('Please enter the following information:')

first_name = input ('First name: ')
last_name = input ('Last name: ')
email = input ('Email Address: ')
phone_num = input ('Phone Number: ')
job_title = input ('Job Title: ')
id_number = input('ID Number: ')
hair = input('Hair Color: ')
eyes = input('Eyes Color: ')
month = input('Month: ')
training = input ('Do you have advance training? ')


print(f"""
The ID Card is:
----------------------------------------------------
{last_name.upper()}, {first_name.capitalize()}
{job_title.title()}
ID: {id_number}
​
{email.lower()}
{phone_num}
​
Hair: {hair.capitalize():<25}Eyes: {eyes.capitalize()}
Month: {month.capitalize():<24}Training: {training.capitalize()}
----------------------------------------------------
""")