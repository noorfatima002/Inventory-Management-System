def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty.")


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value < 0:
                print("Quantity cannot be negative.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value < 0:
                print("Price cannot be negative.")
                continue

            return value

        except ValueError:
            print("Please enter a valid price.")