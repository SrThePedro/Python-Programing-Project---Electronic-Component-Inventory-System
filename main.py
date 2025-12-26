import csv

class Component:
    def __init__(self, id, c_type, name, price, count,  min_limit, details):
        self.id = id
        self.c_type = c_type
        self.name = name
        self.price = price
        self.count = count
        self.min_limit = min_limit
        self.details = details

    def __iter__(self):
        yield self.id
        yield self.c_type
        yield self.name
        yield self.price
        yield self.count
        yield self.min_limit
        yield self.details

    def __str__(self):
        return f"{self.id:^5} | {self.c_type:^12} | {self.name:^20} | {self.price:^8} | {self.count:^8} | {self.min_limit:^8} | {self.details:<20} "


def get_valid_value(text, f_type):
    while True:
        try:
            value = f_type(input(text))

            if value < 0:
                print("Value cannot be negative.")
                continue
            return value
        except ValueError:
            print("Error: Invalid value. Plase enter a valid number.")

def add_component(filename):
    print("\n----- Add / Update Component -----")
    c_id = get_valid_value("Enter ID: ",int)

    update_list = []
    found = False

    try:
        with open(filename, 'r', newline='') as f:
            csv_list = csv.reader(f)
            for line in csv_list:
                if not line:
                    continue

                try:
                    if line[0] == str(c_id):
                        found = True
                        c_count = int(line[4])

                        print(f"\nComponent exists: {line[2]} ")
                        print(f"Current Stock: {c_count}")

                        amount = get_valid_value("Amount: ", int)
                        new_count = c_count + amount
                        line[4] = str(new_count)

                        print("Stock updated.")
                        input("\nPress Enter to return to the main menu ...")

                    update_list.append(line)
                except ValueError:
                    update_list.append(line)
                except IndexError:
                    update_list.append(line)

        if found == True:
            try:
                with open(filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(update_list)
                return

            except PermissionError:
                print("\nCan not update file. File is open in another program.")
                return

    except FileNotFoundError:
        pass

    print("Creating new component ...")
    c_type = get_valid_value("Component Type: ",int)
    if not c_type:
        c_type = "UNKNOWN"

    name = input("Name: ")
    price= get_valid_value("Price: ", float)
    count = get_valid_value("Count: " ,int)
    min_limit = get_valid_value("Min Limit: ",int)
    details = input("Details: ")

    new_component = Component(c_id, c_type, name, price, count, min_limit, details)

    try:
        with open(filename, 'a' , newline='') as f:
            writer = csv.writer(f)
            writer.writerow(new_component)
        print("\nList updated.")
        input("\nPress Enter to return to the main menu ...")

    except PermissionError:
        print("\nCan not update file. File is open in another program.")
        return

def print_list(filename):
    component_list = []
    try:
        with open(filename, 'r', newline='') as f:
            csv_list = csv.reader(f)
            for line in csv_list:
                if not line:
                    continue

                current = Component(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
                component_list.append(current)

        if len(component_list) == 0:
            print("\nList is empty.")
            input("\nPress Enter to return to the main menu ...")
            return

        component_list.sort(key=lambda x : int(x.id))

        print("-"*100)
        print(f"{'ID':^5} | {'TYPE':^12} | {'NAME':^20} | {'PRICE(TL)':^8} | {'COUNT':^8} | {'LIMIT':^6} | {'DETAILS':<20}")
        print("-" * 100)

        for i in component_list:
            print(i)

        print("\n\n")
        input("\nPress Enter to return to the main menu ...")
    except PermissionError:
        print("\nCan not read file. File is open in another program.")
        return

    except FileNotFoundError:
        print("File not found.")


def search_item(filename):
    s_type = input("Select search type (id or name): ").lower()

    if s_type != "id" and s_type != "name":
        print("Invalid search type.")
        return

    try:
        with open(filename, 'r' , newline='') as f:
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
                        current = Component(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
                        match_list.append(current)

                except ValueError:
                    continue
                except IndexError:
                    continue

            if found == True:
                print("-" * 100)
                print(f"{'ID':^5} | {'TYPE':^12} | {'NAME':^20} | {'PRICE(TL)':^8} | {'COUNT':^8} | {'LIMIT':^6} | {'DETAILS':<20}")

                for j in match_list:
                    print(j)

                print("-" * 100)

            else:
                print("Item not founded.")

            input("\nPress Enter to return to the main menu ...")

    except PermissionError:
        print("\nCan not read file. File is open in another program.")
        return

    except FileNotFoundError:
        print("File not found.")

def withdraw_component(filename):
    c_id = input("Enter ID: ")

    update_list = []
    found = False
    alert_msg = ""

    try:
        with open(filename, 'r' , newline='') as f:
            csv_list = csv.reader(f)
            for line in csv_list:
                if not line:
                    continue

                try:
                    if line[0] == c_id:
                        found = True
                        print(f"\nComponent Name: {line[2]} || Stock: {line[4]}")
                        amount = get_valid_value("Enter quantity to withdraw: ", int)

                        if amount <= int(line[4]):
                            new_count= int(line[4]) - int(amount)
                            line[4] = str(new_count)
                            print("\nSuccess.")

                            if int(new_count) < int(line[5]):
                                alert_msg = "!! Alert: Stock is below limit !!"

                        else:
                            print("\nNot enough stock.")

                    update_list.append(line)

                except ValueError:
                    update_list.append(line)
                except IndexError:
                    update_list.append(line)

            if found == True:
                try:
                    with open(filename, 'w', newline='' ) as f:
                        writer = csv.writer(f)
                        writer.writerows(update_list)

                    if alert_msg:
                        print(alert_msg)


                except PermissionError:
                    print("\nCan not read file. File is open in another program.")

            else:
                print("\nComponent not founded.")

            input("\nPress Enter to return to the main menu ...")

    except PermissionError:
        print("\nCan not read file. File is open in another program.")
    except FileNotFoundError:
        print("\nFile not founded.")

def check_up(filename):
    urgent_list = []
    try:
        with open(filename, 'r' , newline='') as f:
            csv_list = csv.reader(f)
            for line in csv_list:
                if not line:
                    continue

                try:
                    if int(line[4]) < int(line[5]):
                        current = Component(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
                        urgent_list.append(current)

                except ValueError:
                    continue
                except IndexError:
                    continue

        if len(urgent_list) == 0:
            print("All stock levels are sufficient.")

        else:
            urgent_list.sort(key=lambda x: int(x.id))
            print("-" * 100)
            print(f"{'ID':^5} | {'TYPE':^12} | {'NAME':^20} | {'PRICE(TL)':^8} | {'COUNT':^8} | {'LIMIT':^6} | {'DETAILS':<20}")

            for j in urgent_list:
                print(j)

            print("-" * 100)

        print("\n\n")
        input("\nPress Enter to return to the main menu ...")

    except PermissionError:
        print("\nCan not read file. File is open in another program.")
    except FileNotFoundError:
        print("\nFile not founded.")

def delete_component(filename):
    c_id = input("Enter ID: ")
    update_list = []
    found = False

    try:
        with open(filename, 'r', newline='') as f:
            csv_list = csv.reader(f)
            for line in csv_list:
                if not line:
                    continue

                try:
                    if line[0] == c_id:
                        found = True
                        print("Item successfly deleted.")
                        continue

                    update_list.append(line)

                except ValueError:
                    update_list.append(line)
                except IndexError:
                    update_list.append(line)

        if found == True:
            try:
                with open(filename, 'w' , newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(update_list)

            except PermissionError:
                print("\nCan not save changes. File is open another program.")

        else:
            print("\nComponent not founded.")

        input("\nPress Enter to return to the main menu ...")

    except PermissionError:
        print("\nCan not read file. File is open in another program.")
    except FileNotFoundError:
        print("\nFile not founded.")

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
        print("\nInvalid value. Try again.")






































