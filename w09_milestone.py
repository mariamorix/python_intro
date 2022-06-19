print("Welcome to the Shopping Cart Program!")

cart = []
product = ""
remove_item = ""
option = 0

while option != 5 :
    option = int(input("""\nPlease select one of the following: 

1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit

Please enter an action: """))
    if option == 1 :
        product = input("What item would you like to add? ")
        if product != "nothing" :
            cart.append(product)
            print(f"{product.title()} was added to your cart.")
    elif option == 2 :
        print("The contents of the shopping cart are:")
        for product in cart:
            print(product.title())
    elif option == 3 :
        remove_item = input("What item would like to remove? ")
        cart.remove(remove_item.lower())
        print(f"{remove_item.title()} was removed succesfully.")
    elif option == 4 :
        print(f"Your cart has {len(cart)} itens.")
print("Thanks for shopping with us!")