itens_list = []
item = ""

print("Please enter the items of the shopping list (type: quit to finish):")
while item.lower() != "quit" :
    item = input("Item: ")

    if item != "quit" :
        itens_list.append(item.lower())

print("\nThe shopping list is:")
print()

for item in itens_list:
    print(item.title())
print()

print("\nThe shopping with indexes is:")
for i in range(len(itens_list)) :
    item = itens_list[i]
    print(f"{i}. {item.title()}")
print()

index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

itens_list[index] = new_item

print("\nThe shopping list with indexes is:")
for i in range(len(itens_list)):
    item = itens_list[i]
    print(f"{i}. {item.title()}")


