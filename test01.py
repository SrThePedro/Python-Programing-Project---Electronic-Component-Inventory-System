import csv

class Component:
    def __init__(self, name, id ,price, number, c_type, details):
        self.name = name
        self.id = id
        self.price = price
        self.number = number
        self.c_type = c_type
        self.details = details

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
            self._price = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
            self._number = value

    @property
    def c_type(self):
        return self._c_type

    @c_type.setter
    def c_type(self, value):
        self._c_type = value

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self,value):
        self._details = value


def print_list(filename):
    inventory = {}

    try:
        with open(filename, 'r', newline='') as f:
            csv_reader = csv.reader(f)

            for line in csv_reader:
                if not line:
                    continue

                c_id = int(line[0])
                c_type = line[1]
                c_name = line[2]
                c_price = float(line[3])
                c_number = int(line[4])
                c_details = line[5]

                if c_type in class_map:
                    current_class = class_map[c_type]

                    # Nesneyi oluştur (Constructor parametre sırasına dikkat)
                    # Class(name, id, price, number, c_type, details)
                    new_component = current_class(c_name, c_id, c_price, c_number, c_type, c_details)

                    # Sözlüğe ekle
                    if c_type not in inventory:
                        inventory[c_type] = []
                    inventory[c_type].append(new_component)
                else:
                    # class_map içinde bu tür yoksa, generic Component olarak veya hata basarak geçebiliriz
                    print(f"Uyarı: '{c_type}' türü sistemde tanımlı değil, atlanıyor.")




        print(f"{'ID':^5} | {'TYPE':^12} | {'NAME':^20} | {'PRICE(TL)':^8} | {'COUNT':^8} | {'DETAILS':^10}")
        print("-" * 80)


        for component_type, items in inventory.items():

            items.sort(key=lambda x: x.id)

            for item in items:
                print(item)

    except FileNotFoundError:
        print(f"\nHata: '{filename}' dosyası bulunamadı. Lütfen önce ürün ekleyin.")
    except Exception as e:
        print(f"\nBir hata oluştu: {e}")

    print("\n\n")
    input("Press Enter to return to the main menu...")
    print("\n\n")

def create_class(class_name):
    class newClass(Component):
        def __init__(self,name, id, price ,number,c_type,details):
            super().__init__(name,id,price,number,c_type,details)


        def __iter__(self):
            yield self.id
            yield self.c_type
            yield self.name
            yield self.price
            yield self.number
            yield self.details

        def __str__(self):
            return f"{self.id:^5} | {self.c_type:^12} | {self.name:^20} | {self.price:^8} | {self.number:^8} | {self.details:^10}"

    newClass.__name__ = class_name.capitalize()

    with open('component_types.txt' ,'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(class_name)

    return newClass

def load_classes(filename):
    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f)
        for line in reader:
            if line:
                create_class(line[1])

def add_new_class_type():
    print("\n--- Add New Component Class    ---")
    name = input("Yeni Sınıf Adı (örn: diode): ").lower()

    if name in class_map:
        print("Bu sınıf zaten var!")
        return

    spec1 = input("1. Özellik Adı (örn: Forward Voltage): ")
    spec2 = input("2. Özellik Adı (örn: Max Current): ")

    # Sınıfı oluştur ve sisteme dahil et
    create_dynamic_class(name, spec1, spec2)

    # Kalıcı olması için dosyaya kaydet
    save_classes()

    print(f"\nBaşarılı! '{name.capitalize()}' sınıfı oluşturuldu.")
    print("Artık 'Add Component' menüsünde bu sınıfı görebilirsin.")
    input("Devam etmek için Enter...")






while True:
    print("=" * 50)
    print(f"{'ELECTRNOIC COMPONENT MANAGEMENT SYSTEM':^50}") # Ortalar
    print("=" * 50)

    print("\n[ PROCESS ]")
    print("-" * 50)
    print(" 1 | Show List")
    print(" 2 | Deposit")
    print(" 3 | Withdraw / Sale")
    print(" 4 | Search Component")
    print(" 5 | Check Up")
    print(" 6 | Add New Component Class")
    print(" 7 | Add New Product")
    print("-" * 50)
    print(" Q | Quit")
    print("-" * 50)

    proces = input("Proces: ")

    if proces == '1':
        pass

    elif proces == '2':
        pass

    elif proces == '3':
        pass

    elif proces == '4':
        pass

    elif proces == '5':
        pass

    elif proces == '6':



    elif proces == '7':
        pass

    elif proces == 'Q' or 'q':
        break

    else:
        print("\nInvalid value.")
        input("\nPress Enter to try again...")






