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


def get_valid_number(text, f_type=int):
    while True:
        try:
            value = input(text)
            converted_value = f_type(value)
            if converted_value < 0:
                print("Error: Value cannot be negative.")
                continue
            return converted_value
        except ValueError:
            print("Error: Invalid input. Please enter a valid value.")


def add_component(filename):
    print("\n--- Add Component / Update Stock ---")

    target_id = get_valid_number("Enter ID: ", int)

    updated_list = []
    found = False

    try:
        with open(filename, 'r', newline='') as f:
            csv_list = csv.reader(f)
            for line in csv_list:
                if not line:
                    continue

                try:
                    if line[0] == str(target_id):
                        found = True
                        name = line[2]
                        current_stock = int(line[4])

                        print(f"\nItem exists: {name}")
                        print(f"Current Stock: {current_stock}")

                        add_amount = get_valid_number("Amount: ", int)
                        new_stock = current_stock + add_amount
                        line[4] = new_stock

                        print("Stock updated!")
                        input("\nPress Enter to return to the main menu...")

                    updated_list.append(line)
                except (ValueError, IndexError):
                    updated_list.append(line)

        if found == True:
            try:
                with open(filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(updated_list)
                return
            except PermissionError:
                print("\nCan not update file! File is open in another program.")
                return

    except FileNotFoundError:
        pass

    print("Creating new component...")

    c_type = input("Component Type: ").upper()
    if not c_type:
        c_type = "UNKNOWN"

    name = input("Name: ")
    price = get_valid_number("Price: ", float)
    number = get_valid_number("Stock: ", int)
    min_limit = get_valid_number("Min Limit: ", int)
    details = input("Details: ")

    current = Component(name, target_id, price, number, min_limit, c_type, details)

    try:
        with open(filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(current)
        print(f"\nSuccess!")
        input("Press Enter to return to the main menu...")
    except PermissionError:
        print("\nErorr: Permission denied! Please close the CSV file.")


def print_list(filename):
    componentsList = []
    try:
        with open(filename, 'r', newline='') as f:
            csv_list = csv.reader(f)
            for line in csv_list:
                if not line:
                    continue


                current = Component(line[2], int(line[0]), float(line[3]), int(line[4]), int(line[5]), line[1], line[6])
                componentsList.append(current)

        if len(componentsList) == 0:
            print("\nList is empty.")
            input("Press Enter to return to the main menu...")
            return

        componentsList.sort(key=lambda x: x.id)

        print("-" * 97)
        print(
            f"{'ID':^5} | {'TYPE':^12} | {'NAME':^20} | {'PRICE(TL)':^8} | {'COUNT':^8} | {'LIMIT':^6} | {'DETAILS':<25}")
        print("-" * 97)
        for i in componentsList:
            print(i)

        print("\n\n")
        input("Press Enter to return to the main menu...")

    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("\nError: Permission denied! Please close the CSV file.")


def search_item(filename):
    s_type = input("Select search type (id or name): ").lower()


    if s_type != "id" and s_type != "name":
        print("Invalid search type.")
        return

    try:
        with open(filename, 'r', newline='') as f:
            csv_list = csv.reader(f)
            target = input("Enter (id or name): ")
            found = False
            match_list = []

            for line in csv_list:
                if not line:
                    continue

                try:
                    match = False
                    if s_type == "name" and line[2].lower() == target.lower():
                        match = True
                    if s_type == "id" and line[0] == target:
                        match = True


                    if match == True:
                        found = True
                        current = Component(line[2], int(line[0]), float(line[3]), int(line[4]), int(line[5]), line[1],line[6])
                        match_list.append(current)



                except (ValueError, IndexError):
                    continue

            print("-" * 100)
            print(f"{'ID':^5} | {'TYPE':^12} | {'NAME':^20} | {'PRICE($)':^8} | {'COUNT':^8} | {'LIMIT':^6} | {'DETAILS':<25}")

            for k in match_list:
                print(k)

            if found == True:
                print("-" * 100)
            else:
                print("Item not founded.")

            input("\nPress Enter to return to the main menu...")

    except FileNotFoundError:
        print("File not founded.")
    except PermissionError:
        print("\nERROR: Permission denied! Please close the CSV file.")


def withdraw_component(filename):
    target_id = input("Enter ID: ")

    updated_list = []
    found = False
    alert_msg = ""


    try:
        with open(filename, 'r', newline='') as f:
            csv_list = csv.reader(f)
            for line in csv_list:
                if not line:
                    continue

                try:
                    if line[0] == target_id:
                        found = True
                        current_count = int(line[4])
                        min_limit = int(line[5])
                        name = line[2]

                        print(f"\nProduct Found: {name} || Current Stock: {current_count}")


                        amount = get_valid_number("Enter quantity to withdraw: ", int)

                        if amount <= current_count:
                            new_count = current_count - amount
                            line[4] = new_count
                            print(f"\nSuccess!")

                            if new_count < min_limit:
                                alert_msg = "!! Alert: Stock is below limit!!"
                        else:
                            print("\nError: Not enough stock!")

                    updated_list.append(line)
                except (ValueError, IndexError):
                    updated_list.append(line)

        if found == True:
            try:
                with open(filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(updated_list)

                if alert_msg:
                    print(alert_msg)
            except PermissionError:
                print("\nCan not save changes! File is open in another program.")
        else:
            print("\nID not founded.")

        input("\nPress Enter to return to the main menu...")

    except FileNotFoundError:
        print("File not founded.")
    except PermissionError:
        print("\nERORR : Permission denied! Please close the CSV file.")


def check_up(filename):
    urgent = []
    try:
        with open(filename, 'r', newline='') as f:
            csv_list = csv.reader(f)
            for line in csv_list:
                if not line: continue

                try:
                    current = Component(line[2], int(line[0]), float(line[3]), int(line[4]), int(line[5]), line[1],line[6])
                    if current.number < current.min_limit:
                        urgent.append(current)
                except (ValueError, IndexError):
                    continue

        if len(urgent) == 0:
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
        print("File not founded.")


def delete_component(filename):
    target_id = input("Enter ID: ")

    updated_list = []
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
                        print("İtem successfuly deleted.")
                        continue

                    updated_list.append(line)
                except (ValueError, IndexError):
                    updated_list.append(line)

        if found:
            try:
                with open(filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(updated_list)
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