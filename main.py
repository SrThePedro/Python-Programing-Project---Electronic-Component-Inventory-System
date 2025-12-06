class Component:
    def __init__(self, name, id ,price, number ):
        self.name = name
        self.id = id
        self.price = price
        self.number = number

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = value

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, value):
        self.id = value

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, value):
        if type(value) == int and value >= 0:
            self.price = value
        else:
            raise TypeError

    @property
    def number(self):
        return self.number

    @number.setter
    def number(self, value):
        if type(value) == int:
            self.number = value
        else:
            raise TypeError

class Resistor(Component):
    def __init__(self,name,id,price,number,resistance_value,power_rating):
        super().__init__(name,id,price,number)
        self.resistance_value = resistance_value
        self.power_rating = power_rating

    @property
    def resistance_value(self):
        return self.resistance_value

    @resistance_value.setter
    def resistance_value(self, value):
        self.resistance_value = value

    @property
    def power_rating(self):
        return self.power_rating

    @power_rating.setter
    def power_rating(self,value):
        self.power_rating = value

    def __str__(self):
        return f"{self.id} {self.name} {self.price} {self.number} {self.resistance_value} {self.power_rating}"

class Capacitor(Component):
    def __init__(self,name,id,price,number,capacitance,voltage_rating):
        super().__init__(name,id,price,number)
        self.capacitance = capacitance
        self.voltage_rating = voltage_rating

    @property
    def capacitance(self):
        return self.capacitance

    @capacitance.setter
    def capacitance(self,value):
        self.capacitance = value

    def __str__(self):
        return f"{self.id} {self.name} {self.price} {self.number} {self.capacitance} {self.voltage_rating}"



