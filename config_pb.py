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

    def __init__(self, name: Name, phone: Phone = None, email: Email = None) -> None:
        self.name = Name(name)
        # self.phones = [Phone(phone) for phone in phones]
        self.phones = [phone] if phone else []
        self.email = [email] if email else []

    def add_phone(self, phone: str):
        if phone not in [tel.phone for tel in self.phones]:
            self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        for tel in self.phones:
            if tel.phone == phone:
                self.phones.remove(tel)

    def change_phone(self, old_phone: str, new_phone: str):
        for tel in self.phones:
            if tel.phone == old_phone:
                tel.phone = new_phone


class AddressBook(UserDict):

    def add_record(self, record: Record):
        # Record.name -> Record(Name(name)) -> Record.name.name
        # { Record.name.name : Record() }
        if record.name.name in self.data:
            existing_record = self.data[record.name.name]
            for tel in record.phones:
                existing_record.add_phone(tel.phone)
            # existing_record.add_phone(record.phones[0])
        else:
            self.data[record.name.name] = record

    def edit_record(self, name, phone):
        if name in self.data:
            record = self.data[name]
            record.remove_phone(phone)

    def show_record(self, name):
        if name in self.data:
            record = self.data[name]
            phones = ", ".join([phone.phone for phone in record.phones])
            print(f"Contact {name} has phone: {phones}") 

    def show_addressbook(self):
        # for name.name in sorted(self.data):
        for name in sorted(self.data):
            record = self.data[name]
            phones = ", ".join([phone.phone for phone in record.phones])
            print("{:<20} -> {:<15}".format(name, phones))

    def open_addressbook(self, file_name: str):
        if os.path.exists(file_name):
            with open(file_name, "r", encoding = "UTF-8") as file:
                for line in file:
                    name, file_phones = line.strip().split(';')
                    # record = Record(Name(name))
                    record = Record(name)
                    for tel in file_phones.split(','):
                        record.add_phone(tel)
                    self.add_record(record)

    def close_addressbook(self, file_name: str):
        with open(file_name, "w", encoding = "UTF-8") as file:
            for name in self.data:
                record = self.data[name]
                phones = ",".join([phone.phone for phone in record.phones])
                # file.write(f"{record.name.name};{phones}\n")
                file.write(f"{name};{phones}\n")



if __name__ == "__main__":

    address_book = AddressBook()

    name1 = "John"
    name2 = "Britny"
    record1 = Record(name1)
    record2 = Record(name2)

    record1.add_phone("0976312904")
    record1.add_phone("0563157905")
    record2.add_phone("0508432960")
    record2.add_phone("0732071801")

    record1.change_phone("0976312904", "0673120732")
    record1.remove_phone("0563157905")

    address_book.add_record(record1)
    address_book.add_record(record2)

    file_name = "phonebook.txt"
    address_book.open_addressbook(file_name)

    name3 = "Petro"
    record3 = Record(name3)
    record3.add_phone("0975312570")
    
    address_book.add_record(record3)
    address_book.show_addressbook()
    address_book.close_addressbook(file_name)

    assert isinstance(address_book["Petro"], Record)
    assert isinstance(address_book["Petro"].name, Name)
    assert isinstance(address_book["Petro"].phones, list)
    assert isinstance(address_book["Petro"].phones[0], Phone)
    assert address_book["Petro"].phones[0].phone == "0975312570"