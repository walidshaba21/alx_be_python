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
            item = input("Enter the item to add: ")
            item = item.lower()
            shopping_list.append(item)
            print(f" '{item}' has beed added.")
            cont = input("do you wish to continue operations Y/N: ")
            cont = cont.lower()
            if cont == "n":
                break
        elif choice == '2':
            item = input("Enter item to remove: ")
            item = item.lower()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed.")
            else:
                print(f"'{item}' not found in the list.")
            cont = input("do you wish to continue operations Y/N: ")
            cont = cont.lower()
            if cont == "n":
                break
        elif choice == '3':
            if shopping_list == []:
                print("Your shopping list is empty")
            else: 
                print("Your shopping List:")
                for item in shopping_list:
                    print("-" + item)
            cont = input("do you wish to continue operations Y/N: ")
            cont = cont.lower()
            if cont == "n":
                break
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 
