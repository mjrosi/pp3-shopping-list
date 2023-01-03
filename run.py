shopping_list = []

# Adds an item to the shopping list
def add_item():
    stop = False
    while not stop:
        item = input("Enter the item you wish to add to the shopping list: ")
        shopping_list.append(item)
        print(f"{item} has been added to the shopping list.")
        user_input = input("Would you like to add another item?\nType 'c' to continue or 'q' to quit:\n")
        if user_input == 'q':
            stop = True


# Displays all items on the shopping list
def display_list():
    print()
    print("--- SHOPPING LIST ---")
    for i in shopping_list:
        print("* " + i)


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
            print(f"{item} has not been added to the shopping list.")
    display_list()

# How many items are on the shopping list        
def shopping_list_length():
    number_of_items = len(shopping_list)
    print(f"There are {number_of_items} items on the shopping list.")


# Remove everything from the shopping list
def clear_shopping_list():
    shopping_list.clear()
    print("The shopping list is now empty.")


def main():
    while True:
        print()
        print('''### SHOPPING LIST ###

        Select a number for the action that you would like to do:

        1. Add item to shopping list
        2. View shopping list
        3. Remove item from shopping list
        4. Check if item is on shopping list
        5. How many items on shopping list
        6. Clear shopping list
        ''')

        # Ask the user to make a selection
        selection = input("Make your selection: ") 

        # Determine which action to perform based on the user's selection
        if selection == "1":
            add_item()            
        elif selection == "2":
            display_list()
        elif selection == "3":
            remove_item()
        elif selection == "4":
            check_item()
        elif selection == "5":
            shopping_list_length()
        elif selection == "6":
            clear_shopping_list()
        elif selection == "7":
            sys.exit()
        else:
            print("You did not make a valid selection.")


# Run the function mainMenu - which will run our app    
main()