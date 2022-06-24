

print("Welcome to the Shopping Cart Program!")

carts = []
prices = []
product = ""
cost = 0
remove_item = 0
total_cost = 0
discount = 0
new_total = 0
option = 0

while option != 6 :
    option = int(input("""\nPlease select one of the following: 

1. Add item
2. View cart
3. Remove item
4. Compute total
5. Add Discount Cupom
6. Quit

Please enter an action: """))
    if option == 1 :
        print()
        product = input("What item would you like to add? ")
        if product != "nothing" :
            carts.append(product)
        cost = float(input(f"How much {product.title()} costs? "))
        if cost != 0 :
            prices.append(cost)
            print(f"{product.title()} was added to your cart.")
    elif option == 2 :
        print()
        print("The contents of the shopping cart are:")
        for i in range(len(carts)) :
            cart = carts[i]
            price = prices[i]
            print(f"{carts.index(cart)+ 1}. {cart.title()} - ${price:.2f} ")
    elif option == 3 :
        print()
        if remove_item <= len(carts) :
            remove_item = int(input("What item would like to remove? "))
            item_removed = carts.pop(remove_item - 1) 
            price_removed = prices.pop(remove_item - 1) 
            print(f"Item {remove_item} was removed succesfully.")
        else:
                print("Sorry, that is not a valid item number.")
    elif option == 4 :
        print()
        total_cost = sum(prices)
        print(f"The total price of the items in the shopping cart is $ {total_cost:.2f}")
    elif option == 5 :
        discount = int(input("Please give the percentage of your discount cupom: "))
        new_total = total_cost - (total_cost * discount / 100)
        print()
        print(f"The new total is: $ {new_total:.2f}")


print()
print("Thanks for shopping with us!")