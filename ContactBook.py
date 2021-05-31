d = {}
i = 1
while i != 0:
    print("What do you want to do?")
    print("1. Save Contacts ")
    print("2. Search  ")
    print("3. Update ")
    print("4. Delete  ")
    print("5. Display  ")
    print("6. Press 0 to terminate")
    ch = int(input("Enter your choice "))
    c = []
    if ch == 0:
        print("The Process has been terminated")
        break
    if ch == 1:
        name = input("Enter the name ")
        phone = int(input("Enter the phone number "))
        email = input("Enter the email address ")
        add = input("Enter the address ")
        c.append(phone)
        c.append(email)
        c.append(add)
        d[name] = c
    elif ch == 2:
        name1 = input("Enter name to search ")
        if name1 in d:
            # print("Name :",name1,"Phone Number :",d[name][0])
            print("Name\t\t\tPhone Number\t\t\t\tEmail\t\t\t\tAddress ")
            print(name1, "\t\t\t", d[name1][0], "\t\t\t\t",
                  d[name1][1], "\t\t\t\t\t", d[name1][2])

        else:
            print("Not Available")
    elif ch == 3:
        name1 = input("Enter the name to update ")
        if name1 in d:
            phn1 = int(input("Enter the new phone number to update "))
            email1 = input("Enter the new email address ")
            add1 = input("Enter the new address ")
            c.append(phn1)
            c.append(email1)
            c.append(add1)
            d[name1] = c
            print("Successfully Updated!")
        else:
            print("Not Available ")
    elif ch == 4:
        name1 = input("Enter the name to delete ")
        if name1 in d:
            d.pop(name1)
            print("Successfully Deleted!")
        else:
            print("Not Available ")
    elif ch == 5:
        if not d:
            print("No Contacts Available!")
        else:
            print("Name\t\t\tPhone Number\t\t\t\tEmail\t\t\t\t\tAddress ")
            for i in d:
                print(i, "\t\t\t", d[i][0], "\t\t\t\t",
                      d[i][1], "\t\t\t\t\t", d[i][2])

    else:
        print("Invalid Choice")
