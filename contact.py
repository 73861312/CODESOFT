import os

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contact_list(self):
        print("Contact List:")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact.name} - {contact.phone_number}")

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone_number]
        return results

    def update_contact(self, contact_index, new_contact):
        self.contacts[contact_index] = new_contact
        print("Contact updated successfully!")

    def delete_contact(self, contact_index):
        del self.contacts[contact_index]
        print("Contact deleted successfully!")

def get_contact_details_from_user():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    return Contact(name, phone_number, email, address)

def display_contact_details(contact):
    print(f"\nName: {contact.name}\nPhone Number: {contact.phone_number}\nEmail: {contact.email}\nAddress: {contact.address}\n")

def main():
    contact_manager = ContactManager()

    while True:
        print("\n-------------------")
        print("Contacts Manager")
        print("-------------------")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            contact = get_contact_details_from_user()
            contact_manager.add_contact(contact)
        elif choice == '2':
            contact_manager.view_contact_list()
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            results = contact_manager.search_contact(keyword)
            if results:
                print("Search Results:")
                for i, result in enumerate(results, start=1):
                    print(f"{i}. {result.name} - {result.phone_number}")
                contact_index = int(input("Enter the number of the contact to view details (0 to go back): ")) - 1
                if 0 <= contact_index < len(results):
                    display_contact_details(results[contact_index])
            else:
                print("No results found.")
        elif choice == '4':
            contact_manager.view_contact_list()
            contact_index = int(input("Enter the number of the contact to update (0 to go back): ")) - 1
            if 0 <= contact_index < len(contact_manager.contacts):
                new_contact = get_contact_details_from_user()
                contact_manager.update_contact(contact_index, new_contact)
        elif choice == '5':
            contact_manager.view_contact_list()
            contact_index = int(input("Enter the number of the contact to delete (0 to go back): ")) - 1
            if 0 <= contact_index < len(contact_manager.contacts):
                display_contact_details(contact_manager.contacts[contact_index])
                confirmation = input("Are you sure you want to delete this contact? (y/n): ").lower()
                if confirmation == 'y':
                    contact_manager.delete_contact(contact_index)
        elif choice == '6':
            print("Exiting Contacts Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()