from collections import UserDict


class Field:

    def __init__(self, value: str):
        self.value = value


class Name(Field):
   
   def __init__(self, name: str):
        self.name = name


class Phone(Field):

    def __init__(self, phone: str):
        self.phone = phone


class Email(Field):

    def __init__(self, email: str):
        self.email = email

class Record:

    def __init__(self, name: Name, phone: Phone = None, email: Email = None):
        self.name = name
        # self.phones = [Phone(phone) for phone in phones]
        self.phones = [phone] if phone else []
        self.email = [email] if email else []

    def add_phone(self, phone: str):
        new_phone = Phone(phone)
        if new_phone not in self.phones:
            self.phones.append(new_phone)

    def del_phone(self, phone: str):
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
        self.data[record.name.name] = record

    def find_record(self, value: Record):
        return self.data.get(value)


if __name__ == "__main__":

    name = Name("Bill")
    phone = Phone("0123456789")
    email = Email("fox-24@biz.tv")
    record = Record(name, phone, email)
    ab = AddressBook()
    ab.add_record(record)

    assert isinstance(ab["Bill"], Record)
    assert isinstance(ab["Bill"].name, Name)
    assert isinstance(ab["Bill"].phones, list)
    assert isinstance(ab["Bill"].phones[0], Phone)
    assert isinstance(ab["Bill"].email, Email)
    assert ab["Bill"].phones[0].phone == "0123456789"
    
    # print(isinstance(ab['Bill'], Record))
    # print(record)
    # print(record.name, record.phones, end = "\n")
    # print(record.name.name, record.phones[0].phone, end = "\n")