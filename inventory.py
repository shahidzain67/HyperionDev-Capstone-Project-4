"""
Warehouse management system to manage the following variables and allow managers to manage costs and stock:
- Country
- Code
- Product
- Cost
- Quantity
- Value
"""


class Shoes:
    # Base shoes class
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        # return cost of shoe
        return self.cost

    def get_quantity(self):
        # return quantity of shoes
        return self.quantity

    def __str__(self):
        # return string representation of class
        return (
            self.country
            + ","
            + self.code
            + ","
            + self.product
            + ","
            + self.cost
            + ","
            + self.quantity
        )


def read_shoes_data():
    # read inventory file and store each line as a shoe object in the shoe_objects list
    try:
        # confirm file exists
        with open("inventory.txt", "r") as f:
            next(f)
            lines = f.readlines()  # read file as list of lines
            list_of_shoes = []
            try:
                # confirm file is in correct format and no variables are missing
                for x in lines:
                    variables = x.split(",")  # split line into list of variables
                    country = variables[0]
                    code = variables[1]
                    product = variables[2]
                    cost = variables[3]
                    quantity = variables[4]
                    shoe = Shoes(
                        country, code, product, cost, quantity
                    )  # create new object
                    list_of_shoes.append(shoe)  # add new object to shoe_objects list
                print("File read successfully.")
                return list_of_shoes
            except:
                "inventory.txt has an error."
    except:
        print("inventory.txt file not found.")


def capture_shoes(shoe_objects):
    # add a new shoe object to the shoe_objects list
    country = input("Please enter a country: ")
    code = input("Please enter a code: ")
    product = input("Please enter a product: ")
    cost = input("Please enter a cost: ")
    quantity = input("Please enter a quantity: ")
    shoe = Shoes(country, code, product, cost, quantity)  # create new object
    shoe_objects.append(shoe)  # add new object to shoe_objects list
    with open("inventory.txt", "a") as f:
        f.write(f"\n{country},{code},{product},{cost},{quantity}")


def view_all(shoe_objects):
    # iterate through all shoe objects and print object data
    for shoe in shoe_objects:
        print(shoe.__str__())


def re_stock(shoe_objects):
    # find the shoe object with the lowest quantity, ask the user if he wants to add to this and update inventory.txt

    # find lowest quantity
    min_quantity = int(shoe_objects[0].quantity.strip())
    min_shoe = shoe_objects[0].product.strip()
    for shoe in shoe_objects:
        if int(shoe.quantity.strip()) < min_quantity:
            min_quantity = int(shoe.quantity.strip())
            min_shoe = shoe

    # prompt user to change quantity and update file
    new_quantity = int(input(f"Please update the quantity of {min_shoe.product}: "))

    with open("inventory.txt", "r") as f:
        lines = f.readlines()  # read file as list of lines
    with open("inventory.txt", "w+") as f:
        for count, item in enumerate(lines):
            # find correct line and overwrite quantity
            if min_shoe.code in item:
                lines[
                    count
                ] = f"{min_shoe.country},{min_shoe.code},{min_shoe.product},{min_shoe.cost},{new_quantity}\n"
        f.writelines(lines)

    print(f"Quantity of {min_shoe.product} updated to {new_quantity}")


def search_shoe(code, shoe_objects):
    # returns shoe object depending on the code entered
    for shoe in shoe_objects:
        if shoe.code == code:
            return shoe

    return "No shoe found"


def value_per_item(code, shoe_objects):
    # prints value of each shoe
    for shoe in shoe_objects:
        if code in shoe.code:
            total = int(shoe.cost) * int(shoe.quantity.strip())
            print(f"{shoe.product} value = {total}")


def highest_qty(shoe_objects):
    # finds shoe with maximum quantity and prints this shoe as being for sale
    max_quantity = int(shoe_objects[0].quantity.strip())
    max_shoe = shoe_objects[0].product
    for shoe in shoe_objects:
        if int(shoe.quantity.strip()) > max_quantity:
            max_quantity = int(shoe.quantity.strip())
            max_shoe = shoe
    print(f"{max_shoe.product.strip()} is for sale")


shoe_objects = []
usage_message = """
Welcome to the Nike warehouse system! What would you like to do?

a - read shoes data
b - capture shoe (add new shoe)
c - view all shoes
d - restock shoe
e - search shoe
f - calculate total value for each item
g - find product with highest quantity
z - exit
"""

while True:
    user_choice = input(usage_message).strip().lower()
    if user_choice == "a":
        shoe_objects = read_shoes_data()

    elif user_choice == "b":
        capture_shoes(shoe_objects)

    elif user_choice == "c":
        view_all(shoe_objects)

    elif user_choice == "d":
        re_stock(shoe_objects)

    elif user_choice == "e":
        code = input("Please enter the shoe code: ")
        print(search_shoe(code, shoe_objects))

    elif user_choice == "f":
        code = input("Please enter the shoe code: ")
        value_per_item(code, shoe_objects)

    elif user_choice == "g":
        highest_qty(shoe_objects)

    elif user_choice == "z":
        print("Goodbye")
        break

    else:
        print("Oops - incorrect input")
