# temp_conversion_tool.py

# Define Global Conversion Factors
# This factor is used to convert Fahrenheit to Celsius.
# Formula: (F - 32) × (5/9)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

# This factor is used to convert Celsius to Fahrenheit.
# Formula: (C × 9/5) + 32
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Conversion function: Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Conversion function: Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main user interaction
def main():
    try:
        temp_input = input("Enter the temperature value: ")
        temperature = float(temp_input)  # May raise ValueError

        scale = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if scale == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted:.2f}°F")
        elif scale == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted:.2f}°C")
        else:
            raise ValueError("Invalid scale. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Run the script
if __name__ == "__main__":
    main()