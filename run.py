import sys


shopping_list = []


# Adds an item to the shopping list
def add_item():
    """
    Get item input from the user to add to the shopping list.
    Run a while loop to collect a valid input from the user
    via the terminal, which must be a string.
    The loop will repeatedly request input item, until it stop by user
    by inserting q.
    """
    stop = False
    while not stop:
        item = input("Enter the item you wish to add to the shopping list: ")
        if item.capitalize() not in shopping_list:
            shopping_list.append(item.capitalize())
            print(f"{item.capitalize()} has been added to the shopping list.")
        else:
            print(f"{item.capitalize()} is already in the shopping list")
       
        user_input = input("\nWould you like to add another item?\nType 'c' to continue or 'q' to quit:\n")
        if user_input == 'q':
            stop = True
            display_list()
        elif user_input == 'c':
            stop = False
        else:
            print("Invalid input! Please try again.\n")
            user_input = input("\nWould you like to add another item?\nType 'c' to continue or 'q' to quit:\n")


# Displays all items on the shopping list
def display_list():
    """
    Display added items to shopping list.
    Run a if condition which if the list empty shows the the shopping list is
    empty and asks user to add items by calling the function add_item().
    If th list is not empty display the shopping list and calling
    the main function for gives the user other option to select.
    """
    if len(shopping_list) == 0:
        print("The shopping list is empty.\n")
        input_empty_list_item = input("Would you like to add an item to the shopping list?\nType 'y' for to add or 'n' to not to add:\n")
        if input_empty_list_item == 'y':
            add_item()
            main()
        else:
            main()
    else:
        print("--- SHOPPING LIST ---\n")
        for i in shopping_list:
            print("* " + i)
        print("\n---------------------")
        main()


# Remove an item from the shopping list
def remove_item():
    item = input("Enter the item you wish to remove from the shopping list: ")
    shopping_list.remove(item.capitalize())
    print(f"{item.capitalize()} has been removed from the shopping list.\n")
    display_list()


# Check to see if a particular item is on the shopping list
def check_item():
    item = input("What item would you like to check on the shopping list: ")
    if item.capitalize() in shopping_list:
        print(f"Yes, {item.capitalize()} is on the shopping list.")
    else:
        print(f"No, {item.capitalize()} is not on the shopping list.")
        input_other_item = input(f"Would you like to add {item.capitalize()} to the shopping list?\nType 'y' for to add or 'n' to not to add:\n")
        if input_other_item == 'y':
            shopping_list.append(item)
            print(f"{item.capitalize()} has been added to the shopping list.")
        else:
            print(f"{item.capitalize()} has not been added to the shopping list.")
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
    print('''### WELCOME TO SHOOD SHOPPING LIST GENERATOR###

        Select a number for the action that you would like to do:

        1. Add item to shopping list
        2. View shopping list
        3. Remove item from shopping list
        4. Check if item is on shopping list
        5. How many items on shopping list
        6. Clear shopping list
        7. Exit
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
        print('Thanks for using SHOOD shopping list generator!')
        sys.exit()
    else:
        print("You did not make a valid selection. Please try again.")
        main()


# Run the function main - which will run the program
main()