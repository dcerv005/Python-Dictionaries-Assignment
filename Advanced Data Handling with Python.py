#Question 2 Task 1

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def book_room(rooms, room, customer):
    if rooms[room]['status'] != "booked":
        rooms[room]['status'] = 'booked'
        rooms[room]['customer']= customer
        print(f"{customer} has booked room: {room}.")
    else:
        print(f"Room: {room} is not available")
    
def check_out(rooms, room, customer):
    checked_out= {"status": "available", "customer": ""}
    if customer in rooms[room]['customer']:        
        rooms[room].update(checked_out)
        print(f"{customer} has checked out of room: {room}.")
    else:
        print(f"{customer} is not staying in room: {room}")
def display(rooms):
    for room, information in rooms.items():
        print(f"Room: {room}")
        print(rooms[room]['status'])


book_room(hotel_rooms, "101", "David")
book_room(hotel_rooms, "102", "Coding Temple")
check_out(hotel_rooms, "101", "David")
check_out(hotel_rooms, "102", "Coding Temple")
display(hotel_rooms)

#Task 2
def get_product(products, name):
    item_found = False
    for product, details in products.items():
        if products[product].get("name", "").lower() == name.lower():
            print(f"{name} is in product: {product}")
            item_found = True
            break
    if not item_found:
        print("Item not found in list")
  
        
products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20}
}

get_product(products, "laptop")