class Person:
    def __init__(self, name, phone, email, add):
        self.name = name
        self.phone = phone
        self.email = email
        self.add = add

    def save(self):
        print("Contact Saved!")

    def search(self, n1):
        if self.name == n1:
            print("Name\t\t\tPhone Number\t\t\t\tEmail\t\t\t\t\tAddress ")
            print(self.name, "\t\t\t", self.phone, "\t\t\t\t",
                  self.email, "\t\t\t\t", self.add)
        else:
            print("Not Available")

    def update(self, n1):
        if self.name == n1:
            phone1 = int(input("Enter the new Phone Number "))
            email1 = input("Enter the new email ")
            add1 = input("Enter the new address ")
            self.phone = phone1
            self.email = email1
            self.add = add1
            print("Updated Successfully!")
        else:
            print("Not Available")

    def display(self):
        if not self:
            print("No Contacts Available")
        else:
            print("Name\t\t\tPhone Number\t\t\t\tEmail\t\t\t\t\tAddress ")
            print(self.name, "\t\t\t", self.phone, "\t\t\t\t",
                  self.email, "\t\t\t\t", self.add)


while True:
    print("What do you want to do?")
    print("1. Save Contacts ")
    print("2. Search  ")
    print("3. Update ")
    # print("4. Delete  ")
    print("4. Display  ")
    print("5. Press 0 to terminate")
    ch = int(input("Enter your choice "))
    if ch == 0:
        print("The Process has been terminated")
        break
    if ch == 1:
        name = input("Enter the name ")
        phone = int(input("Enter the Phone Number "))
        email = input("Enter the email ")
        add = input("Enter the address ")
        p = Person(name, phone, email, add)
        p.save()
    elif ch == 2:
        n = input("Enter the name to search ")
        p.search(n)
    elif ch == 3:
        n = input("Enter the name to search ")
        p.update(n)
    # elif ch == 4:
    elif ch == 4:
        p.display()
    else:
        print("Invalid Choice")
