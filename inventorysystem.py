# Initialize an empty inventory list
inventory = []

def add_item(item_name, quantity):
    # Add an item to the inventory
    inventory.append({"name": item_name, "quantity": quantity})

def remove_item(item_name):
    # Remove an item from the inventory
    for item in inventory:
        if item["name"] == item_name:
            inventory.remove(item)
            break
    else:
        print(f"{item_name} not found in inventory.")

def display_inventory():
    # Display the current inventory
    print("Current Inventory:")
    for item in inventory:
        print(f"{item['name']} ({item['quantity']} units)")

# Example usage
add_item("Apples", 50)
add_item("Bananas", 30)
display_inventory()
remove_item("Bananas")
display_inventory()
