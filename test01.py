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

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self,value):
        self._details = value


class_map = []
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
    class_map.append(class_name)
    return newClass









