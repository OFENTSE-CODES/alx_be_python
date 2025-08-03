# shopping_list_manager.py

# Function to display the menu
def display_menu(items):
    print("\nShopping List Manager")
    print("1. Add Item {item}")
    print("2. Remove Item {item}")
    print("3. View List")
    print("4. Exit")

# Main function where list operations happen
def main():
    # Empty list for shopping items
    shopping_list = []

    # Loop for menu interaction
    while True:
        display_menu()  # Show the menu
        try:
            # Input must be a number for the menu choice
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("❗ Invalid input. Please enter a number (1–4).")
            continue

        # Option 1: Add item to the list
        if choice == 1:
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"✅ '{item}' has been added to the shopping list.")
            else:
                print("⚠️ Please enter a valid item name.")

        # Option 2: Remove item from the list
        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"❌ '{item}' has been removed from the shopping list.")
            else:
                print(f"⚠️ '{item}' was not found in the shopping list.")

        # Option 3: View the current list
        elif choice == 3:
            if shopping_list:
                print("\n🛒 Your Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("🛒 The shopping list is currently empty.")

        # Option 4: Exit the program
        elif choice == 4:
            print("👋 Goodbye!")
            break

        # Handle invalid number choices
        else:
            print("❗ Invalid choice. Please select a number between 1 and 4.")

# Entry point of the script
if __name__ == "__main__":
    main()