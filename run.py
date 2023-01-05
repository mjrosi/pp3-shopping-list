import gspread
from google.oauth2.service_account import Credentials
import sys
"""
    code is taken from https://www.geeksforgeeks.org/python-exit-
    commands-quit-exit-sys-exit-and-os-_exit/.
    for importing sys.exit() function.
"""
import time  # for importing sys.exit() function.


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
        while True:
            item = input("Enter the item you wish to add to the shopping list: \n")
            if not item.isalpha():
                print('Invalid Entry! Please enter only letters, like: eggs\n')
                continue
            else:
                if item.capitalize() not in shopping_list:
                    shopping_list.append(item.capitalize())
                    list.append_row([item.capitalize()])
                    print(f"\n{item.capitalize()} has been added to the shopping list.")
                    time.sleep(2.5)
                else:
                    print(f"{item.capitalize()} is already in the shopping list")
            user_input = None 
            while user_input not in ("y", "n"):
                user_input = input("""\nWould you like to add another item?\n
Type 'y' to add or 'n' to back to the main menu:\n""")
                if user_input == 'n':
                    stop = True
                    display_list()
                    time.sleep(2.5)
                elif user_input == 'y':
                    stop = False
                else:
                    print("Invalid input! Please try again.\n")


# Displays all items on the shopping list
def display_list():
    """
    Displays added items in the shopping list.
    Runs an if condition which if the list empty shows the the shopping list is
    empty and asks user to add items by calling the function add_item().
    If the list is not empty display the shopping list and calling
    the main function to give the user other option to select.
    """
    if len(shopping_list) == 0:
        print("The shopping list is empty.\n")
        input_empty_list_item = input("""Would you like to add an item to
the shopping list?\nType 'y' for to add or 'n' to not to add:\n""")
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
        time.sleep(2.5)
        main()


# Remove an item from the shopping list
def remove_item():
    """
    Removes item from the shopping list by requesting
    the user to enter the item name.
    If the item is not in the shopping list raise an error
    and asks the user to try again.
    """
    while True:
        item = input("""Enter the item you wish
to remove from the shopping list:""")
        if item.capitalize() in shopping_list:
            list.delete_rows(2, len(shopping_list) + 1)
            shopping_list.remove(item.capitalize())
            for shopping_item in shopping_list:
                list.append_row([shopping_item])
            print('\nRemoving the item ...')
            time.sleep(2)
            print(f"""\n{item.capitalize()} has been removed from
the shopping list.\n""")
            time.sleep(2.5)
            display_list()
            break
        else:
            print(f"""\n{item.capitalize()} is not in the shopping list. Please
try again.\n""")


# Check to see if a particular item is on the shopping list
def check_item():
    """
    Requests user to enter an item to check if the item
    is in the shopping list.
    If user enters an item which is not in the list, asks
    if the user wants to add the item to the list.
    """
    while True:
        item = input("What item would you like to check on the shopping list: ")
        if not item.isalpha():
            print('\nInvalid Entry! Please enter only letters, like eggs.\n')
            continue
        elif item.capitalize() in shopping_list and item.isalpha():
            print(f"\nYes, {item.capitalize()} is on the shopping list.\n")
            time.sleep(2)
            display_list()
        else:
            print(f"\nNo, {item.capitalize()} is not on the shopping list.\n")
        answer = None
        while answer not in ("y", "n"):
            answer = input(f"""Would you like to add {item.capitalize()}
to the shopping list?\nType 'y' for to add or 'n' to not to add:\n""")
            if answer == 'y':
                shopping_list.append(item.capitalize())
                list.append_row([item.capitalize()])
                print(f"\n{item.capitalize()} has been added to the shopping list.")
                time.sleep(2.5)
                display_list()
                return False
            elif answer == 'n':
                print(f"""\n{item.capitalize()} has not been added to
the shopping list.\n""")
                display_list()
                return False
            else:
                print("Invalid input! Please enter y or n.\n")


# How many items are on the shopping list
def shopping_list_length():
    """
    Shows the numbers of the items in the shopping list.
    """
    number_of_items = len(shopping_list)
    print(f"\nThere are {number_of_items} items on the shopping list.\n")
    display_list()


# Remove everything from the shopping list
def clear_shopping_list():
    """
    Clears the entire items in the shopping list.
    """
    list.delete_rows(2, len(shopping_list) + 1)
    shopping_list.clear()
    print("The shopping list is now empty.")


def main():
    """
    The main function which runs the program.
    """
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
    while True:
        try:
            selection = int(input("""Make a selection by choosing a number
from 1-7: """))
        except ValueError:
            print("Invalid entry! Please choose a number from 1-7.\n")
            continue
        # Determine which action to perform based on the user's selection
        if selection == 1:
            add_item()
        elif selection == 2:
            display_list()
        elif selection == 3:
            remove_item()
        elif selection == 4:
            check_item()
        elif selection == 5:
            shopping_list_length()
        elif selection == 6:
            clear_shopping_list()
        elif selection == 7:
            print('Thanks for using SHOOD shopping list generator!\n')
            sys.exit()
        else:
            print("You did not make a valid selection. Please try again.\n")


if __name__ == "__main__":
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
        ]

    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open('shopping_list')
    list = SHEET.worksheet('list')
    data = list.get_all_values()[1:]
    shopping_list = [str(x[0]) for x in data]
    # Run the function main - which will run the program
    main()
