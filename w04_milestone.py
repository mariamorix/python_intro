
childs_meal = float(input("What is the price of a child's meal? "))
adults_meal = float(input("What is the price of an adult's meal? "))
total_children = int(input("How many children are there? "))
total_adults = int(input("How many adults are there? "))
sales_tax_rate = float(input("What is the sales tax rate? "))
subtotal = (childs_meal * total_children) + (adults_meal * total_adults)
sales_tax = (subtotal * sales_tax_rate) / 100
total = subtotal + sales_tax

print(f"""\nSubtotal:${subtotal:.2f}
Sales Tax: ${sales_tax:.2f}
Total: ${total:.2f}\n""")

payment_amount = float(input("What is the payment amount? "))
change = payment_amount-total

print(f"Change: ${change:.2f}")

if change < 10 :
    print("\nYou can keep the change!")
else :
    print("\nHave a nice day!")
