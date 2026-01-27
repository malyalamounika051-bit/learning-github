def collect_items(n):
    items = []
    for _ in range(n):
        # Keep asking until a non-empty name is entered
        while True:
            name = input("Enter item name: ").strip()
            if name != "":
                break
            print("Item name cannot be empty. Please try again.")
        
        # Keep asking until a valid float price is entered
        while True:
            price_input = input("Enter item price: ").strip()
            try:
                price = float(price_input)
                break
            except ValueError:
                print("Invalid price. Please enter a number.")
        
        items.append([name, price])
    return items

def print_items(items):
    total_price = 0
    for item in items:
        print(f"{item[0]}: ${item[1]}")
        total_price += item[1]
    print("Total price:", total_price)

# --- Main program ---
n = int(input("Enter number of items: "))
my_items = collect_items(n)
print_items(my_items)
