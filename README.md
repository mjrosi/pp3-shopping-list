# SHOOD shopping list generator
[Live webpage](https://pp3-shopping-list.herokuapp.com/)

SHOOD shopping list generator is a command line based Python program for creating a shopping list. This program create a shopping list by adding or remove items from the list. The program display the items in shopping list and also allows the user to know if a specific item is in the list. Moreover, program shows the number of items in shopping list and has an option to clear all the items in the list. The program calls a Google Workspace API to read and write data from it.

![Start screen](/assets/screenshots/Screenshot_shoppinglist_app.jpg)

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
The project goal is to create a shopping list generator using Python. The program can add, remove, edit items in a shopping list. The python program interacts with a Google Sheet to read and write data from it.

### User Goals
The application user can creat a shopping list by adding item to the list and/or removing items from it as well as items in the Google Sheets. Showing a specific item in the list and the number of items in the list are other features of the program that user can use. User can empty the whole list.

## User Experience

### Target Audience
- Users that are inerested in a program for creating a shopping list for them.

## Technical Design

### Flowchart
![Flowchart](/assets/screenshots/flowchart.png)

### Data Modelling
- The data stored in the Google Spreadsheet is a list that contains items from the shopping list. New items can be added or removed from the Google sheet.



## Technologies Used

### Languages
- Python 3

### Frameworks & Tools
- LucidChart
- Heroku
- Google Drive: Used as a cloud hosting platform for the spreadsheet.
- Google Spreadsheet: Used because Python does not have a built in library to store data in an external spreadsheet.
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
- By choosing 1, user can add items to the shopping list.
- The item also will be added to The Google Sheets.
- After adding an item, the user can continue add items by choosing 'y'.
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
- The item will be removed from The Google Sheet as well.
- If user entry is not in the shopping list raise an error and asks the user to try again.

![Remove Items](/assets/screenshots/Screenshot_remove_items.png)
![Remove Items not in the List](/assets/screenshots/Screenshot_remove_items_not_in_the_list.png)

### Check if item is on shopping list
- By choosing 4, the program allows the user to enter an item to check if the item is in the shopping list.
- If the user enters an item which is in the list, the program shows a message which YES, the entry is in the shopping list.
- The program validates the user entry for valid entry.
- If user enters an item which is not in the list, the program shows a message which NO, the entry is not in the shopping list.
- Then The program asks if the user wants to add the item which is not in the shopping list to the list by entering 'y' to add or 'n' to not to add.
- If the user enters 'y' the entry will be added to the shoping list and the Google Sheet.
- If the user enters 'n' the program shows a message which the entry is not added to the list.
- The program validates the user entry. If the entry is not 'n' or 'y', raise an error and asks the user to try again.

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
- To include the details on the project dependencies, the requirements.txt file is updated by entering this command in the terminal: `pip3 freeze > requirements.txt`
- Commit resulting changes to requirements.txt and push to GitHub.
- Login or create a new account on Heroku.
- Click on the Create New App button on the dashboard.
- Enter a unique name for the application, select the Europe as region and click the Create App button.
- In the Application Configuration page, click on the Settings tab and then scroll down to the Config Vars section to set up the credentials used by the application to access the spreadsheet data.
- Click Reveal Config Vars and enter ‘CREDS’ in the Key field. Copy and paste the entire contents of the creds.json file into the Value field and click Add.
- Next add ‘PORT’ in the next Key field and ‘8000’ in the Value field.
- Scroll down the Settings page to Buildpacks and click Add Buildpack. Select Python form the pop up window and click on Save Changes. Click Add Buildpack again, select Node.js from the pop up window and save. Make sure that Python is listed first and Node.js underneath.
- On the Application Configuration page, click on the Deploy tab.
Select GitHub as the Deployment Method and confirm that you want to connect to GitHub if prompted. Enter the name of the GitHub repository used for this project and click on Connect to link up the Heroku app to the GitHub repo.
- Scroll down to the Automatic Deploys section and click Enable Automatic Deploys or choose to Manually Deploy by clicking on Deploy Branch.
- Once the program runs, the message “The app was successfully deployed” will appear, click View. The application can also be run from the Application Configuration page by clicking on the Open App button.

## Credits

### Code
- Code Institute Python lessons.
- Code Institute Love Sandwiches project.
- for importing sys.exit() function. For importing sys.exit() function the code is taken from [here.](https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/)
- Check if string contains only Letters and Spaces from [here.](https://bobbyhadz.com/blog/python-check-if-string-contains-only-letters-and-spaces)
- While loop yes or no from [here.](https://tutorial.eyehunts.com/python/while-loop-yes-or-no-python-example-code/)