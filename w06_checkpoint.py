#Write a program to determine wheter to loan money based on the following rules:
#First, check if the loan size is at least 5. If it is, use the following rules:
#If the credit history and income are both at least 7, then the decision is "yes"
#If either the credit history or income is at least 7, then check if the down payment is at least 5, if it is, the decision is "yes", if not, the decision is "no"
#Otherwise (if neither the credit history nor income is at least 7), the decision is "no"
#Otherwise (if the loan is not 5 or greater), use these rules:
#If the credit is less than 4, then the decision is "no"
#Otherwise, check the following:
#If either the income or the down payment is at least 7, the decision is "yes"
#If both the income and the down payment are at least 4, then the answer is "yes"
#Otherwise, the decision is "no"
#Finally, display the decision to the user.

loan = int(input("How large is the loan? "))
credit_history = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))

if loan >= 5 :
    if credit_history >= 7 and income >= 7 :
         loan_acceptance = True
    elif credit_history >= 7 or income >=7 :
        if down_payment >= 5 :
            loan_acceptance = True
        else :
            loan_acceptance = False
    else :
        loan_acceptance = False
else:
    if credit_history < 4 :
        loan_acceptance = False
    else:
        if income >= 7 or down_payment >= 7 :
            loan_acceptance = True
        elif income >= 4 and down_payment >= 4 :
            loan_acceptance = True
        else:
            loan_acceptance = False
       

if loan_acceptance == True :
    print("Loan Accepted")
else :
    print("Loan Denied")
