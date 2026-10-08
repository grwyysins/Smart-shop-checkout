products = {
    "P001": {"name": "Notebook", "price": 300},
    "P002": {"name": "Desktop", "price": 15000},
    "P003": {"name": "Phone Cover", "price": 6000},
    "P004": {"name": "Keyboard", "price": 2700},
    "P005": {"name": "Laptop Bag", "price": 1400}
}
basket = {}   

def display_products():
    print("\n========== PRODUCT MENU ==========")

    for code, product in products.items():
        print(
            f"{code} - {product['name']} - "
            f"KSh {product['price']:.2f}"
        )

    print("==================================")

def add_to_basket():
    display_products()

    code = input("Enter the product code: ").upper()

    if code not in products:
        print("Invalid product code.")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid whole number.")
        return

    if code in basket:
        basket[code] += quantity
    else:
        basket[code] = quantity

    print(
        f"{quantity} x {products[code]['name']} "
        f"added to your basket."
    )

def calculate_totals():

    subtotal = 0

    for code, quantity in basket.items():

        price = products[code]["price"]

        line_total = price * quantity

        subtotal += line_total

    if subtotal >= 20000:
        discount_rate = 0.5
    elif subtotal >= 15000:
        discount_rate = 0.25
    elif subtotal >= 13000:
        discount_rate = 0.15
    else:
        discount_rate = 0

    discount = subtotal * discount_rate

    total = subtotal - discount

    return subtotal, discount, total

def view_basket():

    if not basket:
        print("\nYour basket is empty.")
        return

    print("\n========== YOUR BASKET ==========")

    for code, quantity in basket.items():

        product = products[code]

        line_total = product["price"] * quantity

    subtotal, discount, total = calculate_totals()

    print("---------------------------------")
    print(f"Subtotal: KSh {subtotal:.2f}")
    print(f"Discount: KSh {discount:.2f}")
    print(f"Final Total: KSh {total:.2f}")
    print("=================================")

def remove_item():

    if not basket:
        print("\nYour basket is empty.")
        return

    view_basket()

    code = input(
        "\nEnter the product code to remove: "
    ).upper()

    if code in basket:

        del basket[code]

        print("Item removed successfully.")

    else:

        print("That item is not in your basket.")

def process_payment(total):

    while True:

        try:

            payment = float(
                input("Enter payment amount: KSh ")
            )

            if payment < 0:
                print("Payment cannot be negative.")
                continue

            if payment < total:

                print(
                    f"Insufficient payment. "
                    f"You need KSh {total - payment:.2f} more."
                )

                continue

            change = payment - total

            return payment, change

        except ValueError:

            print("Please enter a valid money amount.")

def print_receipt(payment, change):

    subtotal, discount, total = calculate_totals()

    print("\n")
    print("========================================")
    print("          SMART SHOP RECEIPT")
    print("========================================")

    for code, quantity in basket.items():

        product = products[code]

        line_total = product["price"] * quantity

        print(
            f"{product['name']} x {quantity} "
            f"= KSh {line_total:.2f}"
        )

    print("----------------------------------------")
    print(f"Subtotal:       KSh {subtotal:.2f}")
    print(f"Discount:       KSh {discount:.2f}")
    print(f"TOTAL:          KSh {total:.2f}")
    print(f"Payment:        KSh {payment:.2f}")
    print(f"Change:         KSh {change:.2f}")
    print("========================================")
    print("       THANK YOU FOR SHOPPING!")
    print("========================================")

print("========================================")
print("       WELCOME TO SMART SHOP")
print("========================================")

while True:

    print("\n========== MAIN MENU ==========")
    print("1. Add item to basket")
    print("2. View basket")
    print("3. Remove item")
    print("4. Checkout")
    print("5. Exit")
    print("===============================")

    choice = input("Choose an option: ")

    if choice == "1":
        add_to_basket()

    elif choice == "2":
        view_basket()

    elif choice == "3":
        remove_item()

    elif choice == "4":
        if not basket:
            print("Your basket is empty.")
            print("Please add an item before checkout.")

        else:
            subtotal, discount, total = calculate_totals()

            print("\n========== CHECKOUT ==========")
            print(f"Subtotal: KSh {subtotal:.2f}")
            print(f"Discount: KSh {discount:.2f}")
            print(f"Total to pay: KSh {total:.2f}")

            payment, change = process_payment(total)
            print_receipt(payment, change)
            print("\nThank you for shopping with us!")
            break

    elif choice == "5":
        print("Thank you for visiting Smart Shop!")
        break

    else:
        print("Invalid choice. Please select 1-5.")