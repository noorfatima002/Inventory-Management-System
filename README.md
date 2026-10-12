# Inventory Management System

## Project Overview
This is a Python-based command-line application for managing inventory products and stock.

## Features
- Add, view, search, update, and delete products.
- Manage stock in and stock out.
- Calculate total inventory value.
- Generate low-stock reports.
- Save product information in JSON format.
- Validate user input.
- Automated testing with unittest.

## Technologies Used
- Python
- JSON
- Object-Oriented Programming
- unittest

## Requirements
- Python 3.10 or newer

## How to Run
Open a terminal in the project directory and execute:

```bash
python main.py
```

## Data Storage
Product data is stored in data/products.json.

## Run Automated Tests
Execute the following command from the project directory:

```bash
python -m unittest discover -s tests -v
```

## Project Structure
```text
inventory_management_system/
├── data/products.json
├── tests/test_inventory.py
├── inventory.py
├── main.py
├── models.py
├── storage.py
├── validators.py
└── README.md
```

## Conclusion
This project demonstrates Python programming, inventory management, JSON data storage, modular design, and automated testing.
