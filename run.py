shopping_list = []

# Adds an item to the shopping list

def add_item():
    stop = False
    while not stop:
        item = input("Enter the item you wish to add to the shopping list: ")
        shopping_list.append(item)
        print(item + " has been added to the shopping list.")
        user_input = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")
        if user_input == 'q':
            stop = True
    
add_item()

# Displays all items on the shopping list
def display_list():
    print()
    print("--- SHOPPING LIST ---")
    for i in shopping_list:
        print("* " + i)

display_list()

# Remove an item from the shopping list
def remove_item():
    item = input("Enter the item you wish to remove from the shopping list: ")
    shopping_list.remove(item)
    print(item + "has been removed from the shopping list.")


# Check to see if a particular item is on the shopping list
def check_item():
    item = input("What item would you like to check on the shopping list: ")
    if item in shopping_list:
        print("Yes, " + item + " is on the shopping list.")
    else:
        print("No, " + item + " is not on the shopping list.")
    input_other_item = input(f"Would you like to add {item} to the shopping list?\nType 'y' for yes or 'n' to not to add:\n")
    if input_other_item == 'y':
        shopping_list.append(item)
        print(f"{item} has been added to the shopping list.")
    else:
        print(f"{item}has not been added to the shopping list.")
    display_list()



check_item()
