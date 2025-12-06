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

class
