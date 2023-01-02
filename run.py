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
    print(item + " has been removed from the shopping list.")