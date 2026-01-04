import csv


# MAİN CLASS
class Component:
    def __init__(self, id, c_type, name, price, count, min_limit, details):
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


# SUBCLASSES
class Resistor(Component):
    def __init__(self, id, c_type, name, price, count, min_limit, details):
        super().__init__(id, c_type, name, price, count, min_limit, details)


class Capacitor(Component):
    def __init__(self, id, c_type, name, price, count, min_limit, details):
        super().__init__(id, c_type, name, price, count, min_limit, details)


class Connector(Component):
    def __init__(self, id, c_type, name, price, count, min_limit, details):
        super().__init__(id, c_type, name, price, count, min_limit, details)


class Module(Component):
    def __init__(self, id, c_type, name, price, count, min_limit, details):
        super().__init__(id, c_type, name, price, count, min_limit, details)


class Sensor(Component):
    def __init__(self, id, c_type, name, price, count, min_limit, details):
        super().__init__(id, c_type, name, price, count, min_limit, details)


class IC(Component):
    def __init__(self, id, c_type, name, price, count, min_limit, details):
        super().__init__(id, c_type, name, price, count, min_limit, details)


class LED(Component):
    def __init__(self, id, c_type, name, price, count, min_limit, details):
        super().__init__(id, c_type, name, price, count, min_limit, details)


class Diode(Component):
    def __init__(self, id, c_type, name, price, count, min_limit, details):
        super().__init__(id, c_type, name, price, count, min_limit, details)


class Potentiometer(Component):
    def __init__(self, id, c_type, name, price, count, min_limit, details):
        super().__init__(id, c_type, name, price, count, min_limit, details)


class Tool(Component):
    def __init__(self, id, c_type, name, price, count, min_limit, details):
        super().__init__(id, c_type, name, price, count, min_limit, details)


# MANAGER CLASS
class InventoryManager:
    def __init__(self, filename):
        self.filename = filename

    def get_valid_value(self, text, f_type):
        while True:
            try:
                value = f_type(input(text))
                if value < 0:
                    print("Value cannot be negative.")
                    continue
                return value
            except ValueError:
                print("Error: Invalid value. Plase enter a valid number.")

    def add_component(self):
        print("\n----- Add / Update Component -----")
        c_id = self.get_valid_value("Enter ID: ", int)

        update_list = []
        found = False

        try:
            with open(self.filename, 'r', newline='') as f:
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

                            amount = self.get_valid_value("Amount: ", int)
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
                    with open(self.filename, 'w', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerows(update_list)
                    return
                except PermissionError:
                    print("\nCan not update file. File is open in another program.")
                    return

        except FileNotFoundError:
            pass

        print("Creating new component ...")

        print("\nSelect Type:")
        print("1: Resistor      2: Capacitor")
        print("3: Connector     4: Module")
        print("5: Sensor        6: IC")
        print("7: LED           8: Diode")
        print("9: Potentiometer 10: Tool")
        c_type = self.get_valid_value("Enter Type Number (Other for else): ", int)

        c_type_str = "UNKNOWN"
        if c_type == 1:
            c_type_str = "Resistor"
        elif c_type == 2:
            c_type_str = "Capacitor"
        elif c_type == 3:
            c_type_str = "Connector"
        elif c_type == 4:
            c_type_str = "Module"
        elif c_type == 5:
            c_type_str = "Sensor"
        elif c_type == 6:
            c_type_str = "IC"
        elif c_type == 7:
            c_type_str = "LED"
        elif c_type == 8:
            c_type_str = "Diode"
        elif c_type == 9:
            c_type_str = "Potentiometer"
        elif c_type == 10:
            c_type_str = "Tool"
        else:
            c_type_str = "Other"

        name = input("Name: ")
        price = self.get_valid_value("Price: ", float)
        count = self.get_valid_value("Count: ", int)
        min_limit = self.get_valid_value("Min Limit: ", int)
        details = input("Details: ")


        if c_type_str == "Resistor":
            new_component = Resistor(c_id, c_type_str, name, price, count, min_limit, details)
        elif c_type_str == "Capacitor":
            new_component = Capacitor(c_id, c_type_str, name, price, count, min_limit, details)
        elif c_type_str == "Connector":
            new_component = Connector(c_id, c_type_str, name, price, count, min_limit, details)
        elif c_type_str == "Module":
            new_component = Module(c_id, c_type_str, name, price, count, min_limit, details)
        elif c_type_str == "Sensor":
            new_component = Sensor(c_id, c_type_str, name, price, count, min_limit, details)
        elif c_type_str == "IC":
            new_component = IC(c_id, c_type_str, name, price, count, min_limit, details)
        elif c_type_str == "LED":
            new_component = LED(c_id, c_type_str, name, price, count, min_limit, details)
        elif c_type_str == "Diode":
            new_component = Diode(c_id, c_type_str, name, price, count, min_limit, details)
        elif c_type_str == "Potentiometer":
            new_component = Potentiometer(c_id, c_type_str, name, price, count, min_limit, details)
        elif c_type_str == "Tool":
            new_component = Tool(c_id, c_type_str, name, price, count, min_limit, details)
        else:
            new_component = Component(c_id, c_type_str, name, price, count, min_limit, details)

        try:
            with open(self.filename, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(new_component)
            print("\nList updated.")
            input("\nPress Enter to return to the main menu ...")

        except PermissionError:
            print("\nCan not update file. File is open in another program.")
            return

    def print_list(self):
        component_list = []
        try:
            with open(self.filename, 'r', newline='') as f:
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

            component_list.sort(key=lambda x: int(x.id))

            print("-" * 100)
            print(
                f"{'ID':^5} | {'TYPE':^12} | {'NAME':^20} | {'PRICE(TL)':^8} | {'COUNT':^8} | {'LIMIT':^6} | {'DETAILS':<20}")
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

    def search_item(self):
        s_type = input("Select search type (id or name): ").lower()

        if s_type != "id" and s_type != "name":
            print("Invalid search type.")
            return

        try:
            with open(self.filename, 'r', newline='') as f:
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
                    print(
                        f"{'ID':^5} | {'TYPE':^12} | {'NAME':^20} | {'PRICE(TL)':^8} | {'COUNT':^8} | {'LIMIT':^6} | {'DETAILS':<20}")
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

    def withdraw_component(self):
        c_id = input("Enter ID: ")
        update_list = []
        found = False
        alert_msg = ""

        try:
            with open(self.filename, 'r', newline='') as f:
                csv_list = csv.reader(f)
                for line in csv_list:
                    if not line:
                        continue
                    try:
                        if line[0] == c_id:
                            found = True
                            print(f"\nComponent Name: {line[2]} || Stock: {line[4]}")
                            amount = self.get_valid_value("Enter quantity to withdraw: ", int)

                            if amount <= int(line[4]):
                                new_count = int(line[4]) - int(amount)
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
                    with open(self.filename, 'w', newline='') as f:
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

    def check_up(self):
        urgent_list = []
        try:
            with open(self.filename, 'r', newline='') as f:
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
                print(
                    f"{'ID':^5} | {'TYPE':^12} | {'NAME':^20} | {'PRICE(TL)':^8} | {'COUNT':^8} | {'LIMIT':^6} | {'DETAILS':<20}")
                for j in urgent_list:
                    print(j)
                print("-" * 100)

            print("\n\n")
            input("\nPress Enter to return to the main menu ...")

        except PermissionError:
            print("\nCan not read file. File is open in another program.")
        except FileNotFoundError:
            print("\nFile not founded.")

    def delete_component(self):
        c_id = input("Enter ID: ")
        update_list = []
        found = False

        try:
            with open(self.filename, 'r', newline='') as f:
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
                    with open(self.filename, 'w', newline='') as f:
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

    def run_menu(self):
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
                self.print_list()
            elif proces == '2':
                self.add_component()
            elif proces == '3':
                self.withdraw_component()
            elif proces == '4':
                self.search_item()
            elif proces == '5':
                self.check_up()
            elif proces == '6':
                self.delete_component()
            elif proces == 'q':
                break
            else:
                print("\nInvalid value. Try again.")



app = InventoryManager("component_list.csv")
app.run_menu()