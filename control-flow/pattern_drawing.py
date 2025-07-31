size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to iterate over each row
while row < size:
    # For each row, use a for loop to print '*' size times
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1