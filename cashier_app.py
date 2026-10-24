basket = []

def show_basket(basket):
    """Print all items currently in the basket"""
    print()
    print("Current basket:")
    print()

    if not basket:
        print("The basket is empty.")
    else:
        for item in basket:
            name, price, quantity = item
            subtotal = price * quantity
            print(f"{name} - €{price:.2f} x {quantity} = €{subtotal:.2f}")

        total = sum(item[1] * item[2] for item in basket)
        print()
        print(f"Total: €{total:.2f}")

    print()
    print("Options: add / remove / checkout / quit")


def prompt_for_item():
    """Prompt the user for an item's name, price and quantity"""
    name = input("Enter the item name: ").strip().title()
    price = float(input("Enter the price: €"))
    quantity = int(input("Enter the quantity: "))

    return name, price, quantity


def add_item(basket):
    """Add an item to the basket"""
    name, price, quantity = prompt_for_item()

    if price < 0 or quantity <= 0:
        print("Price cannot be negative and quantity must be positive.")
        return

    basket.append((name, price, quantity))
    print()
    print(f"{quantity} x {name} added to the basket.")


def remove_item(basket):
    """Remove an item from the basket"""
    name = input("Enter the item to remove: ").strip().title()

    for item in basket:
        if item[0] == name:
            basket.remove(item)
            print(f"{name} has been removed from the basket.")
            return

    print(f"{name} is not in the basket.")


def checkout(basket):
    """Calculate the total, accept payment and give change"""
    if not basket:
        print("The basket is empty. Add some items first.")
        return

    total = sum(item[1] * item[2] for item in basket)

    print()
    print("=" * 35)
    print("         RECEIPT          ")
    print("=" * 35)

    for item in basket:
        name, price, quantity = item
        subtotal = price * quantity
        print(f"{name}: {quantity} x €{price:.2f} = €{subtotal:.2f}")

    print("-" * 35)
    print(f"TOTAL: €{total:.2f}")

    

def run_app(basket):
    print("=" * 40)
    print()
    print("Welcome to Python Cash Register")
    print()
    print("=" * 40)

    is_running = True

    while is_running:
        show_basket(basket)
        print()

        command = input("> ").lower().strip()

        if command == "quit":
            is_running = False
            print("Goodbye!")

        elif command == "add":
            add_item(basket)
           # try:
                
        
        elif command == "remove":
            remove_item(basket)

        elif command == "checkout":
            checkout(basket)

        else:
            print(f"Sorry, I don't know '{command}'.")


run_app(basket)