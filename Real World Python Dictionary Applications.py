#Question 1

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

def add_category(menu, category):
    if category not in menu:
        menu[category]={}
        print(f"Category: {category} has been added to the menu.")
    else:
        print(f"Category: {category} is already on the menu.")

def add_items(menu, category, item, price):
    if category in menu:
        menu[category][item]= price
        print(f"Item: {item} has been added to {category}.")
        
    else:
        print(f"Category: {category} doesnt exist in menu.") 

def update_item_price(menu, category, item, new_price):
    menu[category].update({item: new_price})
    print(f"{item}'s price has been updated.")
     

def remove_item(menu, category, item):
    menu[category].pop(item)
    print(f"Item: {item} removed from {category}.")         


add_category(restaurant_menu, "Beverages")
add_items(restaurant_menu, "Beverages", "Coca-Cola", 2.00)
add_items(restaurant_menu, "Beverages", "Iced Tea", 1.5) 
update_item_price(restaurant_menu, "Main Course", "Steak", 17.99)
remove_item(restaurant_menu, "Starters", "Bruschetta")

print(restaurant_menu)