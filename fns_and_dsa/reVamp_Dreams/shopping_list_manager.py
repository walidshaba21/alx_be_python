def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add to the List: ")
            item = item.lower()
            shopping_list.append(item)
            print(f"'{item}' has been added")
            choice2 = input("Do you wish to continue? Y/n: ")
            choice2 = choice2.lower()
            if choice2 == 'n':
                break
        elif choice == '2':
            item = input("Enter the item to remove from the list: ")
            item = item.lower()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list")
            else:
                print("Item not found in the list.")
            choice2 = input("Do you wish to continue? Y/n: ")
            choice2 = choice2.lower()
            if choice2 == 'n':
                break
        elif choice == '3':
            for item in shopping_list:
                print(f"-{item}")
            choice2 = input("Do you wish to continue? Y/n: ")
            choice2 = choice2.lower()
            if choice2 == 'n':
                break
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
