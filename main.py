from models import Product
from inventory import Inventory
from validators import (
    get_non_empty,
    get_positive_int,
    get_positive_float
)


inventory = Inventory()


def display_products(products):
    if not products:
        print("\nNo products found.")
        return

    print("\n" + "=" * 80)
    print(
        f"{'ID':<12}"
        f"{'Name':<20}"
        f"{'Category':<15}"
        f"{'Qty':<8}"
        f"{'Price':<10}"
    )
    print("=" * 80)

    for product in products:
        print(
            f"{product['product_id']:<12}"
            f"{product['name']:<20}"
            f"{product['category']:<15}"
            f"{product['quantity']:<8}"
            f"{product['price']:<10.2f}"
        )

    print("=" * 80)


def add_product():
    print("\n--- Add Product ---")

    product_id = get_non_empty("Enter Product ID: ")
    name = get_non_empty("Enter Product Name: ")
    category = get_non_empty("Enter Category: ")
    quantity = get_positive_int("Enter Quantity: ")
    price = get_positive_float("Enter Price: ")

    product = Product(
        product_id,
        name,
        category,
        quantity,
        price
    )

    success, message = inventory.add_product(product)
    print(message)


def view_products():
    print("\n--- All Products ---")

    products = inventory.get_all_products()
    display_products(products)


def search_product():
    print("\n--- Search Product ---")

    keyword = get_non_empty("Enter ID, name or category: ")

    results = inventory.search_product(keyword)

    display_products(results)


def update_product():
    print("\n--- Update Product ---")

    product_id = get_non_empty("Enter Product ID: ")

    name = get_non_empty("Enter New Name: ")
    category = get_non_empty("Enter New Category: ")
    quantity = get_positive_int("Enter New Quantity: ")
    price = get_positive_float("Enter New Price: ")

    success, message = inventory.update_product(
        product_id,
        name,
        category,
        quantity,
        price
    )

    print(message)


def delete_product():
    print("\n--- Delete Product ---")

    product_id = get_non_empty("Enter Product ID: ")

    success, message = inventory.delete_product(product_id)

    print(message)


def stock_in():
    print("\n--- Stock In ---")

    product_id = get_non_empty("Enter Product ID: ")
    quantity = get_positive_int("Enter Quantity to Add: ")

    success, message = inventory.stock_in(
        product_id,
        quantity
    )

    print(message)


def stock_out():
    print("\n--- Stock Out ---")

    product_id = get_non_empty("Enter Product ID: ")
    quantity = get_positive_int("Enter Quantity to Remove: ")

    success, message = inventory.stock_out(
        product_id,
        quantity
    )

    print(message)


def inventory_value():
    print("\n--- Total Inventory Value ---")

    total = inventory.total_inventory_value()

    print(f"Total Inventory Value: {total:.2f}")


def low_stock_report():
    print("\n--- Low Stock Report ---")

    products = inventory.low_stock()

    display_products(products)


def main():
    while True:

        print("\n")
        print("=" * 40)
        print("   INVENTORY MANAGEMENT SYSTEM")
        print("=" * 40)

        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Stock In")
        print("7. Stock Out")
        print("8. Total Inventory Value")
        print("9. Low Stock Report")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            stock_in()

        elif choice == "7":
            stock_out()

        elif choice == "8":
            inventory_value()

        elif choice == "9":
            low_stock_report()

        elif choice == "0":
            print("\nThank you for using Inventory Management System!")
            break

        else:
            print("\nInvalid choice. Please select 0-9.")


if __name__ == "__main__":
    main()