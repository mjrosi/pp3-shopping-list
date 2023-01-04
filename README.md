# SHOOD shopping list generator

SHOOD shopping list generator is a program for creating a shopping list. By this program is possible to add, remove, display the items in shopping list. Also the program allows the user to choose if they want to know if a specific item is in the list. Moreover, program shows the number of items in shopping list and has an option to clear all the items in the list.

![Start screen](/assets/screenshots/Screenshot_shoppinglist_app.jpg)

[Live webpage](https://pp3-shopping-list.herokuapp.com/)

## Table of Content

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
3. [Technical Design](#technical-design)
    1. [Flowchart](#flowchart)
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks-&-tools)
5. [Features](#features)
6. [Testing](#validation)
    1. [PEP8 validation](#pep8-validation)
7. [Deployment](#deployment)
8. [Credits](#credits)

## Project Goals 
The project goal is to create a shopping list generator using Python. The program can add, remove, edit items in a shopping list.

### User Goals
The application user wants to creat a shopping list by adding item to the list and/or removing items from the list. Showing a specific item in the list and the number of items in the list are other features of the program that user can use. User can empty the whole list.

## User Experience

### Target Audience
- Users that are inerested in a program for creating a shopping list for them.

## Technical Design

### Flowchart
![Flowchart](/assets/screenshots/shoppin_list_diagram.jpeg)


## Technologies Used

### Languages
- Python 3

### Frameworks & Tools
- Heroku
- pep8
- gitHub
- Gitpod
- Git

## Features

### Main Menu
- Shows the main menu with 7 options for the user to choose.
- Prompts a user to input a number between 1 to 7.
- The program validates the user entry. If the entry is not a number between 1 to 7, raise an error and asks the user to try again.
![Start screen](/assets/screenshots/Screenshot_shoppinglist_app.jpg)

### Add Items Input
- By choosing 1, user can add items to the list.
- After adding an item, user can continue add items by choosing 'y'.
- User can stop adding items to the list by choosing 'n'.
- By choosing 'n', programs will display the shopping list and the main menu.
- The program validates the user entry. If the entry is not 'n' or 'y', raise an error and asks the user to try again.

![Add Items](/assets/screenshots/Screenshot_add_item_function.png)

### View Shopping List 
- By choosing 2, the program displays added items in the shopping list.
- If the list is empty it tells the user that the shopping list is empty and asks the user if they want to add items.
- If the list is not empty it displays the shopping list and shows the main menu to give the user other option to select.

![View Shopping List](/assets/screenshots/Screenshot_view_shopping_list.png)
![View Shopping List if empty](/assets/screenshots/Screenshot_View_Shopping_List_empty.png)

### Remove item from shopping list
- By choosing 3, the program removes item from the shopping list by requesting the user to enter the item name.
- After removing the item, the programs displays the shopping list and the main menu.
- If the item is not in the shopping list raise an error and asks the user to try again.

![Remove Items](/assets/screenshots/Screenshot_remove_items.png)
![Remove Items not in the List](/assets/screenshots/Screenshot_remove_items_not_in_the_list.png)

### Check if item is on shopping list
- By choosing 4, the program allows the user to enter an item to check if the item is in the shopping list.
- If user enters an item which is not in the list, the program asks if the user wants to add the item to the list.

![Check Items](/assets/screenshots/Screenshot_check_item.png)

### How many items on shopping list
- By choosing 5, the program shows the numbers of the items in the shopping list.

![Number of Items](/assets/screenshots/Screenshot_number_of_items.png)

### Clear shopping list
- By choosing 6, the program clears the entire items in the shopping list.

![Clear the List](/assets/screenshots/Screenshot_clear_list.png)

### Exit
- By choosing 7, user exits the program.

![Exit the Program](/assets/screenshots/Screenshot_exit.png)

## Validator testing

### PEP8 validation
The code is checked in [pep8](https://pep8ci.herokuapp.com/).
No error has found.

## Deployment
Use the following steps to deploy the poject to Heroku:
1. Login or create a Heroku account.
2. Click the "New" button in the upper right corner and select "Create New App".
3. Choose an app name and your region and click "Create App". Note: the app name must be unique.
4. Go to the "Settings" tab, add the python build pack and then the node.js build pack. This is to ensure the project functions correctly with the Code Institute pre-installed template.
5. Go to the "Deploy" tab and pick GitHub as a deployment method.
6. Search for a repository to connect to.
7. Click enable automatic deploys and then deploy branch.
8. Wait for the app to build and then click on the "View" link.

## Credits

### Code
- Code Institute Python lessons.
- Code Institute Love Sandwiches project.
- for importing sys.exit() function. For importing sys.exit() function the code is taken from https://www.geeksforgeeks.org/python-exit-
    commands-quit-exit-sys-exit-and-os-_exit/.
