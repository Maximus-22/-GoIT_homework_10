import os
from collections import UserDict


class Field:

    def __init__(self, value: str) -> None:
        self.value = value


class Name(Field):
   
   def __init__(self, name: str) -> None:
        self.name = name


class Phone(Field):

    def __init__(self, phone: str) -> None:
        self.phone = phone


class Email(Field):

    def __init__(self, email: str) -> None:
        self.email = email

class Record:

    """ QUESTION 1! """
    # def __init__(self, name: Name, phone: Phone, email: Phone) -> None:
    def __init__(self, name: Name) -> None:
        self.name = Name(name)
        # self.phones = [Phone(phone) for phone in phones]
        self.phones = []
        # self.email = Email(email)

    # def add_phone(self, phone: str):
    #     # new_phone = Phone(phone)
    #     # for tel in self.phones:
    #     if Phone(phone) not in self.phones:
    #         self.phones.append(Phone(phone))

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def del_phone(self, phone: str):
        for tel in self.phones:
            if tel.phone == phone:
                self.phones.remove(tel)

    def change_phone(self, old_phone: str, new_phone: str):
        for tel in self.phones:
            if tel.phone == old_phone:
                tel.phone = new_phone


class AdressBook(UserDict):

    def add_record(self, record: Record):
        # Record.name -> Record(Name(name)) -> Record.name.name
        # { Record.name.name : Record() }
        if record.name.name in self.data:
            existing_record = self.data[record.name.name]
            " QUESTION 2! "
            for tel in record.phones:
                existing_record.add_phone(tel.phone)
        else:
            self.data[record.name.name] = record

    def show_record(self, name):
        if name in self.data:
            record = self.data[name]
            phones = ", ".join([phone.phone for phone in record.phones])
            print("{:<20} -> {:<10}".format(record.name.value, phones))  

    def show_adressbook(self):
        for name in sorted(self.data):
            record = self.data[name]
            phones = ", ".join([phone.phone for phone in record.phones])
            print("{:<20} -> {:<10}".format(record.name.name, phones))

    def open_adressbook(self, file_name: str):
        if os.path.exists(file_name):
            with open(file_name, "r", encoding = "UTF-8") as file:
                for line in file:
                    " QUESTION 3! "
                    name, file_phones = line.strip().split(';')
                    record = Record(name)
                    for tel in file_phones.split(','):
                        record.add_phone(tel)
                    self.add_record(record)

    def close_adressbook(self, file_name: str):
        with open(file_name, 'w') as file:
                for name in self.data:
                    record = self.data[name]
                    phones = ",".join([phone.phone for phone in record.phones])
                    file.write(f"{record.name.name};{phones}\n")

    # def find_record(self, value: Record):
    #     return self.data.get(value)


if __name__ == "__main__":

    address_book = AdressBook()

    record1 = Record("John")
    record2 = Record("Britny")

    record1.add_phone("0976312904")
    record1.add_phone("0563157905")
    record2.add_phone("0508432960")
    record2.add_phone("0732071801")

    record1.change_phone("0976312904", "0673120732")
    record1.del_phone("0563157905")

    address_book.add_record(record1)
    address_book.add_record(record2)

    file_name = "phonebook.txt"
    address_book.open_adressbook(file_name)


    record3 = Record("Petro")
    record3.add_phone("0975312570")
    
    address_book.add_record(record3)
    address_book.show_adressbook()
    address_book.close_adressbook(file_name)

    assert isinstance(address_book["Petro"], Record)
    assert isinstance(address_book["Petro"].name, Name)
    assert isinstance(address_book["Petro"].phones, list)
    assert isinstance(address_book["Petro"].phones[0], Phone)
    assert address_book["Petro"].phones[0].phone == "0975312570"