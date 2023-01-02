shopping_list = []

# Adds an item to the shopping list

def add_item():
    item = input("Enter the item you wish to add to the shopping list: ")
    shopping_list.append(item)
    print(item + " has been added to the shopping list.")
    
add_item()