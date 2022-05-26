from re import S


childs_meal=float(input("What is the price of a child's meal? "))
adults_meal=float(input("What is the price of an adult's meal? "))
total_children=int(input("How many children are there? "))
total_adults=int(input("How many adults are there? "))
sales_tax_rate=float(input("What is the sales tax rate? "))
subtotal=(childs_meal*total_children)+(adults_meal*total_adults)
sales_tax=(subtotal*sales_tax_rate)/100
total=subtotal+sales_tax

print(f"""\nSubtotal:${subtotal}
Sales Tax: ${sales_tax}
Total: ${total}\n""")

payment_amount=float(input("What is the payment amount? "))
change=payment_amount-total

print(f"Change: ${round(change,2)}")
