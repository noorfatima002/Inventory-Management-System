from storage import load_products, save_products


class Inventory:

    def __init__(self):
        self.products = load_products()

    def add_product(self, product):
        for item in self.products:
            if item["product_id"] == product.product_id:
                return False, "Product ID already exists."

        self.products.append(product.to_dict())
        save_products(self.products)

        return True, "Product added successfully."

    def get_all_products(self):
        return self.products

    def search_product(self, keyword):
        keyword = keyword.lower()

        results = []

        for product in self.products:
            if (
                keyword in product["product_id"].lower()
                or keyword in product["name"].lower()
                or keyword in product["category"].lower()
            ):
                results.append(product)

        return results

    def update_product(self, product_id, name, category, quantity, price):
        for product in self.products:
            if product["product_id"] == product_id:

                product["name"] = name
                product["category"] = category
                product["quantity"] = quantity
                product["price"] = price

                save_products(self.products)

                return True, "Product updated successfully."

        return False, "Product not found."

    def delete_product(self, product_id):
        for product in self.products:
            if product["product_id"] == product_id:

                self.products.remove(product)
                save_products(self.products)

                return True, "Product deleted successfully."

        return False, "Product not found."

    def stock_in(self, product_id, quantity):
        for product in self.products:
            if product["product_id"] == product_id:

                if quantity <= 0:
                    return False, "Quantity must be greater than 0."

                product["quantity"] += quantity
                save_products(self.products)

                return True, "Stock added successfully."

        return False, "Product not found."

    def stock_out(self, product_id, quantity):
        for product in self.products:
            if product["product_id"] == product_id:

                if quantity <= 0:
                    return False, "Quantity must be greater than 0."

                if quantity > product["quantity"]:
                    return False, "Not enough stock available."

                product["quantity"] -= quantity
                save_products(self.products)

                return True, "Stock removed successfully."

        return False, "Product not found."

    def total_inventory_value(self):
        total = 0

        for product in self.products:
            total += product["quantity"] * product["price"]

        return total

    def low_stock(self, threshold=5):
        return [
            product
            for product in self.products
            if product["quantity"] <= threshold
        ]