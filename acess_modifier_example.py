class Person:
    def __init__ (self, name, age, address):
        self.name=name
        self._age=age
        self.__address=address

    def get_name(self):
        return self.name
    def _get_age(self):
        return self._age
    def __get_address(self):
        return self.__address

ram = Person('Hari', 25, 'KTM')

def getDetails():
    print(ram.get_name())
    print(ram._get_age())
    # print(ram.__get_address())

getDetails()