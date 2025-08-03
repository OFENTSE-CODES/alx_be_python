def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # array to store items

    while True:
        display_menu()  # display menu inside loop
        try:
            choice = int(input("Enter your choice (1-4): "))  # ensure numeric input
        except ValueError:
            print("❗ Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f" '{item}' added to the shopping list.")
            else:
                print(" Please enter a valid item name.")

        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif choice == 3:
            if shopping_list:
                print("\n Your Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print(" Your shopping list is currently empty.")

        elif choice == 4:
            print(" Goodbye!")
            break

        else:
            print("❗ Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()