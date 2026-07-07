print("=" * 45)
print("      SECURE PASSWORD MANAGER")
print("=" * 45)

while True:
    print("\nChoose an option:")
    print("1. Add New Password")
    print("2. View Saved Passwords")
    print("3. Search Password")
    print("4. Delete Password")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        website = input("Enter Website Name: ")
        username = input("Enter Username/Email: ")
        password = input("Enter Password: ")

        with open("passwords.txt", "a") as file:
            file.write(f"{website}|{username}|{password}\n")

        print("\n✅ Password saved successfully!")

    elif choice == "2":
        try:
            with open("passwords.txt", "r") as file:
                data = file.readlines()

            if len(data) == 0:
                print("\nNo passwords saved.")
            else:
                print("\n========== SAVED PASSWORDS ==========")
                for line in data:
                    website, username, password = line.strip().split("|")
                    print(f"\nWebsite : {website}")
                    print(f"Username: {username}")
                    print(f"Password: {password}")
                    print("-" * 35)

        except FileNotFoundError:
            print("\nNo password file found.")

    elif choice == "3":
        search = input("Enter Website Name: ")

        found = False

        try:
            with open("passwords.txt", "r") as file:
                for line in file:
                    website, username, password = line.strip().split("|")

                    if website.lower() == search.lower():
                        print("\nPassword Found")
                        print(f"Website : {website}")
                        print(f"Username: {username}")
                        print(f"Password: {password}")
                        found = True
                        break

            if not found:
                print("\nPassword not found.")

        except FileNotFoundError:
            print("\nNo password file found.")

    elif choice == "4":
        delete = input("Enter Website Name to Delete: ")

        try:
            with open("passwords.txt", "r") as file:
                lines = file.readlines()

            with open("passwords.txt", "w") as file:
                deleted = False

                for line in lines:
                    website, username, password = line.strip().split("|")

                    if website.lower() != delete.lower():
                        file.write(line)
                    else:
                        deleted = True

            if deleted:
                print("\n✅ Password deleted successfully!")
            else:
                print("\nWebsite not found.")

        except FileNotFoundError:
            print("\nNo password file found.")

    elif choice == "5":
        print("\nThank you for using Secure Password Manager!")
        break

    else:
        print("\nInvalid choice! Please try again.")