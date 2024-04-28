inventory = []
def add_item(item_name, quantity):
    inventory.append({"name": item_name, "quantity": quantity})
def remove_item(item_name):
    for item in inventory:
        if item["name"] == item_name:
            inventory.remove(item)
            break
    else:
        print(f"{item_name} not found in inventory.")
def display_inventory():
    print("Current Inventory:")
    for item in inventory:
        print(f"{item['name']} ({item['quantity']} units)")
add_item("Apples", 50)
add_item("Bananas", 30)
display_inventory()
remove_item("Bananas")
display_inventory()
