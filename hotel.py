menu = {
    'burger': {'price': 400, 'available': True},
    'pizza': {'price': 600, 'available': True},
    'spaghetti': {'price': 800, 'available': True},
    'noodles': {'price': 700, 'available': False},
    'punjabi': {'price': 400, 'available': True},
    'sizzler': {'price': 900, 'available': False}
}

order_book = {}
max_table = 10

def display_menu():
    print("\nRestaurant Menu:")
    for item, details in menu.items():
        status = "Available" if details['available'] else "Not Available"
        print(f"{item.capitalize()} - ₹{details['price']} ({status})")

def place_order():
    try:
        table_id = int(input("Enter the table ID (1-10): "))
        if table_id < 1 or table_id > max_table:
            print("Invalid table number. Try again.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    if table_id not in order_book:
        order_book[table_id] = []

    display_menu()
    food_item = input("Enter the food item you would like to order: ").strip().lower()
    if food_item not in menu:
        print("Item not found in menu.")
        return
    if not menu[food_item]['available']:
        print("Sorry, this item is currently not available.")
        return

    try:
        quantity = int(input("Enter the quantity: "))
        if quantity < 1:
            print("Quantity must be at least 1.")
            return
    except ValueError:
        print("Please enter a valid number for quantity.")
        return

    for order in order_book[table_id]:
        if order['fooditem'] == food_item:
            order['quantity'] += quantity
            print("Order updated.")
            return

    order_book[table_id].append({'fooditem': food_item, 'quantity': quantity})
    print("Order added.")

def calculate_order():
    total_bill = 0
    print("\nOrders Summary:")
    for table_id, orders in order_book.items():
        print(f"\nTable {table_id}:")
        for order in orders:
            food_item = order['fooditem']
            quantity = order['quantity']
            price = menu[food_item]['price']
            subtotal = price * quantity
            total_bill += subtotal
            print(f" - {food_item.capitalize()} x {quantity} = ₹{subtotal}")
    print(f"\nTotal bill for all tables: ₹{total_bill}")
    return total_bill

while True:
    print("\n1. Place Order")
    print("2. Calculate Total Bill")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number from 1 to 3.")
        continue

    if choice == 1:
        place_order()
    elif choice == 2:
        calculate_order()
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please select between 1 and 3.")
