import csv


class Component:
    def __init__(self, name, id, price, number, min_limit, c_type):
        self.name = name
        self.id = id
        self.price = price
        self.number = number
        self.min_limit = min_limit
        self.c_type = c_type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._price = value
        else:
            raise TypeError

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if type(value) == int:
            self._number = value
        else:
            raise TypeError

    @property
    def min_limit(self):
        return self._min_limit

    @min_limit.setter
    def min_limit(self, value):
        if type(value) == int:
            self._min_limit = value
        else:
            raise TypeError

    @property
    def c_type(self):
        return self._c_type

    @c_type.setter
    def c_type(self, value):
        self._c_type = value


class Resistor(Component):
    def __init__(self, name, id, price, number, min_limit, details):
        super().__init__(name, id, price, number, min_limit, 'resistor')
        self.details = details

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        self._details = value

    def __iter__(self):
        yield self.id
        yield self.c_type
        yield self.name
        yield self.price
        yield self.number
        yield self.min_limit
        yield self.details

    def __str__(self):
        return f"{self.id:^5} | {self.c_type:^12} | {self.name:^20} | {self.price:^8} | {self.number:^8} | {self.min_limit:^6} | {self.details:<25}"


class Capacitor(Component):
    def __init__(self, name, id, price, number, min_limit, details):
        super().__init__(name, id, price, number, min_limit, 'capacitor')
        self.details = details

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        self._details = value

    def __iter__(self):
        yield self.id
        yield self.c_type
        yield self.name
        yield self.price
        yield self.number
        yield self.min_limit
        yield self.details

    def __str__(self):
        return f"{self.id:^5} | {self.c_type:^12} | {self.name:^20} | {self.price:^8} | {self.number:^8} | {self.min_limit:^6} | {self.details:<25}"


class Transistor(Component):
    def __init__(self, name, id, price, number, min_limit, details):
        super().__init__(name, id, price, number, min_limit, 'transistor')
        self.details = details

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        self._details = value

    def __iter__(self):
        yield self.id
        yield self.c_type
        yield self.name
        yield self.price
        yield self.number
        yield self.min_limit
        yield self.details

    def __str__(self):
        return f"{self.id:^5} | {self.c_type:^12} | {self.name:^20} | {self.price:^8} | {self.number:^8} | {self.min_limit:^6} | {self.details:<25}"


def add_component(filename):
    type_choice = input("Select type (Resistor, Capacitor, Transistor): ").lower()

    if type_choice in ['resistor', 'capacitor', 'transistor']:
        name = input("Name: ")
        id_val = input("ID: ")
        price = input("Price: ")
        number = input("Number: ")
        min_limit = input("Min Limit Alert: ")
        details = input("Details: ")

        if type_choice == 'resistor':
            current = Resistor(name, int(id_val), float(price), int(number), int(min_limit), details)
        elif type_choice == 'capacitor':
            current = Capacitor(name, int(id_val), float(price), int(number), int(min_limit), details)
        elif type_choice == 'transistor':
            current = Transistor(name, int(id_val), float(price), int(number), int(min_limit), details)
    else:
        print("Invalid Type")
        return

    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(current)
    print("Component added successfully.")


def print_list(filename):
    components = []
    try:
        with open(filename, 'r', newline='') as f:
            csv_list = csv.reader(f)
            for line in csv_list:
                if not line:
                    continue

                if line[1] == 'resistor':
                    current = Resistor(line[2], int(line[0]), float(line[3]), int(line[4]), int(line[5]), line[6])
                elif line[1] == 'capacitor':
                    current = Capacitor(line[2], int(line[0]), float(line[3]), int(line[4]), int(line[5]), line[6])
                elif line[1] == 'transistor':
                    current = Transistor(line[2], int(line[0]), float(line[3]), int(line[4]), int(line[5]), line[6])
                else:
                    continue

                components.append(current)

        components.sort(key=lambda x: x.id)

        print(
            f"{'ID':^5} | {'TYPE':^12} | {'NAME':^20} | {'PRICE(TL)':^8} | {'COUNT':^8} | {'LIMIT':^6} | {'DETAILS':<25}")
        print("-" * 97)
        for i in components:
            print(i)

        print("\n\n")
        input("Press Enter to return to the main menu...")
        print("\n\n")
    except FileNotFoundError:
        print("File not found. Please add a component first.")


def search_item(filename):
    search_type = input("Select search type (id or name): ")
    found = False

    try:
        with open(filename, 'r', newline='') as f:
            csv_list = csv.reader(f)
            header_printed = False

            target = ""
            if not found:
                target = input(f"Enter {search_type}: ")
                found = True

            for line in csv_list:
                if not line: continue

                is_match = False
                if search_type == "name" and line[2] == target: is_match = True
                if search_type == "id" and line[0] == target: is_match = True

                if is_match:
                    if line[1] == 'resistor':
                        current = Resistor(line[2], int(line[0]), float(line[3]), int(line[4]), int(line[5]), line[6])
                    elif line[1] == 'capacitor':
                        current = Capacitor(line[2], int(line[0]), float(line[3]), int(line[4]), int(line[5]), line[6])
                    elif line[1] == 'transistor':
                        current = Transistor(line[2], int(line[0]), float(line[3]), int(line[4]), int(line[5]), line[6])

                    if not header_printed:
                        print("-" * 97)
                        print(
                            f"{'ID':^5} | {'TYPE':^12} | {'NAME':^20} | {'PRICE($)':^8} | {'COUNT':^8} | {'LIMIT':^6} | {'DETAILS':<25}")
                        header_printed = True

                    print(current)
                    print("-" * 97)
                    input("\nPress Enter to return...")
                    return current

            print("Item not found.")
            input("Press Enter...")

    except FileNotFoundError:
        print("File not found.")


def withdraw_component(filename):
    target_id = input("Enter ID to withdraw: ")

    updated_rows = []
    found = False
    alert_msg = ""

    try:
        with open(filename, 'r', newline='') as f:
            csv_list = csv.reader(f)
            for line in csv_list:
                if not line: continue

                if line[0] == target_id:
                    found = True
                    current_count = int(line[4])
                    min_limit = int(line[5])
                    name = line[2]

                    print(f"\nProduct Found: {name}")
                    print(f"Current Stock: {current_count}")
                    print(f"Min Limit    : {min_limit}")

                    withdraw_amount = int(input("Enter quantity to withdraw: "))

                    if withdraw_amount <= current_count:
                        new_count = current_count - withdraw_amount
                        line[4] = new_count
                        print(f"\nSuccess! Withdrawn: {withdraw_amount}. New Stock: {new_count}")

                        if new_count < min_limit:
                            alert_msg = f"\n!!! WARNING: Stock for '{name}' is below limit! (Current: {new_count}, Limit: {min_limit}) !!!"
                    else:
                        print("\nError: Not enough stock!")

                updated_rows.append(line)

        if found:
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(updated_rows)

            if alert_msg:
                print(alert_msg)
        else:
            print("\nID not found.")

        input("\nPress Enter to return to the main menu...")

    except FileNotFoundError:
        print("File not found.")


def check_up(filename):
    urgent = []
    try:
        with open(filename, 'r', newline='') as f:
            csv_list = csv.reader(f)
            for line in csv_list:
                if not line: continue

                if line[1] == 'resistor':
                    current = Resistor(line[2], int(line[0]), float(line[3]), int(line[4]), int(line[5]), line[6])
                elif line[1] == 'capacitor':
                    current = Capacitor(line[2], int(line[0]), float(line[3]), int(line[4]), int(line[5]), line[6])
                elif line[1] == 'transistor':
                    current = Transistor(line[2], int(line[0]), float(line[3]), int(line[4]), int(line[5]), line[6])
                else:
                    continue

                if current.number < current.min_limit:
                    urgent.append(current)

        urgent.sort(key=lambda x: x.id)

        print(
            f"{'ID':^5} | {'TYPE':^12} | {'NAME':^20} | {'PRICE($)':^8} | {'COUNT':^8} | {'LIMIT':^6} | {'DETAILS':<25}")
        print("-" * 97)
        for i in urgent:
            print(i)

        print("\n\n")
        input("Press Enter to return to the main menu...")
        print("\n\n")
    except FileNotFoundError:
        print("File not found.")


while True:
    print("=" * 50)
    print(f"{'ELECTRONIC COMPONENT MANAGEMENT SYSTEM':^50}")
    print("=" * 50)

    print("\n[ PROCESS ]")
    print("-" * 50)
    print(" 1 | Show List")
    print(" 2 | Add Component")
    print(" 3 | Withdraw Component")
    print(" 4 | Search Component")
    print(" 5 | Check Up (Low Stock)")
    print("-" * 50)
    print(" Q | Quit")
    print("-" * 50)

    proces = input("Process: ").lower()

    if proces == '1':
        print_list("component_list.csv")

    elif proces == '2':
        add_component("component_list.csv")

    elif proces == '3':
        withdraw_component("component_list.csv")

    elif proces == '4':
        search_item("component_list.csv")

    elif proces == '5':
        check_up("component_list.csv")

    elif proces == 'q':
        break

    else:
        print("\nInvalid value.")
        input("\nPress Enter to try again...")