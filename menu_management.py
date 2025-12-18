def add_item(menu, item):
    if item not in menu:
        menu.append(item)


def remove_item(menu, item):
    if item in menu:
        menu.remove(item)


def check_item(menu, item):
    return f"{item} is available" if item in menu else f"{item} is not available"


menu = input("Enter initial menu items separated by comma: ").split(",")

add_item_name = input("Enter item to add: ")
remove_item_name = input("Enter item to remove: ")
check_item_name = input("Enter item to check: ")

add_item(menu, add_item_name)
remove_item(menu, remove_item_name)

print("Updated menu:", menu)
print("Availability:", check_item(menu, check_item_name))
