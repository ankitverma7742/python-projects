import json

# Define the filename where contacts will be stored
filename = "contacts.json"

# Load contAacts from file if exists
def load_contacts():
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save contacts to file
def save_contacts(contacts):
    with open(filename, "w") as f:
        json.dump(contacts, f, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print(f"Contact {name} added successfully.")

# Update an existing contact
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact found.")
            contact["phone"] = input("Enter new phone number: ")
            contact["email"] = input("Enter new email: ")
            print(f"Contact {name} updated successfully.")
            return
    print(f"No contact found with name {name}.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name.lower():
            del contacts[i]
            print(f"Contact {name} deleted successfully.")
            return
    print(f"No contact found with name {name}.")

# Search for a contact
def search_contact(contacts):
    name = input("Enter the name of the contact to search for: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            return
    print(f"No contact found with name {name}.")

# List all contacts
def list_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"Contact {i}:")
            print(f"  Name: {contact['name']}")
            print(f"  Phone: {contact['phone']}")
            print(f"  Email: {contact['email']}")
            print()

# Main function to handle the menu
def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. List Contacts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            update_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '5':
            list_contacts(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()