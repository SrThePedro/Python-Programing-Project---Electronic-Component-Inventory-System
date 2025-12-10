import csv

class Component:
    def __init__(self, name, id ,price, number, c_type ):
        self.name = name
        self.id = id
        self.price = price
        self.number = number
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
    def c_type(self):
        return self._c_type

    @c_type.setter
    def c_type(self, value):
        self._c_type = value

class Resistor(Component):
    def __init__(self,name,id,price,number,resistance_value,power_rating):
        super().__init__(name,id,price,number,'resistor')
        self.resistance_value = resistance_value
        self.power_rating = power_rating


    @property
    def resistance_value(self):
        return self._resistance_value

    @resistance_value.setter
    def resistance_value(self, value):
        self._resistance_value = value

    @property
    def power_rating(self):
        return self._power_rating

    @power_rating.setter
    def power_rating(self,value):
        self._power_rating = value

    def __iter__(self):
        yield self.id
        yield self.c_type
        yield self.name
        yield self.price
        yield self.number
        yield self.resistance_value
        yield self.power_rating

    def __str__(self):
        return f"{self.id:^5} | {self.c_type:^12} | {self.name:^20} | {self.price:^8} | {self.number:^8} | {self.resistance_value:^10} | {self.power_rating:^8}"

class Capacitor(Component):
    def __init__(self,name,id,price,number,capacitance,voltage_rating):
        super().__init__(name,id,price,number, 'capacitor')
        self.capacitance = capacitance
        self.voltage_rating = voltage_rating

    @property
    def capacitance(self):
        return self._capacitance

    @capacitance.setter
    def capacitance(self,value):
        self._capacitance = value

    def __iter__(self):
        yield self.id
        yield self.c_type
        yield self.name
        yield self.price
        yield self.number
        yield self.capacitance
        yield self.voltage_rating

    def __str__(self):
        return f"{self.id:^5} | {self.c_type:^12} | {self.name:^20} | {self.price:^8} | {self.number:^8} | {self.capacitance:^10} | {self.voltage_rating:^8}"

class Transistor(Component):
    def __init__(self, name, id, price, number, type, package_type):
        super().__init__(name,id,price,number, 'transistor')
        self.type = type
        self.package_type = package_type

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def package_type(self):
        return self._package_type

    @package_type.setter
    def package_type(self, value):
        self._package_type = value

    def __iter__(self):
        yield self.id
        yield self.c_type
        yield self.name
        yield self.price
        yield self.number
        yield self.type
        yield self.package_type

    def __str__(self):
        return f"{self.id:^5} | {self.c_type:^12} | {self.name:^20} | {self.price:^8} | {self.number:^8} | {self.type:^10} | {self.package_type:^8}"

r1 = Resistor("10k Metal Film", 102, 1, 500, 10000, 0.25)
r2 = Resistor("330R Carbon Film", 101, 1, 1000, 330, 0.25)
r3 = Resistor("5R6 Power Resistor", 103, 15, 50, 5.6, 5)

c1 = Capacitor("Electrolytic" , 201, 3.5, 200, 1000, 16)
c2 = Capacitor("Ceramic", 202, 0.25, 2000, 0.1 , 50)
c3 = Capacitor("Low ESR", 203, 8, 100, 470, 35)

t1 = Transistor("BC547", 301, 1.5 , 300, "NPN", "TO-92")
t2 = Transistor("IRFZ44N", 302, 12, 40, "MOSFET", "TO-220")
t3 = Transistor("BD140", 303, 4.5, 80, "PNP", "TO-126")


def add_component(filename):
    type = input("Select type (Resistor, Capacitor, Transistor) :")

    if type == 'resistor':
        name = input("Name: ")
        id = input("ID: ")
        price = input("Prcie: ")
        number = input("Number: ")
        resistance_value = input("Resistance Value: ")
        power = input("Power Rating: ")

        current = Resistor(name, int(id), float(price), int(number), (resistance_value), float(power))

    elif type == 'capacitor':
        name = input("Name: ")
        id = input("ID: ")
        price = input("Prcie: ")
        number = input("Number: ")
        capacitance = input("Capacitance: ")
        voltage_rating = input("Voltage Rating: ")

        current = Capacitor(name, int(id), float(price), int(number), capacitance, voltage_rating)

    elif type == 'transistor':
        name = input("Name: ")
        id = input("ID: ")
        price = input("Prcie: ")
        number = input("Number: ")
        type2 = input("Type: ")
        package_type = input("Package Type: ")

        current = Transistor(name, int(id), float(price), int(number), type2, package_type )

    else:
        print("Invalid")


    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(current)

def print_list(filename):
    rs = []
    cp = []
    tr = []

    with open(filename, 'r', newline='') as f:
        csv_list = csv.reader(f)
        for line in csv_list:
            if not line:
                continue

            if line[1] == 'resistor':
                current = Resistor(line[2], int(line[0]), float(line[3]), int(line[4]), (line[5]), float(line[6]))
                rs.append(current)

            elif line[1] == 'capacitor':
                current = Capacitor(line[2], int(line[0]), float(line[3]), int(line[4]), (line[5]), (line[6]))
                cp.append(current)

            elif line[1] == 'transistor':
                current = Transistor(line[2], int(line[0]), float(line[3]), int(line[4]), (line[5]), (line[6]))
                tr.append(current)

        rs.sort(key=lambda x: x.id)
        cp.sort(key=lambda x: x.id)
        tr.sort(key=lambda x: x.id)

        print(f"{'ID':^5} | {'TYPE':^12} | {'NAME':^20} | {'PRICE($)':^8} | {'COUNT':^8} | {'SPEC 1':^10} | {'SPEC 2':^8}")
        for i in rs:
            print(i)


        for i in cp:
            print(i)


        for i in tr:
            print(i)

        print("\n\n")
        input("Ana menüye dönmek için Enter tuşuna basınız...")
        print("\n\n")

def search_item(filename):
    type = input("Select type(id or name): ")
    if type == "name":
        name = input("Name: ")
        print("\n")
        with open(filename, 'r', newline='') as f:
            csv_list = csv.reader(f)
            for line in csv_list:
                if not line:
                    continue

                if line[2] == name:
                    if line[1] == 'resistor':
                        current = Resistor(line[2], int(line[0]), float(line[3]), int(line[4]), (line[5]), float(line[6]))

                    elif line[1] == 'capacitor':
                        current = Capacitor(line[2], int(line[0]), float(line[3]), int(line[4]), (line[5]), (line[6]))

                    elif line[1] == 'transistor':
                        current = Transistor(line[2], int(line[0]), float(line[3]), int(line[4]), (line[5]), (line[6]))
                    print("-"*100)
                    print(f"{'ID':^5} | {'TYPE':^12} | {'NAME':^20} | {'PRICE($)':^8} | {'COUNT':^8} | {'SPEC 1':^10} | {'SPEC 2':^8}")
                    print(current)
                    print("-"*100)
                    print("\n\n")
                    input("Ana menüye dönmek için Enter tuşuna basınız...")
                    print("\n\n")
                    return current
    elif type == "id":
        id = input("ID: ")
        print("\n")
        with open(filename, 'r', newline='') as f:
            csv_list = csv.reader(f)
            for line in csv_list:
                if not line:
                    continue

                if line[0] == id:
                    if line[1] == 'resistor':
                        current = Resistor(line[2], int(line[0]), float(line[3]), int(line[4]), (line[5]),float(line[6]))

                    elif line[1] == 'capacitor':
                        current = Capacitor(line[2], int(line[0]), float(line[3]), int(line[4]), (line[5]), (line[6]))

                    elif line[1] == 'transistor':
                        current = Transistor(line[2], int(line[0]), float(line[3]), int(line[4]), (line[5]), (line[6]))
                    print("-"*100)
                    print( f"{'ID':^5} | {'TYPE':^12} | {'NAME':^20} | {'PRICE($)':^8} | {'COUNT':^8} | {'SPEC 1':^10} | {'SPEC 2':^8}")
                    print(current)
                    print("-"*100)
                    print("\n\n")
                    input("Ana menüye dönmek için Enter tuşuna basınız...")
                    print("\n\n")
                    return current


    else:
        raise ValueError

def delete_component(filename):
    pass

#arayuz

while True:
    print("=" * 50)
    print(f"{'ELECTRNOIC COMPONENT MANAGEMENT SYSTEM':^50}") # Ortalar
    print("=" * 50)

    print("\n[ PROCESS ]")
    print("-" * 50)
    print(" 1 | Show List")
    print(" 2 | Add Component")
    print(" 3 | Sub Component")
    print(" 4 | Search Component")
    print(" 5 | Check Up")
    print("-" * 50)
    print(" Q | Quit")
    print("-" * 50)

    proces = input("Proces: ")

    if proces == '1':
        print_list("component_list.csv")

    elif proces == '2':
        add_component("component_list.csv")

    elif proces == '3':
        pass

    elif proces == '4':
        search_item("component_list.csv")

    elif proces == '5':
        pass

    elif proces == 'Q':
        break

    else:
        print("Invalid Proces.")





















