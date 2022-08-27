class Person:
    def __init__(self,name,age,address):
        self._name = name
        self._age=age
        self._address = address
    
    def print_info(self):
        print(f"Name: {self._name}\nAge: {self._age}\nAddress: {self._address}\n")
    
    def get_name(self):
        return(self.name)

    def get_age(self):
        return(self.age)

    def get_address(self):
        return(self.address)

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_address(self, address):
        self.address = address
    
