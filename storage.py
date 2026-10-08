import json
import os

FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    "data",
    "products.json"
)


def load_products():
    if not os.path.exists(FILE_PATH):
        return []

    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_products(products):
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

    with open(FILE_PATH, "w") as file:
        json.dump(products, file, indent=4)

    return True