from collections import UserDict


class Field:
    pass


class Name(Field):
   def __init__(self, name: str):
        self.name = name


class Phone(Field):
    def __init__(self, phone: str):
        self.phone = phone


class Record:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phones = [phone]

    def add_phone(self, phone: str):
        self.phones.append(phone)

    def del_phone(self, phone: str):
        for tel in self.phones:
            if tel.phone == phone:
                self.phones.remove(tel)

    def change_phone(self, old_phone: str, new_phone: str):
        for tel in self.phones:
            if tel.phone == old_phone:
                tel.phone = new_phone


class AddressBook(UserDict):
    def add_record(self, class_record):
        # Record.name -> Record(Name(name)) -> Record.name.name
        # { Record.name.name : Record() }
        self.data[class_record.name.name] = record


if __name__ == "__main__":

    name = Name('Bill')
    phone = Phone('0123456789')
    record = Record(name, phone)
    ab = AddressBook()
    ab.add_record(record)

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].phone == '0123456789'
    
    print(isinstance(ab['Bill'], Record))
    print(record)
    print(record.name, record.phones, end = "\n")
    print(record.name.name, record.phones[0].phone, end = "\n")