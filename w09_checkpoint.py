#Ask the user for the names of their friends and append them to a list. 
#Then, display each of the friends in the list. You should stop asking for friends when the user types "end".

friends = []

print("""Type the name of your friends, type "end" when you've finished.""")

add_names = input("Type the name of your friends: ")

while add_names.lower() != "end" :
    if add_names.lower() != "end" :
        friends.append(add_names)
    add_names = input("Type the name of your friends: ")

print()
print("Your friends are:")

for friend in friends   : 
    print(friend)