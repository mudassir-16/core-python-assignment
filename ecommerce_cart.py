def calculate_total_price(cart_items):
    if not cart_items:
        return 0
    total = sum(cart_items.values())
    if len(cart_items) > 5:
        total *= 0.9
    return total


cart = {}
n = int(input("Enter number of items: "))

for _ in range(n):
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    cart[name] = price

print("Total Price:", int(calculate_total_price(cart)))
