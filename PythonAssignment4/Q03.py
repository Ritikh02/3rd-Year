# Design and develop a menu-driven Python program for the following list operations.
# a. Create a list of N integers
# b. Display the list elements
# c. Insert an element at a specific position
# d. Delete an element at a given position
# e. Exit

def menu():
    lst = []
    while True:
        print("\n1. Create a list")
        print("2. Display list")
        print("3. Insert element")
        print("4. Delete element")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            lst = [int(input("Enter element: ")) for _ in range(int(input("Enter size of list: ")))]
        elif choice == 2:
            print("List:", lst)
        elif choice == 3:
            index = int(input("Enter index: "))
            value = int(input("Enter value: "))
            lst.insert(index, value)
        elif choice == 4:
            index = int(input("Enter index to delete: "))
            lst.pop(index)
        elif choice == 5:
            break
        else:
            print("Invalid choice!")

menu()
