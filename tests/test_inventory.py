import unittest
from unittest.mock import patch

from inventory import Inventory
from models import Product


class TestInventory(unittest.TestCase):

    def setUp(self):
        self.load_patcher = patch(
            "inventory.load_products",
            return_value=[]
        )
        self.save_patcher = patch("inventory.save_products")

        self.load_patcher.start()
        self.mock_save = self.save_patcher.start()

        self.addCleanup(self.load_patcher.stop)
        self.addCleanup(self.save_patcher.stop)

        self.inventory = Inventory()

    def test_add_product(self):
        product = Product("P001", "Laptop", "Electronics", 10, 50000)

        success, message = self.inventory.add_product(product)

        self.assertTrue(success)
        self.assertEqual(len(self.inventory.products), 1)
        self.assertEqual(self.inventory.products[0]["name"], "Laptop")
        self.mock_save.assert_called_once()

    def test_duplicate_product_id(self):
        product = Product("P001", "Laptop", "Electronics", 10, 50000)

        self.inventory.add_product(product)
        success, message = self.inventory.add_product(product)

        self.assertFalse(success)
        self.assertEqual(len(self.inventory.products), 1)

    def test_stock_in(self):
        product = Product("P001", "Laptop", "Electronics", 10, 50000)
        self.inventory.add_product(product)

        success, message = self.inventory.stock_in("P001", 5)

        self.assertTrue(success)
        self.assertEqual(self.inventory.products[0]["quantity"], 15)

    def test_stock_out(self):
        product = Product("P001", "Laptop", "Electronics", 10, 50000)
        self.inventory.add_product(product)

        success, message = self.inventory.stock_out("P001", 3)

        self.assertTrue(success)
        self.assertEqual(self.inventory.products[0]["quantity"], 7)

    def test_stock_out_insufficient_quantity(self):
        product = Product("P001", "Laptop", "Electronics", 5, 50000)
        self.inventory.add_product(product)

        success, message = self.inventory.stock_out("P001", 10)

        self.assertFalse(success)
        self.assertEqual(self.inventory.products[0]["quantity"], 5)

    def test_total_inventory_value(self):
        self.inventory.add_product(
            Product("P001", "Laptop", "Electronics", 2, 50000)
        )
        self.inventory.add_product(
            Product("P002", "Mouse", "Electronics", 3, 1000)
        )

        self.assertEqual(
            self.inventory.total_inventory_value(),
            103000
        )

    def test_low_stock_report(self):
        self.inventory.add_product(
            Product("P001", "Mouse", "Electronics", 3, 1000)
        )
        self.inventory.add_product(
            Product("P002", "Laptop", "Electronics", 10, 50000)
        )

        result = self.inventory.low_stock()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["product_id"], "P001")

    def test_delete_product(self):
        self.inventory.add_product(
            Product("P001", "Laptop", "Electronics", 10, 50000)
        )

        success, message = self.inventory.delete_product("P001")

        self.assertTrue(success)
        self.assertEqual(len(self.inventory.products), 0)

    def test_search_product(self):
        self.inventory.add_product(
            Product("P001", "Laptop", "Electronics", 10, 50000)
        )

        result = self.inventory.search_product("laptop")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["product_id"], "P001")


if __name__ == "__main__":
    unittest.main()
