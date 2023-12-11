class ContactBook:
    def _init_(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        if name not in self.contacts:
            self.contacts[name] = phone_number
            print(f"Contact {name} added successfully.")
        else:
            print(f"Contact {name} already exists. Use a different name.")

    def get_contact(self, name):
        if name in self.contacts:
            return f"Contact: {name}, Phone Number: {self.contacts[name]}"
        else:
            return f"Contact {name} not found."

    def display_contacts(self):
        print("\nContacts:")
        for name, phone_number in self.contacts.items():
            print(f"{name}: {phone_number}")

# Example usage
contact_book = ContactBook()

contact_book.add_contact("John Doe", "123-456-7890")
contact_book.add_contact("Jane Smith", "987-654-3210")

print(contact_book.get_contact("John Doe"))
print(contact_book.get_contact("Jane Smith"))
print(contact_book.get_contact("Bob"))

contact_book.display_contacts()
