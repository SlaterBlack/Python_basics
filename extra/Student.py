from Person import Person

class Student(Person):
    def __init__ (self, name, age, address, snumber):
        Person.__init__(self,name,age, address)
        self._snumber = snumber

    def print_info(self):
        Person.print_info(self)
        print(f"Snumber: {self._snumber}")

    def get_snumber(self):
        return self._snumber
