import csv


class Component:
    def __init__(self, name, id, price, number, min_limit, c_type, details):
        self.name = name
        self.id = id
        self.price = price
        self.number = number
        self.min_limit = min_limit
        self.c_type = c_type
        self.details = details

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


def get_valid_number(prompt, type_func=int):
    while True:
        try:
            value = input(prompt)
            converted_value = type_func(value)
            if converted_value < 0:
                print("Error: Value cannot be negative.")
                continue
            return converted_value
        except ValueError:
            print(f"Error: Invalid input. Please enter a valid {'integer' if type_func is int else 'number'}.")


def add_component(filename):
    print("\n--- Add Component / Update Stock ---")

    target_id = get_valid_number("Enter ID: ", int)

    updated_rows = []
    found = False

    try:
        with open(filename, 'r', newline='') as f:
            csv_list = csv.reader(f)
            for line in csv_list:
                if not line: continue

                try:
                    if line[0] == str(target_id):
                        found = True
                        name = line[2]
                        current_stock = int(line[4])

                        print(f"\nItem exists: {name}")
                        print(f"Current Stock: {current_stock}")

                        add_amount = get_valid_number("Amount to ADD to stock: ", int)
                        new_stock = current_stock + add_amount
                        line[4] = new_stock

                        print(f"Stock updated! Old: {current_stock} -> New: {new_stock}")
                        input("\nPress Enter to return to the main menu...")

                    updated_rows.append(line)
                except (ValueError, IndexError):
                    updated_rows.append(line)

        if found:
            try:
                with open(filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(updated_rows)
                return
            except PermissionError:
                print("\nCRITICAL ERROR: Could not update file! File is open in another program.")
                return

    except FileNotFoundError:
        pass

    print(f"\nID {target_id} not found. Creating new component record...")

    c_type = input("Component Type (e.g. Resistor, IC): ").upper()
    if not c_type:
        c_type = "UNKNOWN"

    name = input("Name: ")
    price = get_valid_number("Price: ", float)
    number = get_valid_number("Initial Stock: ", int)
    min_limit = get_valid_number("Min Limit Alert: ", int)
    details = input("Details: ")

    current = Component(name, target_id, price, number, min_limit, c_type, details)

    try:
        with open(filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(current)
        print(f"\nSuccess! New item added: {name}")
        input("Press Enter to return to the main menu...")
    except PermissionError:
        print("\nERROR: Permission denied! Please close the CSV file.")


def print_list(filename):
    components = []
    try:
        with open(filename, 'r', newline='') as f:
            csv_list = csv.reader(f)
            for line in csv_list:
                if not line: continue

                try:
                    current = Component(
                        name=line[2],
                        id=int(line[0]),
                        price=float(line[3]),
                        number=int(line[4]),
                        min_limit=int(line[5]),
                        c_type=line[1],
                        details=line[6]
                    )
                    components.append(current)
                except (ValueError, IndexError):
                    print(f"Warning: Skipping corrupt data line -> {line}")

        if not components:
            print("\nList is empty.")
            input("Press Enter...")
            return

        components.sort(key=lambda x: x.id)

        print("-" * 97)
        print(
            f"{'ID':^5} | {'TYPE':^12} | {'NAME':^20} | {'PRICE(TL)':^8} | {'COUNT':^8} | {'LIMIT':^6} | {'DETAILS':<25}")
        print("-" * 97)
        for i in components:
            print(i)

        print("\n\n")
        input("Press Enter to return to the main menu...")

    except FileNotFoundError:
        print("File not found. Please add a component first.")
    except PermissionError:
        print("\nERROR: Permission denied! Please close the CSV file if it is open in Excel.")


def search_item(filename):
    search_type = input("Select search type (id or name): ").lower()

    if search_type not in ['id', 'name']:
        print("Invalid search type.")
        return

    try:
        with open(filename, 'r', newline='') as f:
            csv_list = csv.reader(f)
            header_printed = False
            target = input(f"Enter {search_type}: ")
            found_any = False

            for line in csv_list:
                if not line: continue

                try:
                    is_match = False
                    if search_type == "name" and line[2].lower() == target.lower(): is_match = True
                    if search_type == "id" and line[0] == target: is_match = True

                    if is_match:
                        found_any = True
                        current = Component(
                            name=line[2], id=int(line[0]), price=float(line[3]),
                            number=int(line[4]), min_limit=int(line[5]),
                            c_type=line[1], details=line[6]
                        )

                        if not header_printed:
                            print("-" * 97)
                            print(
                                f"{'ID':^5} | {'TYPE':^12} | {'NAME':^20} | {'PRICE($)':^8} | {'COUNT':^8} | {'LIMIT':^6} | {'DETAILS':<25}")
                            header_printed = True

                        print(current)
                except (ValueError, IndexError):
                    continue

            if found_any:
                print("-" * 97)
            else:
                print("Item not found.")

            input("\nPress Enter to return to the main menu...")

    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("\nERROR: Permission denied! Please close the CSV file.")


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

                try:
                    if line[0] == target_id:
                        found = True
                        current_count = int(line[4])
                        min_limit = int(line[5])
                        name = line[2]

                        print(f"\nProduct Found: {name}")
                        print(f"Current Stock: {current_count}")

                        withdraw_amount = get_valid_number("Enter quantity to withdraw: ", int)

                        if withdraw_amount <= current_count:
                            new_count = current_count - withdraw_amount
                            line[4] = new_count
                            print(f"\nSuccess! Withdrawn: {withdraw_amount}. New Stock: {new_count}")

                            if new_count < min_limit:
                                alert_msg = f"\n!!! WARNING: Stock for '{name}' is below limit! (Current: {new_count}, Limit: {min_limit}) !!!"
                        else:
                            print("\nError: Not enough stock!")

                    updated_rows.append(line)
                except (ValueError, IndexError):
                    updated_rows.append(line)

        if found:
            try:
                with open(filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(updated_rows)

                if alert_msg:
                    print(alert_msg)
            except PermissionError:
                print("\nCRITICAL ERROR: Could not save changes! File is open in another program.")
        else:
            print("\nID not found.")

        input("\nPress Enter to return to the main menu...")

    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("\nERROR: Permission denied! Please close the CSV file.")


def check_up(filename):
    urgent = []
    try:
        with open(filename, 'r', newline='') as f:
            csv_list = csv.reader(f)
            for line in csv_list:
                if not line: continue

                try:
                    current = Component(
                        name=line[2], id=int(line[0]), price=float(line[3]),
                        number=int(line[4]), min_limit=int(line[5]),
                        c_type=line[1], details=line[6]
                    )
                    if current.number < current.min_limit:
                        urgent.append(current)
                except (ValueError, IndexError):
                    continue

        if not urgent:
            print("\nAll stock levels are sufficient.")
        else:
            urgent.sort(key=lambda x: x.id)
            print(
                f"{'ID':^5} | {'TYPE':^12} | {'NAME':^20} | {'PRICE($)':^8} | {'COUNT':^8} | {'LIMIT':^6} | {'DETAILS':<25}")
            print("-" * 97)
            for i in urgent:
                print(i)

        print("\n\n")
        input("Press Enter to return to the main menu...")
    except FileNotFoundError:
        print("File not found.")


def delete_component(filename):
    target_id = input("Enter ID to delete: ")

    updated_rows = []
    found = False

    try:
        with open(filename, 'r', newline='') as f:
            csv_list = csv.reader(f)
            for line in csv_list:
                if not line:
                    continue

                try:
                    if line[0] == target_id:
                        found = True
                        print(f"\nItem deleted: {line[2]} (ID: {target_id})")
                        continue

                    updated_rows.append(line)
                except (ValueError, IndexError):
                    updated_rows.append(line)

        if found:
            try:
                with open(filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(updated_rows)
            except PermissionError:
                print("\nCan not save changes! File is open in another program.")
        else:
            print("\nID not founded.")

        input("\nPress Enter to return to the main menu...")

    except FileNotFoundError:
        print("File not founded.")
    except PermissionError:
        print("\nERROR: Permission denied! Please close the CSV file.")


while True:
    print("=" * 50)
    print(f"{'ELECTRONIC COMPONENT MANAGEMENT SYSTEM':^50}")
    print("=" * 50)

    print("\n[ PROCESS ]")
    print("-" * 50)
    print(" 1 | Show List")
    print(" 2 | Add Component / Update Stock")
    print(" 3 | Withdraw Component")
    print(" 4 | Search Component")
    print(" 5 | Check Up (Low Stock)")
    print(" 6 | Delete Component")
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

    elif proces == '6':
        delete_component("component_list.csv")

    elif proces == 'q':
        break

    else:
        print("\nInvalid value.")