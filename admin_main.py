def admin_dashboard():
    while True:
        print('''\nAdmin Dashboard:
              
                1. Add Staff
                2. Update Staff
                3. View Staff
                4. Delete Staff
                5. Logout
              ''')
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Add Staff function called")
        elif choice == '2':
            print("Update Staff function called")
        elif choice == '3':
            print("View Staff function called")
        elif choice == '4':
            print("Delete Staff function called")
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")

